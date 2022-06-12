//
// Created by Cristi Ifrim on 3/4/2022.
//
#include "services.h"
#include <string.h>
#include <stdlib.h>

History* createHistory() {
    /*
     * Creates a pointer to a history structure, initializes it and returns it
     */
    History* h = malloc(sizeof(History));
    h->top = -1;
    h->stack = createVector(15, &destroyVector, &copyVector);
    return h;
}

void destroyHistory(History* h) {
    /*
     * Destroys and de-allocates the pointer of a history structure
     */
    if(h == NULL)
        return;

    destroyVector(h->stack);
    free(h);
}

void addToHistory(History* h, Vector* v) {

    /*
     * Adds a vector to a history structure, used for undo/redo functionality
     */

    int stackSize = vectorSize(h->stack);

    for(int i = h->top + 1; i < stackSize; ++i)
        destroyVector(getItem(h->stack, i));

    h->stack->size = h->top + 1;
    h->top++;
    addToVector(h->stack, v);
}

char* lowerStr(char* str) {
    /*
     * Returns a string given as a parameter to it's lowercase form
     */

    char* lowStr = malloc(sizeof(char) * (strlen(str) + 1));
    strcpy(lowStr, str);
    for(int i = 0; i < strlen(lowStr); ++i)
        if(lowStr[i] >= 'A' && lowStr[i] <= 'Z')
            lowStr[i] += 32;
    return lowStr;
}

int addCountry(Vector* r, char* name, char* continent, double population) {
    /*
     * Adds a country to a vector and returns different errors if the operation was not successfully
     */
    const char* continentsList[5] = {"europe", "africa", "asia", "australia", "america"};
    if(name == NULL)
        return ERROR_ELEM_NOT_FOUND;
    if(continent == NULL)
        return ERROR_INVALID_NAME;
    if(population == 0)
        return ERROR_INVALID_POPULATION;

    int index = searchElement(r, name);
    if(index != -1)
        return ERROR_ELEM_NOT_FOUND;

    int found = 0;
    char* loweredContinent = lowerStr(continent);
    for(int i = 0; i < 5 && !found; ++i)
        if(strcmp(loweredContinent, continentsList[i]) == 0)
            found = 1;

    free(loweredContinent);

    if(found == 0)
        return ERROR_INVALID_NAME;

    Country* c = createCountry(name, continent, population);
    if(c == NULL)
        return ERROR_NULLPTR_GENERATED;

    addToVector(r, c);
    return SUCCES_ADDITION;
}

int deleteCountry(Vector* r, char* name) {
    /*
     * Deletes a country from a vector, returns an error if the element was not found
     */
    int index = searchElement(r, name);
    if(index == -1)
        return ERROR_ELEM_NOT_FOUND;

    deleteElement(r, index);
    return SUCCES_DELETION;
}

int updateCountry(Vector* r, char* name, char* newName, char* continent, double population) {
    /*
     * Updates a country from a vector structure
     * It updates the name, the continent or the population of a country
     * In case of errors, returns an error code
     */
    int destIndex = searchElement(r, name);
    //name[0] -= 32;
    if(destIndex == -1)
        return ERROR_ELEM_NOT_FOUND;
    if(newName == NULL)
        return ERROR_INVALID_NAME;
    if(continent == NULL)
        return ERROR_INVALID_NAME;

    Country *c, *d;

    if(strcmp(newName, "default") != 0) {
        c = createCountry(newName, returnContinent(getItem(r, destIndex)),
                          returnPopulation(getItem(r, destIndex)));

        if(c == NULL)
            return ERROR_NULLPTR_GENERATED;

        d = getItem(r, destIndex);
        r->data[destIndex] = c;
        destroyCountry(d);
        return SUCCES_UPDATE;
    }

    if(strcmp(continent, "default") != 0) {
        c = createCountry(returnName(r->data[destIndex]), continent, returnPopulation(r->data[destIndex]));
        if(c == NULL)
            return ERROR_NULLPTR_GENERATED;

        const char* continentsList[5] = {"europe", "africa", "asia", "australia", "america"};
        int found = 0;
        char *loweredContinent = lowerStr(continent);
        for(int i = 0; i < 5 && !found; ++i)
            if(strcmp(loweredContinent, continentsList[i]) == 0)
                found = 1;

        free(loweredContinent);

        if(found == 0) {
            destroyCountry(c);
            return ERROR_INVALID_NAME;
        }

        d = r->data[destIndex];
        r->data[destIndex] = c;
        destroyCountry(d);
        return SUCCES_UPDATE;
    }

    if(population == 0)
        return ERROR_INVALID_POPULATION;

    c = createCountry(returnName(r->data[destIndex]), returnContinent(r->data[destIndex]), population);
    if(c == NULL)
        return ERROR_NULLPTR_GENERATED;

    d = r->data[destIndex];
    r->data[destIndex] = c;
    destroyCountry(d);
    return SUCCES_UPDATE;
}

int migratePopulation(Vector* r, char* destCountry, char* srcCountry, double populationAmount) {
    /*
     * This function migrates a number of people from a country to another
     * If not successfully, returns an error code
     */
    if(populationAmount == 0)
        return ERROR_INVALID_POPULATION;

    int destIndex = searchElement(r, destCountry);
    if(destIndex == -1)
        return ERROR_ELEM_NOT_FOUND;

    int srcIndex = searchElement(r, srcCountry);
    if(srcIndex == -1)
        return ERROR_ELEM_NOT_FOUND;

    if(returnPopulation(r->data[srcIndex]) - populationAmount <= 0)
        return ERROR_INVALID_POPULATION;

    setPopulation(r->data[destIndex], returnPopulation(r->data[destIndex]) + populationAmount);
    setPopulation(r->data[srcIndex], returnPopulation(r->data[srcIndex]) - populationAmount);

    return SUCCES_UPDATE;
}

Vector* getCountriesMatchingString(Vector* r, char* str) {

    /*
     * This function creates and returns a vector with countries that contain in their name a given string
     */

    Vector* c;
    if(str == NULL)
        c = copyVector(r);
    else {
        char* loweredStr = lowerStr(str);
        c = createVector(r->size, &destroyCountry, &copyCountry);
        for(int i = 0; i < r->size; ++i) {
            char* loweredName = lowerStr(returnName(getItem(r, i)));
            if(strstr(loweredName, loweredStr) != NULL)
                addToVector(c, copyCountry(r->data[i]));
            free(loweredName);
        }
        free(loweredStr);
    }

    return c;
}

Vector* getCountriesMatchingNameAndContinent(Vector* r) {

    /*
     * This function creates and returns a vector with countries that begin with the same letter as their continent
     */

    Vector* c;
    c = createVector(r->size, &destroyCountry, &copyCountry);
    for(int i = 0; i < r->size; ++i) {
        char* loweredName = lowerStr(returnName(getItem(r, i)));
        char* loweredContinent = lowerStr(returnContinent(getItem(r, i)));
        if(loweredName[0] == loweredContinent[0])
            addToVector(c, copyCountry(r->data[i]));
        free(loweredName);
        free(loweredContinent);

    }

    return c;
}

void sortByCompareFunction(Vector* v, int (*comparator)(Country*, Country*), char* order) {
    /*
     * This function sorts a vector following the value of a comparator function
     */
    int ordr = 1;
    if(strcmp(order, "descending") == 0)
        ordr = 0;

    int vSize = vectorSize(v);
    for(int i = 0; i < vSize - 1; ++i)
        for(int j = i; j < vSize; ++j)
            if(comparator(getItem(v, i), getItem(v, j)) == ordr) {
                Country* aux = getItem(v, i);
                v->data[i] = getItem(v, j);
                v->data[j] = aux;
            }
}

Vector* getCountriesMatchingContinent(Vector* r, char* str, double population) {

    /*
     * This function creates and returns a list of countries that are on a given continent and their population is
     * greater than a given population.
     */

    Vector* c;
    char* loweredStr = (str == NULL)?NULL:lowerStr(str);

    c = createVector(r->size, &destroyCountry, &copyCountry);
    for(int i = 0; i < r->size; ++i) {
        char* loweredContinent = lowerStr(returnContinent(getItem(r, i)));
        if(str == NULL || strstr(loweredContinent, loweredStr) != NULL)
            if(returnPopulation(r->data[i]) > population)
                addToVector(c, copyCountry(r->data[i]));
        free(loweredContinent);
    }
    free(loweredStr);

    return c;
}
