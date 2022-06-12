//
// Created by Cristi Ifrim on 3/17/2022.
//

#pragma once

#include "dog.h"
#include "repository.h"
#include "service.h"
#include "exceptions.h"


class tests {

public:
    void domainTests();
    void repositoryTests();
    void serviceAdminTests();
    void serviceUserTests();
    void comparatorTests();
    void runTests();

};
