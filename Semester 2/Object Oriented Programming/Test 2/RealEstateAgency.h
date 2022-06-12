//
// Created by Cristi Ifrim on 5/4/2022.
//

#ifndef T2_913_IFRIM_CRISTIAN_1_REALESTATEAGENCY_H
#define T2_913_IFRIM_CRISTIAN_1_REALESTATEAGENCY_H

#include <vector>
#include "Dwelling.h"
#include "Client.h"

class RealEstateAgency {
    std::vector<Dwelling> dwellings{};
    std::vector<Client*> clients{};

public:
    RealEstateAgency();
    Dwelling addDwelling(double price, bool isProfitable);
    int removeClient(const std::string& name);
    std::vector<Dwelling> getDwellings() { return this->dwellings; }
    std::vector<Client*> getClients() { return this->clients; }
    std::vector<Client*> getInterestedClients(Dwelling d);
    void writeToFile(const std::string& filename);
};


#endif //T2_913_IFRIM_CRISTIAN_1_REALESTATEAGENCY_H
