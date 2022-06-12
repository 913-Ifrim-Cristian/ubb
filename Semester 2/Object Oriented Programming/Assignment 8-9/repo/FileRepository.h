//
// Created by Cristi Ifrim on 4/17/2022.
//

#ifndef A8_9_913_IFRIM_CRISTIAN_FILEREPOSITORY_H
#define A8_9_913_IFRIM_CRISTIAN_FILEREPOSITORY_H

#include "repository.h"
#include <string>

class FileRepository : public Repository {
    std::string path;

    virtual void loadData();
    virtual void saveData();

public:
    FileRepository(const std::string& path) : path{path} { this->loadData(); }

    void add(const Dog& d) override { Repository::add(d); this->saveData(); }
    void remove(const std::string& name) override { Repository::remove(name); this->saveData(); }

    ~FileRepository() override { this->saveData(); }
};


#endif //A8_9_913_IFRIM_CRISTIAN_FILEREPOSITORY_H
