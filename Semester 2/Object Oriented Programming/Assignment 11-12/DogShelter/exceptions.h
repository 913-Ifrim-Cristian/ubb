//
// Created by Cristi Ifrim on 3/23/2022.
//

#pragma once

#include <string>
#include <exception>

#define VALUE_ERROR 1909
#define ELEM_ERROR 1910
#define INDEX_ERROR 1911
#define INPUT_ERROR 1912

class RepositoryException : public std::exception {
    std::string msg;
public:
    RepositoryException(const std::string& message="Repository error!"): msg{message} {}
    const char* what() const noexcept override;
};

class ValidationException : public std::exception {
    std::string msg;
public:
    ValidationException(const std::string& message="Validation error!"): msg{message} {}
    const char* what() const noexcept override;
};

class InputException : public std::exception {
    std::string msg;
public:
    InputException(const std::string& message="Invalid Input!"): msg{message} {}
    const char* what() const noexcept override;
};
