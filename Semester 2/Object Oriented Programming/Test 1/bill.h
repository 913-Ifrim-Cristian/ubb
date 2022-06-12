//
// Created by Cristi Ifrim on 4/6/2022.
//

#ifndef T1_913_IFRIM_CRISTIAN_1_BILL_H
#define T1_913_IFRIM_CRISTIAN_1_BILL_H


#include <string>

class Bill {
private:
    std::string serial;
    std::string company;
    struct {
        int d, m, y;
    } date{};
    double sum;
    bool isPaid;

public:
    Bill(const std::string& serial, const std::string& company, int d, int m, int y, double sum, bool isPaid);
    std::string getSerial() const { return this->serial; }
    std::string getCompany() const { return this->company; }
    int getDateYear() const { return this->date.y;}
    int getDateMonth() const { return this->date.m;}
    int getDateDay() const { return this->date.d;}
    double getSum() const { return this->sum; }
    bool getState() { return this->isPaid; }
};


#endif //T1_913_IFRIM_CRISTIAN_1_BILL_H
