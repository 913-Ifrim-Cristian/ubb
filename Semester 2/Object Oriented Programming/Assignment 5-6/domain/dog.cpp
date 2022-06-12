//
// Created by Cristi Ifrim on 3/16/2022.
//

#include "dog.h"

Dog::Dog(const std::string& name, const std::string& breed, int age, const std::string& photograph):
    name{name}, breed{breed}, age{age}, photograph{photograph}{}

std::string Dog::getName() const {
    return this->name;
}

std::string Dog::getBreed() const {
    return this->breed;
}

int Dog::getAge() const {
    return this->age;
}

std::string Dog::getPhotograph() const {
    return this->photograph;
}

void Dog::setAge(int age) {
    this->age = age;
}

void Dog::setName(const std::string& name) {
    this->name = name;
}

void Dog::setBreed(const std::string& breed) {
    this->breed = breed;
}

void Dog::setPhotograph(const std::string& photograph) {
    this->photograph = photograph;
}

