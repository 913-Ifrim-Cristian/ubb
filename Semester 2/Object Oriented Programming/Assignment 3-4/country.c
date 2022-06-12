//
// Created by Cristi Ifrim on 3/3/2022.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "country.h"

Country* createCountry(char* name, char* continent, double population) {
    /*
     * Creates a pointer to a Country element and returns it
     */
    if(name == NULL || continent == NULL) {
        return NULL;
    }

    Country* c = malloc(sizeof(Country));
    if(c == NULL) {
        return NULL;
    }

    c->name = malloc((strlen(name) + 1) * sizeof(char));
    if(c->name == NULL) {
        free(c);
        return NULL;
    }
    strcpy(c->name, name);

    c->continent = malloc((strlen(continent) + 1) * sizeof(char));
    if(c->continent == NULL) {
        free(c->name);
        free(c);
        return NULL;
    }
    strcpy(c->continent, continent);

    c->population = population;

    return c;
}

void destroyCountry(Country* c) {
    /*
     * Destroys a country and clears the memory
     */
    if(c == NULL) {
        return;
    }
    free(c->name);
    free(c->continent);
    free(c);
}

char* returnName(Country* c) {
    /*
     * Getter function for the name of a Country type structure
     */
    return c->name;
}

char* returnContinent(Country* c) {
    /*
     * Getter function for the continent of a Country type structure
     */
    return c->continent;
}

double returnPopulation(Country* c) {
    /*
     * Getter function for the population of a Country type structure
     */
    return c->population;
}

void setPopulation(Country* c, double amount) {
    /*
     * Setter function for the population of a country
     */
    c->population = amount;
}

int compareCountriesPopulation(Country* a, Country* b) {
    /*
     * Comparator function that returns 1 if population of a is greater than population of b
     */
    return a->population > b->population;
}

int compareCountriesName(Country* a, Country* b) {
    /*
     *  Comparator function that returns 1 if the names of the countries are in ascending order
     */
    return strcmp(returnName(a), returnName(b)) == 1;
}

Country* copyCountry(Country* c) {
    /*
     * This function does a deepcopy of a country and returns the copy
     */
    return createCountry(c->name, c->continent, c->population);
}

