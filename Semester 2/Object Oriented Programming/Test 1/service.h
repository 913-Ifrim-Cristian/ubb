//
// Created by Cristi Ifrim on 4/6/2022.
//

#ifndef T1_913_IFRIM_CRISTIAN_1_SERVICE_H
#define T1_913_IFRIM_CRISTIAN_1_SERVICE_H

#include "repository.h"
#include "bill.h"
#include <string>

class Service {
    Repository& r;

public:
    Service(Repository& repo): r{repo} {
        this->r.init();
    }
    void remove(const std::string&);
    std::vector<Bill> getList() { return this->r.getList(); }
    double getMoneyToPay();
    std::vector<Bill> sortUnpaid();
};


#endif //T1_913_IFRIM_CRISTIAN_1_SERVICE_H
