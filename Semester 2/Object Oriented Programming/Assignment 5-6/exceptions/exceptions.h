//
// Created by Cristi Ifrim on 3/23/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_EXCEPTIONS_H
#define A5_6_913_IFRIM_CRISTIAN_EXCEPTIONS_H

#include <string>

#define VALUE_ERROR 1909
#define ELEM_ERROR 1910
#define INDEX_ERROR 1911
#define INPUT_ERROR 1912

std::string errorMsg(int errorid);

#endif //A5_6_913_IFRIM_CRISTIAN_EXCEPTIONS_H
