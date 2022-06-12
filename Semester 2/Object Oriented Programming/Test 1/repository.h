//
// Created by Cristi Ifrim on 4/6/2022.
//

#ifndef T1_913_IFRIM_CRISTIAN_1_REPOSITORY_H
#define T1_913_IFRIM_CRISTIAN_1_REPOSITORY_H

#include "bill.h"
#include <vector>

class Repository {
    std::vector<Bill> data;

public:
    void init();
    int getSize() { return this->data.size(); }
    int search(const std::string&);
    void remove(int index);
    std::vector<Bill> getList(int filter = 0);
};


#endif //T1_913_IFRIM_CRISTIAN_1_REPOSITORY_H
