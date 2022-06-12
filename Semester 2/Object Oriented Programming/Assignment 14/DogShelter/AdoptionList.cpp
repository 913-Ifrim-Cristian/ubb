//
// Created by Cristi Ifrim on 4/18/2022.
//

#include "AdoptionList.h"
#include <fstream>
#include <Windows.h>
#include <shellapi.h>
#include "exceptions.h"
#include "utility.h"

void AdoptionList::adopt(const Dog &d) {
    this->data.push_back(d);
}

void AdoptionList::remove(const Dog& d)
{
    int i = 0;
    for (i = 0; i < data.size(); ++i)
        if (utility::toLower(data[i].getName()) == utility::toLower(d.getName()))
            break;
    if (i == data.size())
        throw RepositoryException(d.getName() + " is not in the adoption list!");
    data.erase(data.begin() + i);
}

std::vector<Dog> &AdoptionList::get() {
    return this->data;
}

Dog& AdoptionList::operator[](int index) {

    if (index < 0 || index >= this->data.size())
        throw RepositoryException("Array index out of bounds!");

    return this->data[index];
}

void AdoptionListHTML::save() {

    std::ofstream f(this->path);

    f << "<!DOCTYPE html>\n";
    f << "<html>\n";
    f << "<head>\n";
    f << "<title>Adoption List</title>\n";
    f << "</head>\n";
    f << "<body>\n";
    f << "<table border=\"1\">\n";
    f << "<tr>\n";
    f << "<td>Name</td>\n";
    f << " <td>Breed</td>\n";
    f << "<td>Age</td>\n";
    f << "<td>Photograph</td>\n";
    f << "</tr>\n";

    for(auto it: this->data) {
        f << "<tr>";
        f << "<td>" << it.getName() << "</td>\n";
        f << "<td>" << it.getBreed() << "</td>\n";
        f << "<td>" << it.getAge() << "</td>\n";
        f << "<td>" << "<a href = \"" << it.getPhotograph() << "\">Link</a>" << "</td>\n";
        f << "</tr>\n";
    }
    f << "</table>\n</body>\n</html>\n";
}

void AdoptionListHTML::open() {

    std::string command = "start ";
    system(command.append(this->path).c_str());
}

void AdoptionListCSV::save() {
    std::ofstream g(this->path);

    for(const auto& d: this->data) {
        g << d;
    }

    g.close();
}

void AdoptionListCSV::open() {
    ShellExecuteA(nullptr, nullptr, "notepad.exe", this->path.c_str(), nullptr, SW_SHOWMAXIMIZED);
}
