//
// Created by Cristi Ifrim on 3/17/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_TESTS_H
#define A5_6_913_IFRIM_CRISTIAN_TESTS_H

#include "../domain/dog.h"
#include "../array/DynamicArray.h"
#include "../repo/repository.h"
#include "../services/service.h"
#include "../exceptions/exceptions.h"


class tests {

public:
    void domainTests();
    void dynamicArrayTests();
    void repositoryTests();
    void serviceAdminTests();
    void serviceUserTests();
    void exceptionsTests();
    void runTests();

};


#endif //A5_6_913_IFRIM_CRISTIAN_TESTS_H
