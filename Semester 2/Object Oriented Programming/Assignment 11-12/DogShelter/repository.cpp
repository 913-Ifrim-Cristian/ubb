//
// Created by Cristi Ifrim on 3/19/2022.
//

#include "repository.h"
#include "exceptions.h"
#include "utility.h"
#include <algorithm>

int Repository::search(const std::string& name) {
    /*
     * Searches an item in the repository and returns it's position or -1 if it doesn't exit.
     */

    auto it = std::find_if(this->data.begin(), this->data.end(), [&name](const Dog& d) {
        return utility::toLower(d.getName()) == utility::toLower(name);
    });

    if(it == this->data.end())
        return -1;

    int index = it - this->data.begin();
    return index;
}

void Repository::add(const Dog& dog) {
    /*
     * Adds a Dog element to the Repo.
     */

    int index = this->search(dog.getName());
    if(index != -1)
        throw RepositoryException("The element is already in the database!");

    this->data.push_back(dog);
}

void Repository::remove(const std::string& name) {
    /*
     * Removes a Dog element from the Repo.
     */

    int index = this->search(name);
    if(index == -1)
        throw RepositoryException("The element is not in the database!");

    this->data.erase(this->data.begin() + index);
}

Dog &Repository::operator[](int index) {

    if(index < 0 || index >= this->data.size())
        throw RepositoryException("Array index out of bounds!");

    return this->data[index];
}

Dog Repository::find(const std::string& name)
{
    for (auto it : this->data) {
        if (utility::toLower(it.getName()) == utility::toLower(name))
            return it;
    }
}
