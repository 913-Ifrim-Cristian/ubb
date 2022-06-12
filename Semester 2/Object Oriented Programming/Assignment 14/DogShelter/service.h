//
// Created by Cristi Ifrim on 3/21/2022.
//

#pragma once
#include "repository.h"
#include "AdoptionList.h"
#include "Dog.h"
#include "validator.h"
#include <string>
#include "Action.h"
#include <memory>

#define UPDATE_BREED 99
#define UPDATE_NAME 100
#define UPDATE_PHOTOGRAPH 102

class AdminService {

    Repository& repo;
    Validator validator;
    std::vector<std::unique_ptr<Action>> actions;
    int whereOnStack;

public:
    explicit AdminService(Repository& r);
    void add(const std::string&, const std::string&, int, const std::string&);
    void remove(const std::string&);
    void update(const std::string&, int, const std::string&);
    void update(const std::string&, int);
    Repository getRepo() const { return this->repo; }
    void cascadeUpdate(const std::string& name, std::vector<std::string> args, int age = -1);
    void undo();
    void redo();
};

class UserService {

    Repository& repo;
    AdoptionList* adoptionList;
    std::vector<std::unique_ptr<Action>> actions;
    int whereOnStack;

public:
    explicit UserService(Repository& r) : repo{ r }, adoptionList{ nullptr }, whereOnStack{ -1 } {}
    void init(int type);
    std::vector<Dog> getDogList() { return this->repo.getData(); }
    std::vector<Dog> getDogListByFilter(const std::string&, int);
    std::vector<Dog>& getAdoptionList() { return this->adoptionList->get(); }
    AdoptionList* getAdoption() { return this->adoptionList; }
    void adoptDog(Dog&);
    void openAdoptionList();
    void undo();
    void redo();

};
