//
// Created by Cristi Ifrim on 3/20/2022.
//

#include "ui.h"
#include <string>
#include <iostream>
#include "../utilities/utility.h"

void UI::start() {
    std::string option;

    std::cout << "Welcome to the Pet Monitoring app. May I ask who you are?(user/admin/exit)\n";
    std::cout << ">>> ";
    std::getline(std::cin, option);

    while(option != "exit") {

        if (utility::toLower(option) == "admin")
            this->admin();

        else if (utility::toLower(option) == "user")
            this->user();
        else
            std::cout << "ERROR: Invalid option!\n";

        std::cout << "Welcome to the Pet Monitoring app. May I ask who you are?(user/admin/exit)\n";
        std::cout << ">>> ";
        std::getline(std::cin, option);
    }

    std::cout << "Goodbye!\n\n";
}

void adminMenu() {
    std::cout << "--------------------\n";
    std::cout << "/       MENU       /\n";
    std::cout << "--------------------\n";
    std::cout << "1. Add a dog\n--------------------\n2. Remove a dog\n--------------------\n3. Update a dog"
                 "\n--------------------\n4. See all dogs\n--------------------\n5. Exit\n--------------------\n";
}

void UI::adminShow() {

    if(this->__admin.getRepo().getSize() == 0) {
        std::cout << "ERROR: There are no elements in the repo!";
        return;
    }

    Repository r = this->__admin.getRepo();

    for(int i = 0; i < this->__admin.getRepo().getSize(); ++i)
        std::cout << "Dog name: " << this->__admin.getRepo()[i].getName() << ", breed: " << this->__admin.getRepo()[i].getBreed(),
        std::cout << ", age: " << this->__admin.getRepo()[i].getAge() << ".\nURL: " << this->__admin.getRepo()[i].getPhotograph() << ".\n\n";

    std::cout << "\n";

}

void UI::adminAdd() {
    std::string name, breed, url;
    int age;

    std::cout << "Please enter the name of the dog: ";
    std::getline(std::cin, name);

    std::cout << "Please enter the breed of the dog: ";
    std::getline(std::cin, breed);

    std::cout << "Please enter the age of the dog: ";
    age = utility::readInteger();

    std::cout << "Please enter the URL of the dog: ";
    std::getline(std::cin, url);

    this->__admin.add(name, breed, age, url);
    std::cout << "SUCCESS: " << name << " has been added to the database.\n";
    std::cout << "INFO: Breed: " << breed << ", Age: " << age << ".\n";

}

void UI::adminRemove() {
    std::string name;

    std::cout << "Please enter the name of the dog: ";
    std::getline(std::cin, name);

    this->__admin.remove(name);

    std::cout << "SUCCESS: " <<  name << " has been removed from the database.\n";
}

void UI::updateName() {

    std::string name, newName;
    std::cout << "Please enter the actual name of the dog: ";
    std::getline(std::cin, name);

    std::cout << "Please enter the new name of the dog: ";
    std::getline(std::cin, newName);

    this->__admin.update(name, UPDATE_NAME, newName);

    std::cout << "SUCCESS: " << name << "'s name has been updated to " << newName << ".\n";
}

void UI::updateBreed() {

    std::string name, newName;
    std::cout << "Please enter the actual name of the dog: ";
    std::getline(std::cin, name);

    std::cout << "Please enter the new breed of the dog: ";
    std::getline(std::cin, newName);

    this->__admin.update(name, UPDATE_BREED, newName);

    std::cout << "SUCCESS: " << name << "'s breed has been updated to " << newName << ".\n";

}

void UI::updateAge() {

    std::string name;
    int newName;
    std::cout << "Please enter the actual name of the dog: ";
    std::getline(std::cin, name);

    std::cout << "Please enter the new age of the dog: ";
    newName = utility::readInteger();

    this->__admin.update(name, newName);
    std::cout << "SUCCESS: " << name << "'s age has been updated to " << newName << ".\n";

}

void UI::updatePhoto() {

    std::string name, newName;
    std::cout << "Please enter the actual name of the dog: ";
    std::getline(std::cin, name);

    std::cout << "Please enter the new photograph of the dog: ";
    std::getline(std::cin, newName);

    this->__admin.update(name, UPDATE_PHOTOGRAPH, newName);

    std::cout << "SUCCESS: " << name << "'s age has been updated to " << newName << ".\n";

}


void UI::adminUpdate() {
    std::string option;

    std::cout << "What do you want to update?(name, breed, age, photograph): ";
    std::getline(std::cin, option);

    if(utility::toLower(option) == "name")
        this->updateName();
    else if(utility::toLower(option) == "breed")
        this->updateBreed();
    else if(utility::toLower(option) == "age")
        this->updateAge();
    else if(utility::toLower(option) == "photograph")
        this->updatePhoto();
    else
        std::cout << "ERROR: Invalid option!\n\n";

}

void UI::admin() {
    std::cout << "Hello, admin! What's your desire?\n";

    while(true) {

        adminMenu();

        std::cout << "Please select an option: ";

        std::string option;
        std::getline(std::cin, option);
        std::cout << std::endl;

        if(option == "5")
            return;
        try {
            if(option == "1")
                this->adminAdd();
            else if(option == "2")
                this->adminRemove();
            else if(option == "3")
                this->adminUpdate();
            else if(option == "4")
                this->adminShow();
            else
                std::cout << "ERROR: Invalid option!\n\n";
        }
        catch(int errorid) {
            std::cout << errorMsg(errorid) << "\n\n";
        }
        catch(std::exception& e) {
            std:: cout << e.what() << "\n\n";
        }
    }

}


void userMenu() {
    std::cout << "--------------------\n";
    std::cout << "/       MENU       /\n";
    std::cout << "--------------------\n";
    std::cout << "1. See all dogs\n--------------------\n2. See dogs by filter\n--------------------\n3. See adoption list"
                 "\n--------------------\n4. Exit\n--------------------\n";
}

void UI::userShow(int option) {

    DynamicArray<Dog> dogList;
    std::string input;

    if(option == 2) {
        std::string breed;
        int age;

        std::cout << "Please enter the breed: ";
        std::getline(std::cin, breed);

        std::cout << "Please enter the age: ";
        age = utility::readInteger();

        if(age < 0) {
            std::cout << "ERROR: Age cannot be negative.\n\n";
            return;
        }

        dogList = this->__user.getDogListByFilter(breed, age);
    }
    else
        dogList = this->__user.getDogList();

    int size = dogList.getSize();
    if(size == 0) {
        std::cout << "ERROR: Dog list is empty.\n\n";
        return;
    }

    int index = 0;
    while(true) {
        std::cout << "Dog name: " << dogList[index].getName() << ", breed: " << dogList[index].getBreed(),
                std::cout << ", age: " << dogList[index].getAge() << ".\nURL: " << "https://" << dogList[index].getPhotograph() << ".\n\n";

        std::string command = "start ";
        system(command.append(dogList[index].getPhotograph()).c_str());

        std::cout << "What do you want to do(adopt/next/exit): ";
        std::getline(std::cin, input);

        if(utility::toLower(input) == "exit")
            return;

        if(utility::toLower(input) == "next") {
            if(index >= dogList.getSize() - 1 && index > 0)
                index = 0;
            else if(index < dogList.getSize() - 1)
                index++;
        }


        else if(utility::toLower(input) == "adopt") {
            this->__user.adoptDog(dogList[index]);
            this->__admin.remove(dogList[index].getName());

            std::cout << "SUCCESS: " << dogList[index].getName() << " has been adopted.\n\n";
            dogList.remove(index);

            if(index >= dogList.getSize() - 1) {
                if(dogList.getSize() == 0) {
                    std::cout << "FINAL: The list has emptied.\n\n";
                    return;
                }
                index = 0;
            }
        }
        else
            std::cout << "ERROR: Invalid option.\n";
    }
}

void UI::userAdoptionList() {
    int size = this->__user.getAdoptionList().getSize();
    if(size == 0) {
        std::cout << "ERROR: The adoption list is empty.\n\n";
        return;
    }

    for(int i = 0; i < size; ++i)
        std::cout << "Dog name: " << this->__user.getAdoptionList()[i].getName() << ", breed: " << this->__user.getAdoptionList()[i].getBreed(),
        std::cout << ", age: " << this->__user.getAdoptionList()[i].getAge() << ".\nURL: " << this->__user.getAdoptionList()[i].getPhotograph() << ".\n\n";

}

void UI::user() {
    std::cout << "Hello, user! What's your desire?\n";

    while(true) {
        userMenu();

        std::cout << "Please select an option: ";

        std::string option;
        std::getline(std::cin, option);
        std::cout << std::endl;

        if (option == "4")
            return;
        try {
            if (option == "1")
                this->userShow(0);
            else if (option == "2")
                this->userShow(2);
            else if (option == "3")
                this->userAdoptionList();
            else
                std::cout << "ERROR: Invalid option!\n\n";
        }
        catch (int errorid) {
            std::cout << errorMsg(errorid) << "\n\n";
        }
        catch (std::exception &e) {
            std::cout << e.what() << "\n\n";
        }
    }
}