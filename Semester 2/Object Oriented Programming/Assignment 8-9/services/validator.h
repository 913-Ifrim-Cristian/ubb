//
// Created by Cristi Ifrim on 4/17/2022.
//

#ifndef A8_9_913_IFRIM_CRISTIAN_VALIDATOR_H
#define A8_9_913_IFRIM_CRISTIAN_VALIDATOR_H

#include <string>

class Validator {

private:

    void validateName(const std::string& name);
    void validateBreed(const std::string& breed);
    void validateAge(int age);
    void validateURL(const std::string& url);

public:

    void validateInput(const std::string& name, const std::string& breed, const std::string& url, int age);
};


#endif //A8_9_913_IFRIM_CRISTIAN_VALIDATOR_H
