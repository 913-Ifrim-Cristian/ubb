//
// Created by Cristi Ifrim on 5/4/2022.
//
#include "UI.h"
#include "RealEstateAgency.h"


int main() {

    RealEstateAgency service;
    UI ui{service};
    ui.start();

}
