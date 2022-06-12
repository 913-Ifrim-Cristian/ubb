//
// Created by Cristi Ifrim on 3/21/2022.
//

#include "service.h"
#include "../exceptions/exceptions.h"
#include "../utilities/utility.h"
#include <algorithm>


AdminService::AdminService(Repository& r): repo{r} {
    /*
     * Constructor method for the AdminService Class.
     */
/*    repo.add(Dog{"Lucki", "Caucasian", 1, "https://tinyurl.com/k4jxx92p"});
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
    this->repo.add(Dog{name, breed, age, url});
}

void AdminService::remove(const std::string& name) {
    /*
     * Removes a Dog from the repository.
     */
    this->validator.validateInput(name, "not null", "not null", 2);
    this->repo.remove(name);
}


void AdminService::update(const std::string& name, int age) {
    /*
     * Overloaded update function to update the age of a Dog from the repository.
     */
    this->validator.validateInput(name, "not null", "not null", age);
    int index = this->repo.search(name);

    if(index == -1)
        throw RepositoryException("The element is not in the database!");

    this->repo[index].setAge(age);

}

void AdminService::update(const std::string& name, int updateType, const std::string& str) {
    /*
     * Updates a Dog name, breed or URL link.
     */

    this->validator.validateInput(name, str, str, 2);
    int index = this->repo.search(name);

    if(index == -1)
        throw RepositoryException("The element is not in the database!");


    switch(updateType) {
        case UPDATE_NAME:
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

}

std::vector<Dog> UserService::getDogListByFilter(const std::string & breed, int age) {
    /*
     * Gets a list of Dog elements that respect a given filter.
     */

    std::vector<Dog> dogList;
    std::vector<Dog> copy = this->repo.getData();

    std::copy_if(copy.begin(), copy.end(), std::back_inserter(dogList),
                 [&breed, age](const Dog& d) {
        return (breed.empty() || utility::toLower(breed) == utility::toLower(d.getBreed())) && age >= d.getAge();
    });

    return dogList;
}

void UserService::adoptDog(const Dog& d) {
    /*
     * Adds a dog to the adoption list
     */
    this->adoptionList->adopt(d);
}

void UserService::init(int type) {
    if(type == 0) {
        this->adoptionList = new AdoptionListHTML("../adoption.html");
    }
    else {
        this->adoptionList = new AdoptionListCSV("../adoption.csv");
    }
}

void UserService::openAdoptionList() {
    this->adoptionList->open();
}
