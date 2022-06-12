//
// Created by Cristi Ifrim on 5/4/2022.
//

#ifndef T2_913_IFRIM_CRISTIAN_1_CLIENT_H
#define T2_913_IFRIM_CRISTIAN_1_CLIENT_H

#include "Dwelling.h"
#include <string>

class Client {
protected:
    std::string name;
    double income;
public:
    Client(const std::string& name, double inc): name{name}, income{inc} {}
    std::string getName() const { return this->name; }
    virtual double totalIncome() { return this->income; }
    virtual std::string toString();
    virtual bool isInterested(Dwelling d) { return false; }

};

class Person : public Client {
public:
    Person(const std::string& name, double inc): Client{name, inc} {}
    bool isInterested(Dwelling d) override;
};

class Company: public Client {
    double moneyFromInvestments;

public:
    Company(const std::string& name, double inc, double money): Client{name, inc}, moneyFromInvestments{money} {};
    double totalIncome() override { return this->income + this->moneyFromInvestments; }
    std::string toString() override;
    bool isInterested(Dwelling d) override;
};


#endif //T2_913_IFRIM_CRISTIAN_1_CLIENT_H
