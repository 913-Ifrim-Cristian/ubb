//
// Created by Cristi Ifrim on 3/3/2022.
//

#ifndef A3_4_913_IFRIM_CRISTIAN_COUNTRY_H
#define A3_4_913_IFRIM_CRISTIAN_COUNTRY_H

typedef struct {
    char* name;
    char* continent;
    double population;
} Country;

Country* createCountry(char* name, char* continent, double population);
void destroyCountry(Country* c);
char* returnName(Country* c);
char* returnContinent(Country* c);
double returnPopulation(Country* c);
void setPopulation(Country* c, double amount);
int compareCountriesPopulation(Country* a, Country* b);
int compareCountriesName(Country* a, Country* b);
Country* copyCountry(Country* c);

#endif //A3_4_913_IFRIM_CRISTIAN_COUNTRY_H
