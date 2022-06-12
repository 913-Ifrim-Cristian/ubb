//
// Created by Cristi Ifrim on 3/21/2022.
//

#include "service.h"
#include "exceptions.h"
#include "utility.h"
#include <algorithm>


AdminService::AdminService(Repository& r) : repo{ r }, whereOnStack{ -1 } {
    /*
     * Constructor method for the AdminService Class.
     */
    /*repo.add(Dog{"Lucki", "Caucasian", 1, "https://tinyurl.com/k4jxx92p"});
    repo.add(Dog{"Mex", "Unknown", 8, "https://tinyurl.com/33ewep8d"});
    repo.add(Dog{"Rex", "Golden Retriever", 2, "https://tinyurl.com/3ebx7t7e"});
    repo.add(Dog{"Lupu", "German Sheperd", 1, "https://tinyurl.com/yfv8rmaa"});
    repo.add(Dog{"Lulu", "Beagle", 5, "https://tinyurl.com/2tykxp2b"});
    repo.add(Dog{"Martin", "Saint Bernard", 3, "https://tinyurl.com/24mxjs7t"});
    repo.add(Dog{"Natasha", "Pitbull", 2, "https://tinyurl.com/2p92n3xp"});
    repo.add(Dog{"Katyusha", "Doberman", 4, "https://tinyurl.com/bdcjafjc"});
    repo.add(Dog{"Relu", "Labrador", 2, "https://tinyurl.com/3wr8eav7"});
    repo.add(Dog{"Ursu", "Pug", 4, "https://tinyurl.com/4t657wa8"});*/
}

void AdminService::add(const std::string& name, const std::string& breed, int age, const std::string& url) {
    /*
     * Adds a Dog to the repository.
     */
    this->validator.validateInput(name, breed, url, age);
    Dog d{ name, breed, age, url };
    this->repo.add(d);

    std::unique_ptr<Action> action = std::make_unique<ActionAdd>(this->repo, d);
    this->whereOnStack++;
    if (this->whereOnStack < this->actions.size()) {
        this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
    }
    actions.push_back(std::move(action));
}

void AdminService::remove(const std::string& name) {
    /*
     * Removes a Dog from the repository.
     */
    this->validator.validateInput(name, "not null", "not null", 2);
    int index = this->repo.search(name);
    Dog d;
    if (index != -1)
       d = this->repo[index];

    this->repo.remove(name);

    std::unique_ptr<Action> action = std::make_unique<ActionRemove>(this->repo, d);
    this->whereOnStack++;
    if (this->whereOnStack < this->actions.size()) {
        this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
    }
    actions.push_back(std::move(action));
}


void AdminService::update(const std::string& name, int age) {
    /*
     * Overloaded update function to update the age of a Dog from the repository.
     */
    this->validator.validateInput(name, "not null", "not null", age);
    int index = this->repo.search(name);

    if(index == -1)
        throw RepositoryException("The element is not in the database!");

    Dog d = this->repo.find(name);
    this->repo[index].setAge(age);

    std::unique_ptr<Action> action = std::make_unique<ActionUpdate>(this->repo, this->repo[index], d);
    this->whereOnStack++;
    if (this->whereOnStack < this->actions.size()) {
        this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
    }
    actions.push_back(std::move(action));

}

void AdminService::update(const std::string& name, int updateType, const std::string& str) {
    /*
     * Updates a Dog name, breed or URL link.
     */

    this->validator.validateInput(name, str, str, 2);
    int index = this->repo.search(name);

    if(index == -1)
        throw RepositoryException("The element is not in the database!");

    Dog d = this->repo.find(name);

    switch(updateType) {
        case UPDATE_NAME:
            if(this->repo.search(str) != -1)
                throw RepositoryException("There is another dog with that name in the database!");

            this->repo[index].setName(str);
            break;
        case UPDATE_BREED:
            this->repo[index].setBreed(str);
            break;
        case UPDATE_PHOTOGRAPH:
            this->repo[index].setPhotograph(str);
            break;
        default:
            break;
    }

    std::unique_ptr<Action> action = std::make_unique<ActionUpdate>(this->repo, this->repo[index], d);
    this->whereOnStack++;
    if (this->whereOnStack < this->actions.size()) {
        this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
    }
    actions.push_back(std::move(action));

}

void AdminService::cascadeUpdate(const std::string& name, std::vector<std::string> args, int age) {

    this->validator.validateInput(name, "default", "default", age);
    int index = this->repo.search(name);

    if (index == -1)
        throw RepositoryException("The element is not in the database!");

    Dog d = this->repo.find(name);

    if (!args[0].empty()) {
        if (this->repo.search(args[0]) != -1 && args[0] != name)
            throw RepositoryException("There is another dog with that name in the database!");
        this->repo[index].setName(args[0]);
    }

    if (age != -1)
        this->repo[index].setAge(age);

   if (!args[1].empty())
        this->repo[index].setBreed(args[1]);

   if (!args[2].empty())
        this->repo[index].setPhotograph(args[2]);

   std::unique_ptr<Action> action = std::make_unique<ActionUpdate>(this->repo, this->repo[index], d);
   this->whereOnStack++;
   if (this->whereOnStack < this->actions.size()) {
       this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
   }
   actions.push_back(std::move(action));
}

std::vector<Dog> UserService::getDogListByFilter(const std::string & breed, int age) {
    /*
     * Gets a list of Dog elements that respect a given filter.
     */

    std::vector<Dog> dogList;
    std::vector<Dog> copy = this->repo.getData();

    std::copy_if(copy.begin(), copy.end(), std::back_inserter(dogList),
                 [&breed, age](const Dog& d) {
        return (breed.empty() || utility::toLower(d.getBreed()).find(utility::toLower(breed)) != std::string::npos) && age >= d.getAge();
    });

    return dogList;
}

void UserService::adoptDog(Dog& d) {
    /*
     * Adds a dog to the adoption list
     */
    this->adoptionList->adopt(d);

    std::unique_ptr<Action> action = std::make_unique<ActionAdopt>(this->adoptionList, this->repo, d);
    this->whereOnStack++;
    if (this->whereOnStack < this->actions.size()) {
        this->actions.erase(this->actions.begin() + this->whereOnStack, this->actions.end());
    }
    actions.push_back(std::move(action));
}

void UserService::init(int type) {
    if(type == 0) {
        this->adoptionList = new AdoptionListHTML("adoption.html");
    }
    else {
        this->adoptionList = new AdoptionListCSV("adoption.csv");
    }
}

void UserService::openAdoptionList() {
    this->adoptionList->open();
}

void AdminService::undo()
{
    if (this->whereOnStack == -1)
        throw std::exception("ERROR: No more to undo!");
    this->actions[this->whereOnStack--]->executeUndo();
}

void AdminService::redo()
{
    if (this->whereOnStack == this->actions.size() - 1)
        throw std::exception("ERROR: No more to redo!");
    this->actions[++this->whereOnStack]->executeRedo();
}

void UserService::undo()
{
    if (this->whereOnStack == -1)
        throw std::exception("ERROR: No more to undo!");
    this->actions[this->whereOnStack--]->executeUndo();
}

void UserService::redo()
{
    if (this->whereOnStack == this->actions.size() - 1)
        throw std::exception("ERROR: No more to redo!");
    this->actions[++this->whereOnStack]->executeRedo();
}
