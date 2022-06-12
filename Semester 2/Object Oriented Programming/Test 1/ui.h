//
// Created by Cristi Ifrim on 4/6/2022.
//

#ifndef T1_913_IFRIM_CRISTIAN_1_UI_H
#define T1_913_IFRIM_CRISTIAN_1_UI_H


#include "service.h"

class UI {
    Service service;

public:
    UI(Service& srv): service{srv} {}

    void start();

    void remove();

    void showBills();

    void showUnpaidBills();

    void showTotal();
};


#endif //T1_913_IFRIM_CRISTIAN_1_UI_H
