//
// Created by Cristi Ifrim on 4/18/2022.
//

#pragma once
#include "Dog.h"
#include <string>
#include <vector>

class AdoptionList {
protected:
    std::vector<Dog> data;
    virtual void save() {}

public:
    virtual void adopt(const Dog&);
    virtual void remove(const Dog&);
    std::vector<Dog>& get();
    virtual Dog& operator[](int index);
    virtual void open() {}

};


class AdoptionListHTML : public AdoptionList {
    std::string path;
    void save() override;

public:
    AdoptionListHTML(const std::string& path): path{path} {}
    void adopt(const Dog& d) override { AdoptionList::adopt(d); this->save(); }
    void open() override;
    ~AdoptionListHTML() { this->save();}
};


class AdoptionListCSV : public AdoptionList {
    std::string path;
    void save() override;

public:
    AdoptionListCSV(const std::string& path): path{path} {}
    void adopt(const Dog& d) override { AdoptionList::adopt(d); this->save(); }
    void open() override;
    ~AdoptionListCSV() { this->save();}
};

