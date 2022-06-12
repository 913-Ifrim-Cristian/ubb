//
// Created by Cristi Ifrim on 3/21/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_SERVICE_H
#define A5_6_913_IFRIM_CRISTIAN_SERVICE_H


#include "../repo/repository.h"
#include "../repo/AdoptionList.h"
#include "../domain/dog.h"
#include "validator.h"
#include <string>

#define UPDATE_BREED 99
#define UPDATE_NAME 100
#define UPDATE_PHOTOGRAPH 102

class AdminService {

    Repository& repo;
    Validator validator;

public:
    explicit AdminService(Repository& r);
    void add(const std::string&, const std::string&, int, const std::string&);
    void remove(const std::string&);
    void update(const std::string&, int, const std::string&);
    void update(const std::string&, int);
    Repository getRepo() const { return this->repo; }
};

class UserService {

    Repository& repo;
    AdoptionList* adoptionList;

public:
    explicit UserService(Repository& r): repo{r}, adoptionList{nullptr} {}
    void init(int type);
    std::vector<Dog> getDogList() { return this->repo.getData(); }
    std::vector<Dog> getDogListByFilter(const std::string&, int);
    const std::vector<Dog>& getAdoptionList() { return this->adoptionList->get(); }
    void adoptDog(const Dog&);
    void openAdoptionList();
};


#endif //A5_6_913_IFRIM_CRISTIAN_SERVICE_H
