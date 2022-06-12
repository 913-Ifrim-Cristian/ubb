//
// Created by Cristi Ifrim on 3/4/2022.
//
#include "ui.h"
#include <stdio.h>
#include <string.h>

void printMenu() {
    printf("--------------------------------------\n");
    printf("Section A\n");
    printf("--------------------------------------\n");
    printf("1. Add a country.\n2. Delete a country.\n3. Update a country.\n");
    printf("--------------------------------------\n");
    printf("Section B\n");
    printf("--------------------------------------\n");
    printf("4. Display all countries who respect a given filter.\n");
    printf("5. Display all countries on a given continent, whose populations are greater than a given value.\n");
    printf("--------------------------------------\n");
    printf("Section C\n");
    printf("--------------------------------------\n");
    printf("6. Undo the last performed operation\n");
    printf("7. Redo the last undone operation.\n");
    printf("8. Exit the program.\n");
    printf("--------------------------------------\n");
    printf("Extra\n");
    printf("--------------------------------------\n");
    printf("9. Display the elements sorted by name.\n");
}

int intSafeInput() {
    int input;
    scanf("%d", &input);
    while(getchar() != '\n');
    return input;
}

double doubleSafeInput() {
    double input;
    if(scanf("%lf", &input) == 0)
        input = 0;
    while(getchar() != '\n');
    return input;
}

void requestAddCountry(Vector* repo, History* history) {
    char name[101];
    char continent[15];
    double population;

    printf("Please enter the name of the country(MAX 100 CHARACTERS!): ");
    gets(name);

    printf("Please enter the continent: ");
    gets(continent);

    printf("Please enter the population: ");
    population = doubleSafeInput();
    int result = addCountry(repo, name, continent, population);

    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is already in the application.\n");
        return;
    }
    if(result == ERROR_INVALID_NAME) {
        printf("ERROR: Invalid continent. The continent should be Europe, Africa, Asia, America or Australia.\n");
        return;
    }
    if(result == ERROR_INVALID_POPULATION) {
        printf("ERROR: Invalid population. A country cannot have no population.\n");
        return;
    }
    if(result == ERROR_NULLPTR_GENERATED) {
        printf("ERROR: Couldn't generate that country.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s was added to the application.\n", name);

}

void requestDeleteCountry(Vector* repo, History* history) {
    char name[101];

    printf("Please enter the name of the country(MAX 100 CHARACTERS!): ");
    gets(name);

    int result = deleteCountry(repo, name);

    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is not in the application.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s was deleted from the application.\n", name);
}

void requestUpdateCountryName(Vector* repo, History* history) {
    char name[101], newName[101];

    printf("Please enter the name of the country(MAX 100 CHARACTERS!): ");
    gets(name);

    printf("Please enter the new name of the country(MAX 100 CHARACTERS!): ");
    gets(newName);

    int result = updateCountry(repo, name, newName, "default", 0);


    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is not in the application.\n");
        return;
    }
    if(result == ERROR_INVALID_NAME) {
        printf("ERROR: Invalid name. Please enter a valid name.\n");
        return;
    }
    if(result == ERROR_NULLPTR_GENERATED) {
        printf("ERROR: Couldn't update that country.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s was updated to %s.\n", name, newName);
}

void requestUpdateCountryContinent(Vector* repo, History* history) {
    char name[101], newName[101];

    printf("Please enter the name of the country(MAX 100 CHARACTERS!): ");
    gets(name);


    printf("Please enter the new continent: ");
    gets(newName);


    int result = updateCountry(repo, name, "default", newName, 0);

    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is not in the application.\n");
        return;
    }
    if(result == ERROR_INVALID_NAME) {
        printf("ERROR: Invalid continent. Please enter a valid continent.\n");
        return;
    }
    if(result == ERROR_NULLPTR_GENERATED) {
        printf("ERROR: Couldn't update that country.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s's continent was updated to %s.\n", name, newName);
}
void requestUpdateCountryPopulation(Vector* repo, History* history) {
    char name[101]; double newName;

    printf("Please enter the name of the country(MAX 100 CHARACTERS!): ");
    gets(name);


    printf("Please enter the new population: ");
    newName = doubleSafeInput();

    int result = updateCountry(repo, name, "default", "default", newName);


    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is not in the application.\n");
        return;
    }
    if(result == ERROR_INVALID_POPULATION) {
        printf("ERROR: Invalid population amount. A country cannot have 0 population.\n");
        return;
    }
    if(result == ERROR_NULLPTR_GENERATED) {
        printf("ERROR: Couldn't update that country.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s's population was updated to %0.1lf.\n", name, newName);
}
void requestMigratePopulation(Vector* repo, History* history) {
    char name[101], newName[101];
    double population;

    printf("Please enter the name of the destination country(MAX 100 CHARACTERS!): ");
    gets(name);


    printf("Please enter the name of the source country(MAX 100 CHARACTERS!): ");
    gets(newName);


    printf("Please enter the number of migrating people(Default is 0): ");
    population = doubleSafeInput();

    int result = migratePopulation(repo, name, newName, population);


    if(result == ERROR_ELEM_NOT_FOUND) {
        printf("ERROR: That country is not in the application.\n");
        return;
    }
    if(result == ERROR_INVALID_POPULATION) {
        printf("ERROR: Invalid population amount. A country cannot have 0 population or cannot migrate more than it's population.\n");
        return;
    }

    addToHistory(history, copyVector(repo));
    printf("SUCCESS: %s's population was migrated to %s.\n", newName, name);
}

void requestUpdateCountry(Vector* repo, History* history) {
    printf("What do you want to update?\n1. Update name.\n2. Update continent.\n3. Update population.\n4. Migrate population.\n");
    int option;
    printf("~$: ");
    option = intSafeInput();

    switch(option) {
        case 1:
            requestUpdateCountryName(repo, history);
            break;
        case 2:
            requestUpdateCountryContinent(repo, history);
            break;
        case 3:
            requestUpdateCountryPopulation(repo, history);
            break;
        case 4:
            requestMigratePopulation(repo, history);
            break;
        default:
            printf("Invalid option!");
            return;
    }
}

void requestPrintCountriesByName(Vector* repo) {
    char str[101];
    printf("Please enter the string that should be contained by a country's name: ");
    gets(str);

    Vector* listOfCountries;

    if(strtok(str, " ") == NULL)
        listOfCountries = getCountriesMatchingString(repo, NULL);
    else
        listOfCountries = getCountriesMatchingString(repo, str);

    printf("\n");
    if(listOfCountries->size == 0)
        printf("No countries with their name containing the string %s found!\n", str);
    else
        for(int i = 0; i < listOfCountries->size; ++i)
            printf("Country: %s, located on continent: %s with a population of: %0.3lf million people.\n", returnName(listOfCountries->data[i]),
                   returnContinent(listOfCountries->data[i]), returnPopulation(listOfCountries->data[i]));

    destroyVector(listOfCountries);
    printf("\n");
}

void requestPrintCountriesByContinent(Vector* repo) {
    char str[101], order[13];
    double population = 0;
    printf("Please enter the continent: ");
    gets(str);

    printf("Please enter the population(Default is 0): ");
    population = doubleSafeInput();

    printf("Please enter the sorting order(Default order is ascending): ");
    gets(order);



    Vector* listOfCountries;

    if(strtok(str, " ") == NULL)
        listOfCountries = getCountriesMatchingContinent(repo, NULL, population);
    else
        listOfCountries = getCountriesMatchingContinent(repo, str, population);

    printf("\n");
    if(listOfCountries->size == 0)
        printf("No countries on continent %s with their population greater than %0.3lf found!\n", str, population);
    else {
        sortByCompareFunction(listOfCountries, &compareCountriesPopulation, order);
        for (int i = 0; i < listOfCountries->size; ++i)
            printf("Country: %s, located on continent: %s with a population of: %0.3lf million people.\n",
                   returnName(listOfCountries->data[i]),
                   returnContinent(listOfCountries->data[i]), returnPopulation(listOfCountries->data[i]));
    }

    destroyVector(listOfCountries);
    printf("\n");
}

void requestUndo(History* h) {
    if(h->top == 0)
        printf("ERROR: There's nothing to undo.\n");
    else
        h->top--,
        printf("SUCCESS: The operation has successfully been undone.\n");
}

void requestRedo(History* h) {
    if(h->top == vectorSize(h->stack) - 1)
        printf("ERROR: There's nothing to redo.\n");
    else
        h->top++,
        printf("SUCCESS: The operation has successfully been redone.\n");
}

void requestPrintCountriesAsc(Vector* r) {

    Vector* listOfCountries = getCountriesMatchingString(r, NULL);

    printf("\n");
    if(listOfCountries->size == 0)
        printf("No countries in the app!\n");
    else {
        sortByCompareFunction(listOfCountries, &compareCountriesName, " ");
        for (int i = 0; i < listOfCountries->size; ++i)
            printf("Country: %s, located on continent: %s with a population of: %0.3lf million people.\n",
                   returnName(listOfCountries->data[i]),
                   returnContinent(listOfCountries->data[i]), returnPopulation(listOfCountries->data[i]));
    }
    destroyVector(listOfCountries);
    printf("\n");

}

void requestPrintCountriesByNameAndContinent(Vector* repo) {

    Vector* listOfCountries = getCountriesMatchingNameAndContinent(repo);

    printf("\n");
    if(listOfCountries->size == 0)
        printf("No countries with their name beginning with the same letter as their continent!\n");
    else
        for(int i = 0; i < listOfCountries->size; ++i)
            printf("Country: %s, located on continent: %s with a population of: %0.3lf million people.\n", returnName(listOfCountries->data[i]),
                   returnContinent(listOfCountries->data[i]), returnPopulation(listOfCountries->data[i]));

    destroyVector(listOfCountries);
    printf("\n");
}

void requestPrintCountriesByFilter(Vector* r) {
    printf("1. Display all countries whose name contains a given string.\n");
    printf("2. Display all countries whose name begin with the same letter as their continent.\n");
    printf("Please select a filter: ");
    int option = intSafeInput();
    switch(option) {
        case 1:
            requestPrintCountriesByName(r);
            break;
        case 2:
            requestPrintCountriesByNameAndContinent(r);
            break;
        default:
            printf("ERROR: Invalid filter.\n");
            break;
    }
    printf("\n");
}

void start(Vector* repo, History* history) {
    printf("Hello user! This is the World Population Management tool!\nThis application lets you keep track of every country's population.");

    addToHistory(history, copyVector(repo));

    while(1) {
        printf("Please select one of the options below:\n");
        printMenu();
        int option;
        Vector* auxiliaryRepo = copyVector(getItem(history->stack, history->top));
        printf("~$: ");

        option = intSafeInput();

        switch(option) {
            case 8:
                destroyHistory(history);
                destroyVector(repo);
                destroyVector(auxiliaryRepo);
                return;
            case 1:
                requestAddCountry(auxiliaryRepo, history);
                break;
            case 2:
                requestDeleteCountry(auxiliaryRepo, history);
                break;
            case 3:
                requestUpdateCountry(auxiliaryRepo, history);
                break;
            case 4:
                requestPrintCountriesByFilter(auxiliaryRepo);
                break;
            case 5:
                requestPrintCountriesByContinent(auxiliaryRepo);
                break;
            case 6:
                requestUndo(history);
                break;
            case 7:
                requestRedo(history);
                break;
            case 9:
                requestPrintCountriesAsc(repo);
                break;
            default:
                printf("ERROR: Invalid option.\n");
                break;
        }
        destroyVector(auxiliaryRepo);
    }
}
