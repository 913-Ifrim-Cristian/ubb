//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "ui.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printMenu() {
    cout << "1. Remove a bill\n2.Show all bills\n3.Show unpaid bills sorted by due date\n4. Calculate total of unpaid bills\n";
    cout << "5. Exit\n\n";
}

void UI::start() {

    cout << "Hello user, how may I help you?\n";
    while(true) {
        printMenu();
        cout << ">>> ";
        string option;
        getline(cin, option);

        if(option == "5")
            return;
        try {
            if (option == "1")
                this->remove();
            else if (option == "2")
                this->showBills();
            else if (option == "3")
                this->showUnpaidBills();
            else if (option == "4")
                this->showTotal();
            else
                cout << "Error: Invalid input!";
        }
        catch(char* str) {
            cout << "Oops! There was an error!\n";
            cout << str;
            cout << "\n";
        }
    }

}

void UI::remove() {
    string serial;
    getline(cin, serial);

    this->service.remove(serial);
    cout << "Bill with serial: " << serial << "succesfully removed!";
}

void UI::showBills() {
    std::vector<Bill> data = this->service.getList();
    for(auto it: data) {
        cout << "Bill ID: " << it.getSerial() << ", from company: " << it.getCompany() << ", due date: ";
        cout << it.getDateDay() << "." << it.getDateMonth() << "." << it.getDateYear() << ", is paid: " << it.getState();
        cout << ", sum: " << it.getSum() << "." << "\n";
    }
    cout << "\n";
}

void UI::showUnpaidBills() {
    std::vector<Bill> data = this->service.sortUnpaid();
    for(auto it: data) {
        cout << "Bill ID: " << it.getSerial() << ", from company: " << it.getCompany() << ", due date: ";
        cout << it.getDateDay() << "." << it.getDateMonth() << "." << it.getDateYear() << ", is paid: " << it.getState();
        cout << "\n";
    }
    cout << "\n";
}

void UI::showTotal() {
    double sum = this->service.getMoneyToPay();
    cout << "There is a total of " << sum << " left to pay!\n\n";
}
