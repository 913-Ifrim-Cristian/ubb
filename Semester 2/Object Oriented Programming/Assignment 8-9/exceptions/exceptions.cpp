//
// Created by Cristi Ifrim on 3/23/2022.
//

#include "exceptions.h"

const char *RepositoryException::what() const noexcept {
    return this->msg.c_str();
}

const char *ValidationException::what() const noexcept {
    return this->msg.c_str();
}

const char *InputException::what() const noexcept {
    return this->msg.c_str();
}
