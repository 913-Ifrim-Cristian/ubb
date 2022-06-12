//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "repository.h"
#include <algorithm>
#include "utility.h"

int Repository::search(const std::string& serial) {
    /*
     * Searches an item in the repository and returns it's position or -1 if it doesn't exit.
     */

    auto it = std::find_if(this->data.begin(), this->data.end(), [&serial](const Bill& d) {
        return utility::toLower(d.getSerial()) == utility::toLower(serial);
    });

    if(it == this->data.end())
        return -1;

    int index = it - this->data.begin();
    return index;
}

void Repository::remove(int index) {
    /*
     * Removes an item from the repository
     */
    this->data.erase(this->data.begin() + index);
}

std::vector<Bill> Repository::getList(int filter) {
    /*
     * Gets the list of all bills or only the unpaid ones
     */

    if(filter != 0) {
        std::vector<Bill> newData;
        for(auto it: this->data) {
            if(!it.getState())
                newData.push_back(it);
        }
        return newData;
    }

    return this->data;
}

void Repository::init() {
    /*
     * Initializes the repo
     */
    this->data.emplace_back("A5CD3", "VODAFONE", 25, 02, 2022, 72, true);
    this->data.emplace_back("A5CD4", "TELEKOM", 28, 05, 2022, 53, false);
    this->data.emplace_back("A5CD5", "E-ON", 13, 12, 2021, 90, false);
    this->data.emplace_back("A5CD6", "City Hall", 25, 03, 2022, 121, false);
    this->data.emplace_back("A5CD7", "DIGI", 8, 01, 2022, 25, true);
}
