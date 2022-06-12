//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "service.h"
#include <algorithm>
#include <exception>


void Service::remove(const std::string& serial) {
    /*
     * Removes an element from the repo
     */
    int index = this->r.search(serial);

    if(index == -1)
        throw "ERROR: Element was not found!";

    this->r.remove(index);
}

double Service::getMoneyToPay() {

    std::vector<Bill> data = this->r.getList(1);
    double sum = 0;
    for(auto it: data) {
        sum += it.getSum();
    }
    return sum;

}

std::vector<Bill> Service::sortUnpaid() {
    std::vector<Bill> data = this->r.getList(1);
    std::sort(data.begin(), data.end(), [](const Bill& a, const Bill& b) {
        if(a.getDateYear() < b.getDateYear())
            return true;
        if(a.getDateYear() == b.getDateYear()) {
            if(a.getDateMonth() < b.getDateMonth())
                return true;
            if(a.getDateMonth() == b.getDateMonth()) {
                if (a.getDateDay() <= b.getDateDay())
                    return true;
                return false;
            }
            return false;
        }
        return false;
    });
    return data;
}
