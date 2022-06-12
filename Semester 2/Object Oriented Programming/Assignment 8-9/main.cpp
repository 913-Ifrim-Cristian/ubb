//
// Created by Cristi Ifrim on 3/17/2022.
//
#include "domain/dog.h"
#include "tests/tests.h"
#include "ui/ui.h"
#include "services/service.h"
#include "repo/FileRepository.h"


int main() {

    //tests c;

    //c.runTests();

    FileRepository repo{"../repo.txt"};

    AdminService admin{repo};
    UserService user{repo};

    UI ui{admin, user};

    ui.start();
    return 0;
}
