//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "utility.h"
#include <algorithm>

const std::string utility::toLower(std::string str) {
    /*
     * Returns a lower-case string from the original string
     */
    std::for_each(str.begin(), str.end(), [](char & c) {
        c = ::tolower(c);
    });
    return str;
}
