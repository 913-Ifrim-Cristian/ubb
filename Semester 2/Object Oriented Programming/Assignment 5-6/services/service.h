//
// Created by Cristi Ifrim on 3/21/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_SERVICE_H
#define A5_6_913_IFRIM_CRISTIAN_SERVICE_H


#include "../repo/repository.h"
#include "../domain/dog.h"
#include <string>

#define UPDATE_BREED 99
#define UPDATE_NAME 100
#define UPDATE_AGE 101
#define UPDATE_PHOTOGRAPH 102

class AdminService {

    Repository& repo;

public:
    AdminService(Repository& r);
    void add(const std::string&, const std::string&, int, const std::string&);
    void remove(const std::string&);
    void update(const std::string&, int, const std::string&);
    void update(const std::string&, int);
    Repository getRepo() const { return this->repo; }
};

class UserService {

    Repository& repo;
    DynamicArray<Dog> adoptionList;

public:
    UserService(Repository& r): repo{r} {}
    DynamicArray<Dog> getDogList() { return this->repo.getData(); }
    DynamicArray<Dog> getDogListByFilter(const std::string&, int);
    const DynamicArray<Dog>& getAdoptionList() { return this->adoptionList; }
    void adoptDog(const Dog&);
};


#endif //A5_6_913_IFRIM_CRISTIAN_SERVICE_H
