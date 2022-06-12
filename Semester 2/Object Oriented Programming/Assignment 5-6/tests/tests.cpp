//
// Created by Cristi Ifrim on 3/17/2022.
//

#include "tests.h"
#include <cassert>
#include <iostream>

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

void tests::dynamicArrayTests() {

    bool isException = false;

    DynamicArray<Dog> vector{1};

    assert(vector.isEmpty());
    assert(!vector.isFull());

    Dog caine = Dog{"Lucky", "Caucasian", 1, "url"};
    //vector.add(caine);
    vector = vector + caine;

    assert(!vector.isEmpty());
    assert(vector.isFull());
    assert(vector.getSize() == 1);

    assert(vector[0].getName() == "Lucky");
    assert(vector[0].getPhotograph() == "url");
    assert(vector[0].getAge() == 1);
    assert(vector[0].getBreed() == "Caucasian");

    Dog animal{"Max", "Unknown", 7, "link"};
    vector.add(animal);

    assert(!vector.isEmpty());
    assert(!vector.isFull());
    assert(vector.getSize() == 2);

    assert(vector[1].getName() == "Max");
    assert(vector[1].getPhotograph() == "link");
    assert(vector[1].getAge() == 7);
    assert(vector[1].getBreed() == "Unknown");

    vector.remove(0);
    assert(!vector.isEmpty());
    assert(!vector.isFull());
    assert(vector.getSize() == 1);

    assert(vector[0].getName() == "Max");
    assert(vector[0].getPhotograph() == "link");
    assert(vector[0].getAge() == 7);
    assert(vector[0].getBreed() == "Unknown");

    try {
        vector.remove(-1);
    }
    catch(int) {
        isException = true;
    }

    assert(isException == true);

    isException = false;

    try {
        vector.remove(3);
    }
    catch(int) {
        isException = true;
    }

    assert(isException == true);

    DynamicArray<std::string> vct;
    assert(vct.isEmpty());
    assert(!vct.isFull());
    assert(vct.getSize() == 0);

    vct.add("test123");

    assert(!vct.isEmpty());
    assert(!vct.isFull());
    assert(vct.getSize() == 1);

    assert(vct[0] == "test123");

    DynamicArray<int> v2{3};
    v2.add(5);

    assert(v2[0] == 5);

    for(int i = 0; i < 10; ++i)
        v2.add(i);

    DynamicArray<int>test{v2};

    assert(test[0] == 5);
    for(int i = 0; i < 10; ++i)
        assert(test[i+1] == i);

    v2.add(125);
    assert(v2[11] == 125);

    v2 + 69;
    assert(v2[12] == 69);

    72 + v2;
    assert(v2[13] == 72);

    v2 = v2 + 25;
    assert(v2[14] == 25);

    v2 = 26 + v2;
    assert(v2[15] == 26);

    isException = false;
    try {
        assert(test[11] == 125);
    }
    catch(int) {
        isException = true;
    }
    assert(isException == true);



    DynamicArray<Dog> testing{vector};

    for(int i = 0; i < 5; ++i)
        testing.add(Dog{"Lucky", "Caucasian", 1, "url"});

    assert(testing.getSize() == 6);

    vector = testing;

    assert(vector.getSize() == 6);
    for(int i = 0; i < 5; ++i)
        assert(vector[i+1].getName() == "Lucky");

    assert(&(vector=vector) == &vector);


    std::cout << "Dynamic Array tests passed successfully.\n";

}

void tests::repositoryTests() {
    Repository repo;
    bool isException = false;

    assert(repo.getSize() == 0);
    try {
        repo[0].getName();
    }
    catch(int) {
        isException = true;
    }

    assert(isException == true);

    assert(repo.search("Max") == -1);

    isException = false;
    try {
        repo.remove("Lucky");
    }
    catch(int) {
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
    catch(int) {
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
    catch(int) {
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
    catch(int) {
        isException = true;
    }

    assert(isException == true);
    isException = false;

    try {
        admin.update("Lucky", 5);
    }
    catch(int) {
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
    catch(int) {
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
    catch(int) {
        isException = true;
    }

    assert(isException == true);



    std::cout << "Admin service tests passed successfully!\n";
}

void tests::serviceUserTests() {
    Repository repo;

    AdminService admin{repo};
    UserService user{repo};

    DynamicArray<Dog> dogList = user.getDogList();
    assert(dogList.getSize() == 10);
    assert(dogList[0].getName() == "Lucki");
    assert(dogList[1].getName() == "Mex");
    assert(dogList[2].getName() == "Rex");
    assert(dogList[9].getName() == "Ursu");

    user.adoptDog(dogList[0]);
    admin.remove(dogList[0].getName());
    assert(user.getDogList().getSize() == 9);

    assert(user.getAdoptionList()[0].getName() == "Lucki");
    assert(user.getAdoptionList()[0].getBreed() == "Caucasian");

    dogList = user.getDogListByFilter("", 10);

    assert(dogList.getSize() == 9);
    assert(dogList[0].getName() == "Ursu");
    assert(dogList[1].getName() == "Mex");
    assert(dogList[8].getName() == "Relu");

    dogList = user.getDogListByFilter("Caucasian", 4);
    assert(dogList.getSize() == 0);

    dogList = user.getDogListByFilter("Pug", 0);
    assert(dogList.getSize() == 0);

    dogList = user.getDogListByFilter("Pug", 4);
    assert(dogList.getSize() == 1);

    user.adoptDog(dogList[0]);

    assert(user.getAdoptionList().getSize() == 2);

    DynamicArray<Dog> newList = user.getDogListByFilter("", 0);
    assert(newList.getSize() == 0);

    newList = user.getDogListByFilter("asdas", 10);
    assert(newList.getSize() == 0);

    assert(user.getDogListByFilter("", 0).getSize() == 0);

    std::cout << "User service tests passed successfully!\n";



}

void tests::exceptionsTests() {

    assert(errorMsg(VALUE_ERROR) == "ERROR: The element is already in the database!");
    assert(errorMsg(ELEM_ERROR) == "ERROR: The element is not in the database!");
    assert(errorMsg(INDEX_ERROR) == "ERROR: Array index out of bounds!");
    assert(errorMsg(INPUT_ERROR) == "ERROR: Invalid input!");

    assert(errorMsg(2) == "");

    std::cout << "Exception tests passed successfully!\n";

}

void tests::runTests() {
    this->domainTests();
    this->dynamicArrayTests();
    this->repositoryTests();
    this->serviceAdminTests();
    this->serviceUserTests();
    this->exceptionsTests();
}

