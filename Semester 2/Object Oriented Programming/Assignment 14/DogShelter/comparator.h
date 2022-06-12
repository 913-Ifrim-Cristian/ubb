//
// Created by Cristi Ifrim on 6/6/2022.
//

#pragma once
#include "Dog.h"
#include <vector>
#include <memory>

template<class T>
class Comparator {
public:
    virtual bool compare(T a, T b) = 0;
    virtual ~Comparator() {}
};

class ComparatorAscendingByName : public Comparator<Dog> {
public:
    bool compare(Dog a, Dog b) override;
};

class ComparatorDescendingByAge : public Comparator<Dog> {
public:
    bool compare(Dog a, Dog b) override;
};

template<class T>
void sort(std::vector<T>&, std::unique_ptr<Comparator<T>>);

