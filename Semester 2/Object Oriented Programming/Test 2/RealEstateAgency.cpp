//
// Created by Cristi Ifrim on 5/4/2022.
//

#include "RealEstateAgency.h"
#include <algorithm>
#include <fstream>

Dwelling RealEstateAgency::addDwelling(double price, bool isProfitable) {
    int prof = 0;
    if(isProfitable == true)
        prof = 1;
    Dwelling d{price, prof};
    this->dwellings.push_back(d);
    return d;
}

int RealEstateAgency::removeClient(const std::string &name) {
    std::vector<Client*>::iterator result;
    int index = -1;
    for(int i = 0; i < this->clients.size(); ++i)
        if(this->clients[i]->getName() == name)
            index = i;
    if(index != -1)
        this->clients.erase(this->clients.begin() + index);
    return index;
}

std::vector<Client *> RealEstateAgency::getInterestedClients(Dwelling d) {
    std::vector<Client*> result;
    for(auto it: this->clients) {
        if(it->isInterested(d))
            result.push_back(it);
    }
    return result;
}

void RealEstateAgency::writeToFile(const std::string& filename) {
    std::ofstream f(filename);

    for(auto it: this->clients) {
        f << it->toString();
    }

    f.close();
}

RealEstateAgency::RealEstateAgency() {
    Client* c1 = new Person{"Aurel", 1900.5};
    Client* c2 = new Person{"Cristi", 6000.2};
    Client* c3 = new Company{"OIL COMPANY", 190000.7, 50000.2};
    Client* c4 = new Company{"IT COMPANY", 80520.2, 91252.3};
    this->clients.push_back(c1);
    this->clients.push_back(c2);
    this->clients.push_back(c3);
    this->clients.push_back(c4);

    Dwelling d{4000, 1};
    Dwelling e{1200, 0};
    this->dwellings.push_back(d);
    this->dwellings.push_back(e);
}
