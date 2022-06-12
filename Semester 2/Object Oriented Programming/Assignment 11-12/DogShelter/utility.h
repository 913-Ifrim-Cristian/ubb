//
// Created by Cristi Ifrim on 3/29/2022.
//

#pragma once
#include <string>
#include <vector>


namespace utility {
    std::string toLower(std::string);
    int readInteger();
    int readDouble();
    std::vector<std::string> tokenize(std::string str, char delimiter=' ');
}
