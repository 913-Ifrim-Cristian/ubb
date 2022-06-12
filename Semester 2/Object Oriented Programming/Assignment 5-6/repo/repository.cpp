//
// Created by Cristi Ifrim on 3/19/2022.
//

#include "repository.h"
#include "../exceptions/exceptions.h"
#include "../utilities/utility.h"

int Repository::search(const std::string& name) {
    /*
     * Searches an item in the repository and returns it's position or -1 if it doesn't exit.
     */

    for(int i = 0; i < this->data.getSize(); ++i)
        if(utility::toLower(this->data[i].getName()) == utility::toLower(name))
            return i;

    return -1;
}

void Repository::add(Dog dog) {
    /*
     * Adds a Dog element to the Repo.
     */

    int index = this->search(dog.getName());
    if(index != -1)
        throw VALUE_ERROR;

    this->data.add(dog);
}

void Repository::remove(const std::string& name) {
    /*
     * Removes a Dog element from the Repo.
     */

    int index = this->search(name);
    if(index == -1)
        throw ELEM_ERROR;

    this->data.remove(index);
}
