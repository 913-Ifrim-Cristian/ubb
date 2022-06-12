//
// Created by Cristi Ifrim on 3/19/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H
#define A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H

#include "../domain/dog.h"
#include "../array/DynamicArray.h"


class Repository {

    DynamicArray<Dog> data;

public:
    int search(const std::string&);
    void add(Dog);
    void remove(const std::string&);
    int getSize() { return this->data.getSize(); }
    const DynamicArray<Dog>& getData() { return this->data; }
    Dog& operator[](int index) { return this->data[index]; }

};


#endif //A5_6_913_IFRIM_CRISTIAN_REPOSITORY_H
