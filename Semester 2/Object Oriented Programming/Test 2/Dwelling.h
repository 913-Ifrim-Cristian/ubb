//
// Created by Cristi Ifrim on 5/4/2022.
//

#ifndef T2_913_IFRIM_CRISTIAN_1_DWELLING_H
#define T2_913_IFRIM_CRISTIAN_1_DWELLING_H


class Dwelling {
    double price;
    bool isProfitable;

public:
    Dwelling(double prc, int profit): price{prc} { if(profit == 0) isProfitable = false; else isProfitable = true; }
    double getPrice() const { return this->price; }
    bool getProfitable() const { return this->isProfitable;}
};


#endif //T2_913_IFRIM_CRISTIAN_1_DWELLING_H
