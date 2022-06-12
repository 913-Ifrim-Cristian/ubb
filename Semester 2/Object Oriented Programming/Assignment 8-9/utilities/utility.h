//
// Created by Cristi Ifrim on 3/29/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_UTILITY_H
#define A5_6_913_IFRIM_CRISTIAN_UTILITY_H

#include <string>
#include <vector>


namespace utility {
    std::string toLower(std::string);
    int readInteger();
    int readDouble();
    std::vector<std::string> tokenize(std::string str, char delimiter=' ');
}

#endif //A5_6_913_IFRIM_CRISTIAN_UTILITY_H
