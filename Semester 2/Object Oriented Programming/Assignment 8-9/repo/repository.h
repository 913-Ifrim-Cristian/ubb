//
// Created by Cristi Ifrim on 3/19/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H
#define A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H

#include "../domain/dog.h"
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
    virtual ~Repository() = default;

};


#endif //A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H
