//
// Created by Cristi Ifrim on 3/4/2022.
//
#include "repo.h"
#include <string.h>

int searchElement(Vector* r, char* name) {
    /*
     * Searches for an element e in repo
     * If the element was found, its position in repo is returned, else -1
     */
    for(int i = 0; i < r->size; ++i) {
        if(strcasecmp(returnName(r->data[i]), name)==0)
            return i;
    }
    return -1;
}

void deleteElement(Vector* r, int pos) {
    /*
     * This function deletes and element from a given position
     */
    if(pos < 0 || pos >= r->size)
        return;

    Country* c = r->data[pos];
    r->data[pos] = r->data[--r->size];
    r->delVector(c);
}

void initRepo(Vector* r) {
    /*
     * This vector initializes a repo with certain values
     */
    addToVector(r, createCountry("Romania", "Europe", 19.29));
    addToVector(r, createCountry("China", "Asia",  1439.32));
    addToVector(r, createCountry("India", "Asia",  1380));
    addToVector(r, createCountry("United States of America", "America",  331.002));
    addToVector(r, createCountry("Canada", "America",  34.742));
    addToVector(r, createCountry("Italy", "Europe",  60.461));
    addToVector(r, createCountry("Germany", "Europe",  83.783));
    addToVector(r, createCountry("France", "Europe",  65.273));
    addToVector(r, createCountry("Brazil", "America",  212.559));
    addToVector(r, createCountry("Argentina", "America",  45.195));
    addToVector(r, createCountry("Japan", "Asia",  126.476));
    addToVector(r, createCountry("New Zealand", "Australia",  4.822));
    addToVector(r, createCountry("Tuvalu", "Australia",  0.011));
    addToVector(r, createCountry("Australia", "Australia",  25.499));
    addToVector(r, createCountry("Ukraine", "Europe",  43.733));
    addToVector(r, createCountry("Malta", "Europe",  0.441));
}

