//
// Created by Cristi Ifrim on 4/17/2022.
//

#include "validator.h"
#include "exceptions.h"

void Validator::validateInput(const std::string &name, const std::string &breed, const std::string &url, int age) {
    std::string exception = "VALIDATION ERROR:\n";

    try {
        this->validateName(name);
    }
    catch(ValidationException& ve) {
        exception += ve.what();
        exception += "\n";
    }

    try {
        this->validateBreed(breed);
    }
    catch(ValidationException& ve) {
        exception += ve.what();
        exception += "\n";
    }

    try {
        this->validateAge(age);
    }
    catch(ValidationException& ve) {
        exception += ve.what();
        exception += "\n";
    }

    try {
        this->validateURL(url);
    }
    catch(ValidationException& ve) {
        exception += ve.what();
        exception += "\n";
    }

    if(exception != "VALIDATION ERROR:\n")
        throw ValidationException(exception);
}

void Validator::validateName(const std::string& name) {
    if(name.empty())
        throw ValidationException("Invalid name!");
}

void Validator::validateBreed(const std::string& breed) {
    if(breed.empty())
        throw ValidationException("Invalid breed!");
}

void Validator::validateAge(int age) {
    if(age < 0)
        throw ValidationException("Invalid age. Age cannot be a negative number!");
}

void Validator::validateURL(const std::string& url) {
    if(url.empty())
        throw ValidationException("Invalid url!");
}
