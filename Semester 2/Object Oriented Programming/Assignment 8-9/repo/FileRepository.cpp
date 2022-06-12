//
// Created by Cristi Ifrim on 4/17/2022.
//

#include "FileRepository.h"
#include <fstream>
#include <iostream>

void FileRepository::loadData() {
    std::ifstream f(this->path);
    while(!f.eof()) {
        Dog d;
        f >> d;
        if(!d.getName().empty())
            this->data.push_back(d);
    }
    f.close();
}

void FileRepository::saveData() {

    std::ofstream g(this->path);

    for(const auto& d: this->data) {
        g << d;
    }

    g.close();
}
