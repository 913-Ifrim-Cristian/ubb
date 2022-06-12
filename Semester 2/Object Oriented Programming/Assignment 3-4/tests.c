//
// Created by Cristi Ifrim on 3/8/2022.
//

#include "tests.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


void testCountry() {
    Country* c = createCountry("Romania", "Europe", 12.7);

    assert(strcmp(returnName(c), "Romania") == 0);
    assert(strcmp(returnContinent(c), "Europe") == 0);
    assert(returnPopulation(c) - 12.7 == 0);

    setPopulation(c, 14.7);
    assert(returnPopulation(c) - 14.7 == 0);

    Country* b = createCountry(NULL, "Europe", 0);
    assert(b == NULL);

    b = createCountry("England", NULL, 0);
    assert(b == NULL);

    b = createCountry("England", "America", 66.3);

    assert(strcmp(returnName(b), "England") == 0);
    assert(strcmp(returnContinent(b), "America") == 0);
    assert(returnPopulation(b) - 66.3 == 0);

    assert(compareCountriesPopulation(c, b) == 0);
    assert(compareCountriesName(c, b) == 1);

    Country* copy = copyCountry(c);
    assert(strcmp(returnName(c), returnName(copy)) == 0 && (copy != c) && (returnName(c) != returnName(copy)));
    assert(strcmp(returnContinent(c), returnContinent(copy)) == 0 && copy != c && returnContinent(c) != returnContinent(copy));
    assert(returnPopulation(c) - returnPopulation(copy) == 0 && copy != c);

    destroyCountry(c);
    destroyCountry(b);
    destroyCountry(copy);

    printf("Country tests passed succesfully!\n");
}

void testVector() {
    Vector* v = createVector(1, &destroyCountry, &copyCountry);

    assert(v->size == 0);
    assert(v->capacity == 1);

    Country* c = createCountry("Romania", "Europe", 12.7);

    addToVector(v, c);

    destroyVector(NULL);
    assert(copyVector(NULL) == NULL);

    assert(returnPopulation(getItem(v, 0)) == 12.7);
    assert(strcmp(returnContinent(getItem(v, 0)), "Europe") == 0);
    assert(strcmp(returnName(getItem(v, 0)), "Romania") == 0);

    assert(vectorSize(v) == 1);
    assert(v->capacity == 1);

    c = createCountry("Canada", "North America", 100.2);

    assert(c != NULL);

    addToVector(v, c);

    assert(getItem(v, -1) == NULL);
    assert(getItem(v, 20) == NULL);

    assert(returnPopulation(getItem(v, 1)) == 100.2);
    assert(strcmp(returnContinent(getItem(v, 1)), "North America") == 0);
    assert(strcmp(returnName(getItem(v, 1)), "Canada") == 0);

    assert(vectorSize(v) == 2);
    assert(v->capacity == 11);

    resizeVector(v);
    assert(vectorSize(v) == 2);
    assert(v->capacity == 21);

    assert(getItem(v, 1) == c);

    Vector* copy = copyVector(v);

    assert(getItem(v, 0) != getItem(copy, 0) && strcmp(returnName(getItem(v, 0)), returnName(getItem(copy, 0))) == 0);
    assert(getItem(v, 0) != getItem(copy, 0) && strcmp(returnContinent(getItem(v, 0)), returnContinent(getItem(copy, 0))) == 0);
    assert(getItem(v, 0) != getItem(copy, 0) && returnPopulation(getItem(v, 0)) - returnPopulation(getItem(copy, 0)) == 0);


    destroyVector(v);
    destroyVector(copy);
    printf("Vector tests passed successfully!\n");

}

void testRepo() {
    Vector* v = createVector(20, &destroyCountry, &copyCountry);

    deleteElement(v, 0);
    assert(vectorSize(v) == 0);

    initRepo(v);

    assert(strcmp(returnName(getItem(v, 0)), "Romania") == 0);
    assert(strcmp(returnContinent(getItem(v, 8)), "America") == 0);
    assert(returnPopulation(getItem(v, 9)) == 45.195);

    assert(searchElement(v, "Nothing") == -1);
    assert(searchElement(v, "France") == 7);

    deleteElement(v, 1);

    assert(strcmp(returnName(getItem(v, 1)), "Malta") == 0);
    assert(strcmp(returnContinent(getItem(v, 1)), "Europe") == 0);
    assert(returnPopulation(getItem(v, 1)) == 0.441);

    destroyVector(v);
    printf("Repo tests succesfully passed!\n");

}

void testServices() {
    History* h = createHistory();
    Vector* v = createVector(10, &destroyCountry, &copyCountry);

    assert(h->top == -1);

    int result = addCountry(v, "Romania", "Europe", 12.7);
    addToHistory(h, copyVector(v));
    assert(result == SUCCES_ADDITION);
    assert(returnPopulation(getItem(getItem(h->stack, 0), 0)) == 12.7);
    assert(strcmp(returnName(getItem(getItem(h->stack, 0), 0)), "Romania") == 0);
    assert(strcmp(returnContinent(getItem(getItem(h->stack, 0), 0)), "Europe") == 0);

    assert(addCountry(v, "Roma", "Polonia", 0) == ERROR_INVALID_POPULATION);
    assert(addCountry(v, NULL, "asia", 5.2) == ERROR_ELEM_NOT_FOUND);
    assert(addCountry(v, "Roma", NULL, 3.1) == ERROR_INVALID_NAME);

    result = addCountry(v, "China", "Asia", 500.2);
    assert(vectorSize(v) == 2);
    assert(result == SUCCES_ADDITION);
    addToHistory(h, copyVector(v));

    result = deleteCountry(v, "China");
    assert(vectorSize(v) == 1);

    assert(h->top == 1);
    assert(strcmp(returnName(getItem(getItem(h->stack, 1), 1)), "China") == 0);

    h->top = 0;
    Vector* vc = getItem(h->stack, h->top);

    assert(vectorSize(vc) == 1);
    assert(searchElement(vc, "China") == -1);

    addToHistory(h, copyVector(vc));
    assert(h->top == 1);

    Vector* repo = createVector(20, &destroyCountry, &copyCountry);
    initRepo(repo);

    deleteCountry(repo, "Romania");
    assert(searchElement(repo, "Romania") == -1);

    updateCountry(repo, "Germany", "default", "America", 0);
    assert(strcmp(returnContinent(getItem(repo, searchElement(repo, "Germany"))), "America") == 0);

    updateCountry(repo, "China", "Taiwan", "default", 0);
    assert(searchElement(repo, "Taiwan") != -1);
    assert(searchElement(repo, "China") == -1);


    assert(returnPopulation(getItem(repo, searchElement(repo, "Ukraine"))) == 43.733);
    updateCountry(repo, "Ukraine", "default", "default", 50.3);
    assert(returnPopulation(getItem(repo, searchElement(repo, "Ukraine"))) == 50.3);

    double population = returnPopulation(getItem(repo, searchElement(repo, "Tuvalu")));
    migratePopulation(repo, "Tuvalu", "Taiwan", 5.3);
    assert(returnPopulation(getItem(repo, searchElement(repo, "Tuvalu"))) == population + 5.3);


    destroyHistory(NULL);

    char* testString = lowerStr("123RomaNIA");
    assert(strcmp(testString, "123romania") == 0);
    free(testString);

    assert(addCountry(repo, "France", "Europe", 123) == ERROR_ELEM_NOT_FOUND);
    assert(addCountry(repo, "corona", "asda", 123) == ERROR_INVALID_NAME);
    assert(deleteCountry(repo, "corona") == ERROR_ELEM_NOT_FOUND);

    assert(updateCountry(repo, "corona", NULL, NULL, 123) == ERROR_ELEM_NOT_FOUND);
    assert(updateCountry(repo, "Malta", NULL, NULL, 123) == ERROR_INVALID_NAME);
    assert(updateCountry(repo, "Malta", "NULL", NULL, 123) == ERROR_INVALID_NAME);
    assert(updateCountry(repo, "Malta", "default", "NULL", 123) == ERROR_INVALID_NAME);
    assert(updateCountry(repo, "Malta", "default", "default", 0) == ERROR_INVALID_POPULATION);

    Vector* testRepo = createVector(20, &destroyCountry, &copyCountry);
    initRepo(testRepo);

    assert(migratePopulation(testRepo, "Romania", "France", 999) == ERROR_INVALID_POPULATION);
    assert(migratePopulation(testRepo, "Romania", "France", 0) == ERROR_INVALID_POPULATION);
    assert(migratePopulation(testRepo, "corona123", "France", 1) == ERROR_ELEM_NOT_FOUND);
    assert(migratePopulation(testRepo, "Romania", "Corona", 1) == ERROR_ELEM_NOT_FOUND);


    Vector* countryList = getCountriesMatchingString(testRepo, NULL);

    for(int i = 0; i < vectorSize(countryList); ++i)
        assert(strcmp(returnName(getItem(countryList, i)), returnName(getItem(testRepo, i))) == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingString(testRepo, "nimic");
    assert(vectorSize(countryList) == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingString(testRepo, "er");
    assert(strcmp(returnName(getItem(countryList, 0)), "United States of America") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Germany") == 0);
    assert(vectorSize(countryList) == 2);

    destroyVector(countryList);

    countryList = getCountriesMatchingNameAndContinent(testRepo);
    assert(strcmp(returnName(getItem(countryList, 0)), "Argentina") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Australia") == 0);
    assert(vectorSize(countryList) == 2);

    destroyVector(countryList);

    countryList = getCountriesMatchingString(testRepo, NULL);
    sortByCompareFunction(countryList, &compareCountriesName, "descending");

    assert(strcmp(returnName(getItem(countryList, 0)), "United States of America") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Ukraine") == 0);
    assert(strcmp(returnName(getItem(countryList, 2)), "Tuvalu") == 0);
    assert(strcmp(returnName(getItem(countryList, 3)), "Romania") == 0);
    assert(strcmp(returnName(getItem(countryList, 4)), "New Zealand") == 0);
    assert(strcmp(returnName(getItem(countryList, 5)), "Malta") == 0);
    assert(strcmp(returnName(getItem(countryList, 6)), "Japan") == 0);
    assert(strcmp(returnName(getItem(countryList, 7)), "Italy") == 0);
    assert(strcmp(returnName(getItem(countryList, 8)), "India") == 0);
    assert(strcmp(returnName(getItem(countryList, 9)), "Germany") == 0);
    assert(strcmp(returnName(getItem(countryList, 10)), "France") == 0);
    assert(strcmp(returnName(getItem(countryList, 11)), "China") == 0);
    assert(strcmp(returnName(getItem(countryList, 12)), "Canada") == 0);
    assert(strcmp(returnName(getItem(countryList, 13)), "Brazil") == 0);
    assert(strcmp(returnName(getItem(countryList, 14)), "Australia") == 0);
    assert(strcmp(returnName(getItem(countryList, 15)), "Argentina") == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingString(testRepo, NULL);
    sortByCompareFunction(countryList, &compareCountriesName, "ascending");

    assert(strcmp(returnName(getItem(countryList, 15)), "United States of America") == 0);
    assert(strcmp(returnName(getItem(countryList, 14)), "Ukraine") == 0);
    assert(strcmp(returnName(getItem(countryList, 13)), "Tuvalu") == 0);
    assert(strcmp(returnName(getItem(countryList, 12)), "Romania") == 0);
    assert(strcmp(returnName(getItem(countryList, 11)), "New Zealand") == 0);
    assert(strcmp(returnName(getItem(countryList, 10)), "Malta") == 0);
    assert(strcmp(returnName(getItem(countryList, 9)), "Japan") == 0);
    assert(strcmp(returnName(getItem(countryList, 8)), "Italy") == 0);
    assert(strcmp(returnName(getItem(countryList, 7)), "India") == 0);
    assert(strcmp(returnName(getItem(countryList, 6)), "Germany") == 0);
    assert(strcmp(returnName(getItem(countryList, 5)), "France") == 0);
    assert(strcmp(returnName(getItem(countryList, 4)), "China") == 0);
    assert(strcmp(returnName(getItem(countryList, 3)), "Canada") == 0);
    assert(strcmp(returnName(getItem(countryList, 2)), "Brazil") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Australia") == 0);
    assert(strcmp(returnName(getItem(countryList, 0)), "Argentina") == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingContinent(testRepo, "America", 0);
    sortByCompareFunction(countryList, &compareCountriesName, "descending");

    assert(strcmp(returnName(getItem(countryList, 0)), "United States of America") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Canada") == 0);
    assert(strcmp(returnName(getItem(countryList, 2)), "Brazil") == 0);
    assert(strcmp(returnName(getItem(countryList, 3)), "Argentina") == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingContinent(testRepo, "America", 50);
    sortByCompareFunction(countryList, &compareCountriesName, "descending");

    assert(strcmp(returnName(getItem(countryList, 0)), "United States of America") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "Brazil") == 0);

    destroyVector(countryList);

    countryList = getCountriesMatchingContinent(testRepo, NULL, 300);
    sortByCompareFunction(countryList, &compareCountriesPopulation, "descending");

    assert(strcmp(returnName(getItem(countryList, 0)), "China") == 0);
    assert(strcmp(returnName(getItem(countryList, 1)), "India") == 0);
    assert(strcmp(returnName(getItem(countryList, 2)), "United States of America") == 0);

    destroyVector(countryList);


    destroyVector(testRepo);
    destroyVector(v);
    destroyHistory(h);
    destroyVector(repo);
    printf("Services tests successfully passed!\n");
}

void runTests() {
    testCountry();
    testVector();
    testRepo();
    testServices();
    printf("All tests passed successfully!\n");
}