//
// Created by Cristi Ifrim on 4/18/2022.
//

#ifndef A8_9_913_IFRIM_CRISTIAN_ADOPTIONLIST_H
#define A8_9_913_IFRIM_CRISTIAN_ADOPTIONLIST_H

#include "../domain/dog.h"
#include <string>
#include <vector>

class AdoptionList {
protected:
    std::vector<Dog> data;
    virtual void save() {}

public:
    virtual void adopt(const Dog&);
    const std::vector<Dog>& get();
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


#endif //A8_9_913_IFRIM_CRISTIAN_ADOPTIONLIST_H
