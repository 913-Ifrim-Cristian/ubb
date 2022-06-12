//
// Created by Cristi Ifrim on 5/4/2022.
//

#include "Client.h"

bool Person::isInterested(Dwelling d) {
    return d.getPrice() / 1000 <= this->income;
}

bool Company::isInterested(Dwelling d) {
    return d.getPrice() / 1000 <= this->totalIncome() && d.getProfitable();
}

std::string Company::toString() {
    std::string result = "";
    result = "Company: " + this->name + ", income: " + std::to_string(this->income) + ", Money from investments: " + std::to_string(this->moneyFromInvestments) + ", total income: ";
    result += std::to_string(this->totalIncome());
    result += "\n";
    return result;
}

std::string Client::toString() {
    std::string result = "";
    result = "Person: " + this->name + ", income: " + std::to_string(this->income) + ", total income: ";
    result += std::to_string(this->totalIncome());
    result += "\n";
    return result;
}
