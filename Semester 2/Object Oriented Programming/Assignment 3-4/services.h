//
// Created by Cristi Ifrim on 3/4/2022.
//

#ifndef A3_4_913_IFRIM_CRISTIAN_SERVICES_H
#define A3_4_913_IFRIM_CRISTIAN_SERVICES_H

#include "repo.h"
#include "country.h"

#define ERROR_ELEM_NOT_FOUND 99
#define ERROR_NULLPTR_GENERATED 100
#define SUCCES_ADDITION 101
#define SUCCES_DELETION 102
#define SUCCES_UPDATE 103
#define ERROR_INVALID_POPULATION 104
#define ERROR_INVALID_NAME 105

typedef struct {
    int top;
    Vector* stack;
} History;

History* createHistory(); //Tested
void destroyHistory(History* h); //Tested
void addToHistory(History* h, Vector* v); //Tested
int addCountry(Vector* r, char* name, char* continent, double population); //Tested
int deleteCountry(Vector* r, char* name); //Tested
int migratePopulation(Vector* r, char* destCountry, char* srcCountry, double populationAmount);
int updateCountry(Vector* r, char* oldName, char* newName, char* continent, double population); //Tested
Vector* getCountriesMatchingString(Vector* r, char* str);
void sortByCompareFunction(Vector* v, int (*comparator)(Country*, Country*), char* order);
Vector* getCountriesMatchingContinent(Vector* r, char* str, double population);
Vector* getCountriesMatchingNameAndContinent(Vector* r);
char* lowerStr(char* str);

#endif //A3_4_913_IFRIM_CRISTIAN_SERVICES_H
