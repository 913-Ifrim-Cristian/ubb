//
// Created by Cristi Ifrim on 3/29/2022.
//

#include "utility.h"
#include <algorithm>
#include <iostream>
#include "exceptions.h"
#include <sstream>

std::string utility::toLower(std::string str) {
    /*
     * Returns a lower-case string from the original string
     */
    std::for_each(str.begin(), str.end(), [](char & c) {
        c = ::tolower(c);
    });
    return str;
}

int utility::readInteger() {
    /*
     * Safe reads an integer
     */
    std::string inputStr;
    int result;
    std::getline(std::cin, inputStr);

    try {
        result = std::stoi(inputStr);
        return result;
    }
    catch(std::exception&) {
        throw InputException("Invalid input!");
    }
}

int utility::readDouble() {
    /*
     * Safe reads a double
     */
    std::string inputStr;
    double result;
    std::getline(std::cin, inputStr);

    try {
        result = std::stod(inputStr);
        return result;
    }
    catch(std::exception&) {
        throw InputException("Invalid input!");
    }
}

std::vector<std::string> utility::tokenize(std::string str, char delimiter) {

    std::vector<std::string> result{};
    std::stringstream ss{str};
    std::string token{};

    while(getline(ss, token, delimiter)) {
        result.push_back(token);
    }

    return result;
}
