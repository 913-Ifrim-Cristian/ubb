//
// Created by Cristi Ifrim on 5/4/2022.
//

#ifndef T2_913_IFRIM_CRISTIAN_1_UI_H
#define T2_913_IFRIM_CRISTIAN_1_UI_H

#include "RealEstateAgency.h"

class UI {
    RealEstateAgency& service;
public:
    UI(RealEstateAgency& srv): service{srv} {}
    void printMenu();
    void start();

    double readDouble();

    void add();
    void remove();
    void show();
    void save();
};


#endif //T2_913_IFRIM_CRISTIAN_1_UI_H
