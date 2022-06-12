//
// Created by Cristi Ifrim on 3/17/2022.
//

#include "tests.h"
#include <cassert>
#include <iostream>
#include "comparator.h"
#include <memory>

void tests::domainTests() {
    Dog caine{"Lucky", "Caucazian", 1, "url"};

    assert(caine.getName() == "Lucky");
    assert(caine.getAge() == 1);
    assert(caine.getBreed() == "Caucazian");
    assert(caine.getPhotograph() == "url");

    caine.setAge(10);
    caine.setBreed("German");
    caine.setName("Max");
    caine.setPhotograph("link");

    assert(caine.getName() == "Max");
    assert(caine.getAge() == 10);
    assert(caine.getBreed() == "German");
    assert(caine.getPhotograph() == "link");

    std::cout << "Domain tests passed successfully!\n";
}

void tests::repositoryTests() {
    Repository repo;
    bool isException = false;

    assert(repo.getSize() == 0);
    try {
        repo[0].getName();
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);

    assert(repo.search("Max") == -1);

    isException = false;
    try {
        repo.remove("Lucky");
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);
    isException = false;

    Dog catel{"Max", "Unknown", 6, "url"};
    repo.add(catel);

    assert(repo.getSize() == 1);
    assert(repo[0].getName() == "Max");
    assert(repo.search("Max") == 0);

    try {
        repo.add(catel);
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);

    repo.remove("Max");
    assert(repo.getSize() == 0);
    assert(repo.search("Max") == -1);
    isException = false;

    try {
        repo[0].getName();
    }
    catch(...) {
        isException = true;
    }
    assert(isException == true);

    std::cout << "Repository tests passed successfully!\n";

}

void tests::serviceAdminTests() {
    Repository repo;

    AdminService admin{repo};

    bool isException = false;

    assert(admin.getRepo().getSize() == 10);

    admin.add("Lucky", "Caucasian", 1, "URL");
    assert(admin.getRepo()[10].getName() == "Lucky");
    assert(admin.getRepo()[10].getBreed() == "Caucasian");
    assert(admin.getRepo()[10].getAge() == 1);
    assert(admin.getRepo()[10].getPhotograph() == "URL");
    assert(admin.getRepo().getSize() == 11);

    admin.update("Lucky", 4);
    assert(admin.getRepo()[10].getAge() == 4);

    admin.update("Lucky", UPDATE_NAME, "Max");
    assert(admin.getRepo().search("Lucky") == -1);
    assert(admin.getRepo()[10].getName() == "Max");

    try {
        admin.update("Lucky", UPDATE_BREED, "Unknown");
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);
    isException = false;

    try {
        admin.update("Lucky", 5);
    }
    catch(...) {
        isException = true;
    }

    isException = false;
    try {
        admin.update("Max", -1);
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);

    admin.update("Max", UPDATE_BREED, "Unknown");
    assert(admin.getRepo()[10].getBreed() == "Unknown");

    admin.update("Max", UPDATE_PHOTOGRAPH, "LINK");
    assert(admin.getRepo()[10].getPhotograph() == "LINK");

    admin.update("Max", 2002, "URLS");

    assert(admin.getRepo()[10].getName() == "Max");
    assert(admin.getRepo()[10].getBreed() == "Unknown");
    assert(admin.getRepo()[10].getAge() == 4);
    assert(admin.getRepo()[10].getPhotograph() == "LINK");

    isException = false;

    try {
        admin.remove("Lucky");
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);

    admin.remove("Max");
    assert(admin.getRepo().search("Max") == -1);
    assert(admin.getRepo().getSize() == 10);

    isException = false;

    try {
        admin.getRepo()[10].setName("Max");
    }
    catch(...) {
        isException = true;
    }

    assert(isException == true);



    std::cout << "Admin service tests passed successfully!\n";
}

void tests::serviceUserTests() {
    Repository repo;

    AdminService admin{repo};
    UserService user{repo};

    std::vector<Dog> dogList = user.getDogList();
    assert(dogList.size() == 10);
    assert(dogList[0].getName() == "Lucki");
    assert(dogList[1].getName() == "Mex");
    assert(dogList[2].getName() == "Rex");
    assert(dogList[9].getName() == "Ursu");

    user.adoptDog(dogList[0]);
    admin.remove(dogList[0].getName());
    assert(user.getDogList().size() == 9);

    assert(user.getAdoptionList()[0].getName() == "Lucki");
    assert(user.getAdoptionList()[0].getBreed() == "Caucasian");

    dogList = user.getDogListByFilter("", 10);

    assert(dogList.size() == 9);
    assert(dogList[0].getName() == "Mex");
    assert(dogList[1].getName() == "Rex");
    assert(dogList[8].getName() == "Ursu");

    dogList = user.getDogListByFilter("Caucasian", 4);
    assert(dogList.empty());

    dogList = user.getDogListByFilter("Pug", 0);
    assert(dogList.empty());

    dogList = user.getDogListByFilter("Pug", 4);
    assert(dogList.size() == 1);

    user.adoptDog(dogList[0]);

    assert(user.getAdoptionList().size() == 2);

    std::vector<Dog> newList = user.getDogListByFilter("", 0);
    assert(newList.empty());

    newList = user.getDogListByFilter("asdas", 10);
    assert(newList.empty());

    assert(user.getDogListByFilter("", 0).empty());

    std::cout << "User service tests passed successfully!\n";



}

void tests::runTests() {
    this->domainTests();
    this->repositoryTests();
    //this->serviceAdminTests();
    //this->serviceUserTests();
    this->comparatorTests();
}

void tests::comparatorTests() {
    std::vector<Dog> v;
    v.emplace_back("Lucky", "Caucasian", 2, "url");
    v.emplace_back("Max", "Caucasian", 1, "url");
    v.emplace_back("Rex", "Caucasian", 5, "url");
    v.emplace_back("Martin", "Caucasian", 9, "url");
    v.emplace_back("Anne", "Caucasian", 3, "url");

    std::unique_ptr<Comparator<Dog>> c = std::make_unique<ComparatorAscendingByName>();
    sort(v, std::move(c));

    assert(v[0].getName() == "Anne");
    assert(v[1].getName() == "Lucky");
    assert(v[2].getName() == "Martin");
    assert(v[3].getName() == "Max");
    assert(v[4].getName() == "Rex");

    std::unique_ptr<Comparator<Dog>> a = std::make_unique<ComparatorDescendingByAge>();
    sort(v, std::move(a));

    assert(v[0].getName() == "Martin");
    assert(v[1].getName() == "Rex");
    assert(v[2].getName() == "Anne");
    assert(v[3].getName() == "Lucky");
    assert(v[4].getName() == "Max");

    std::cout << "Comparator tests passed successfully!\n";


}

