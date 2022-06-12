//
// Created by Cristi Ifrim on 3/19/2022.
//

#pragma once

#include "Dog.h"
#include <vector>


class Repository {

protected:
    std::vector<Dog> data;

public:
    virtual int search(const std::string&);
    virtual void add(const Dog&);
    virtual void remove(const std::string&);
    virtual int getSize() { return this->data.size(); }
    virtual std::vector<Dog> getData() { return this->data; }
    virtual Dog& operator[](int index);
    virtual Dog find(const std::string& name);
    virtual ~Repository() = default;

};
