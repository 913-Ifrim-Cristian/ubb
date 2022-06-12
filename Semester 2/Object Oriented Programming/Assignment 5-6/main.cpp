//
// Created by Cristi Ifrim on 3/17/2022.
//
#include <iostream>
#include "domain/dog.h"
#include "DynamicArray.h"
#include "tests/tests.h"
#include "ui/ui.h"
#include "services/service.h"
#include "repo/repository.h"

int main() {

    tests c;

    c.runTests();

    Repository repo;

    AdminService admin{repo};
    UserService user{repo};

    UI ui{admin, user};

    //ui.start();
    return 0;
}
