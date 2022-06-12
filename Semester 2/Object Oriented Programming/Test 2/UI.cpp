//
// Created by Cristi Ifrim on 5/4/2022.
//

#include "UI.h"
#include <iostream>

void UI::printMenu() {
    std::cout << "---------------\n";
    std::cout << "1. Add dwelling\n2. Remove client\n3. Show clients and dwellings\n4. Save all clients to file\n5. Exit\n";
    std::cout << "---------------\n";
}

void UI::start() {
    while(true) {
        this->printMenu();
        std::cout << "Please select a choice: ";
        std::string option;
        std::getline(std::cin, option);


        if (option == "5") {
            std::cout << "Goodbye!\n\n";
            return;
        }
        try {
            if (option == "1")
                this->add();
            else if (option == "2")
                this->remove();
            else if (option == "3")
                this->show();
            else if (option == "4")
                this->save();
        }
        catch(std::exception& e) {
            std::cout << "ERROR: " << e.what() << "\n\n";
        }
    }


}

void UI::add() {
    std::cout << "Please enter the price of the dwelling: ";
    double price = this->readDouble();

    std::cout << "Please enter if the dwelling is proftable(true/false): ";
    std::string option;
    std::getline(std::cin, option);

    bool isProfitable = false;

    if(option == "true") {
        isProfitable = true;
    }
    else if(option == "false")
        isProfitable = false;
    else {
        std::cout << "Invalid option!";
        return;
    }
    Dwelling d = this->service.addDwelling(price, isProfitable);

    std::cout << "Dwelling added succesfully!";
    std::cout << "Clients interested in this dwelling:\n";
    for(auto it: this->service.getInterestedClients(d)) {
        std::cout << it->toString();
    }
    std::cout << "\n\n";
}

void UI::remove() {
    std::string name;
    std::cout << "Please enter the name of the client: ";
    std::getline(std::cin, name);
    int result = this->service.removeClient(name);
    if(result == -1)
        std::cout << "Client doesn't exit!\n\n";
    else
        std::cout << "Client removed succesfully!\n\n";
}

void UI::show() {
    std::cout << "Clients:\n";
    for(auto it: this->service.getClients())
        std::cout << it->toString();
    std::cout << "Dwellings:\n";
    std::string profit = "yes";
    for(auto it: this->service.getDwellings()) {
        if (!it.getProfitable())
            profit = "no";
        std::cout << it.getPrice() << " " << profit << '\n';
    }

}


void UI::save() {
    std::string filename = "C:\\Users\\Cristi Ifrim\\Documents\\GitHub\\t2-913-Ifrim-Cristian-1\\clients.txt";
    this->service.writeToFile(filename);
    std::cout << "Client saved succesfully!\n\n";
}

double UI::readDouble() {
    std::string doubleStr;
    double result;

    std::getline(std::cin, doubleStr);

    try {
        result = std::stod(doubleStr);
        return result;
    } catch(std::exception&) {
        throw std::exception();
    }
}
