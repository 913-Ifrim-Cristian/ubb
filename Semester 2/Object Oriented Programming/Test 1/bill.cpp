//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "bill.h"

Bill::Bill(const std::string &serial, const std::string &company, int d, int m, int y, double sum, bool isPaid) {
    this->serial = serial;
    this->company = company;
    this->date.d = d;
    this->date.m = m;
    this->date.y = y;
    this->sum = sum;
    this->isPaid = isPaid;
}
