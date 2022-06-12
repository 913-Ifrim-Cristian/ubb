//
// Created by Cristi Ifrim on 3/16/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_DOG_H
#define A5_6_913_IFRIM_CRISTIAN_DOG_H

#include <string>
#include <iostream>


class Dog {
    private:
        std::string breed;
        std::string name;
        int age;
        std::string photograph;

    public:
        /*
         * Constructors
         */
        Dog(): breed{""}, name{""}, age{0}, photograph{""}{}
        Dog(const std::string& name, const std::string& breed, int age, const std::string& photograph);

        /*
         * Getters
         */

        std::string getBreed() const;
        std::string getName() const;
        int getAge() const;
        std::string getPhotograph() const;

        /*
         * Setters
         */
        void setBreed(const std::string& breed);
        void setName(const std::string& name);
        void setAge(int age);
        void setPhotograph(const std::string& photograph);

        /*
         * I/O operators
         */
        std::istream& read(std::istream& in);
        friend std::ostream& operator<<(std::ostream& out, const Dog& obj);
        friend std::istream& operator>>(std::istream& in, Dog& obj);


};


#endif //A5_6_913_IFRIM_CRISTIAN_DOG_H
