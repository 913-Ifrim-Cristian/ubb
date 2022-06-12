//
// Created by Cristi Ifrim on 2/22/2022.
//

#include <stdio.h>
#include <assert.h>
//#include <stdlib.h>

/*
 * NON-UI FUNCTIONS
 */

int checkIfPrime(int x) {
    /*
     * This function checks if a number is a prime number
     */

    if(!(x & 1) || x < 3)
        return x == 2;

    for(int d = 3; d * d <= x; d += 2)
        if(x % d == 0)
            return 0;

    return 1;
}

int checkPair(int a, int b) {

    /*
     * This function checks if a pair of numbers (a, b) satisfy the condition of twin numbers
     */

    return checkIfPrime(a) + checkIfPrime(b) == 2 && b - a == 2;

}

void longestDecreasingSub(int len, int const v[], int sol[]) {

    /*
     * This is the algorithm to determine the longest decreasing contiguous subsequence
     */

    int solNo = v[0], solStart = 0, solEnd = 0, bestSolStart = 0, bestSolEnd = 0;
    for(int i = 1; i < len; ++i)
        if(v[i] <= solNo) {
            solNo = v[i];
            solEnd = i;
        }
        else {
            if(solEnd - solStart > bestSolEnd - bestSolStart) {
                bestSolEnd = solEnd;
                bestSolStart = solStart;
            }
            solStart = i;
            solEnd = i;
            solNo = v[i];
        }

    if(solEnd - solStart > bestSolEnd - bestSolStart) {
        bestSolEnd = solEnd;
        bestSolStart = solStart;
    }

    sol[0] = bestSolStart;
    sol[1] = bestSolEnd;
}


/*
 * UI FUNCTIONS
*/

void readVector(int *len, int v[]) {
    /*
     * This function reads an array
     */

    //free(v);

    printf("Please enter how many numbers to read: ");
    scanf("%d", len);

    if (*len < 3) {
        printf("Please read at least 3 elements!\n\n");
        return;
    }

    //v = (int*)malloc(*len * sizeof(int));

    printf("Please enter the numbers of the array: ");

    for (int i = 0; i < *len; ++i)
        scanf("%d", &v[i]);

    printf("\nNumbers were successfully read. The string is: \n");
    for (int i = 0; i < *len; ++i)
        printf("%d ", v[i]);

    printf("\n\n");


}


void solveTaskOne() {
    /*
     * This function solves task 1
     */
    int n, a = 3, b = 5;
    printf("Please enter the number of pairs: ");
    scanf("%d", &n);

    if(n < 1) {
        printf("Error! The number of pairs should be greater than zero!\n\n");
        return;
    }

    printf("\nThe pairs are: \n");

    while(n) {
        if(checkPair(a, b) == 1) {
            printf("Pair: %d, %d\n", a, b);
            --n;
        }
        a += 2;
        b += 2;
    }
    printf("\n\n");

}

void solveTaskTwo(int len, int v[]) {
    /*
     * This function solves task two
     */

    if(len == 0) {
        printf("The vector is empty! Please read it with option 1!\n\n");
        return;
    }

    if(len < 3) {
        printf("The vector should contain at least 3 elements in order to provide a solution.\n\n");
        return;
    }


    int sol[2];
    longestDecreasingSub(len, v, sol);

    if(sol[0] == sol[1]) {
        printf("There is no such sequence.\n\n");
    }
    else {
        printf("The longest decreasing contiguous subsequence is: \n");
        for (int i = sol[0]; i <= sol[1]; ++i)
            printf("%d ", v[i]);
        printf("\n\n");
    }
}

void solveLabWork() {

    int n;

    printf("Please enter a number: ");
    scanf("%d", &n);

    if(n < 3) {
        printf("There are no prime numbers smaller than %d!\n\n", n);
        return;
    }
    printf("The prime numbers smaller than %d are: ", n);
    printf("2 ");
    for(int i = 3; i < n; i += 2) {
        if(checkIfPrime(i) == 1)
            printf("%d ", i);
    }

    printf("\n\n");

}

void testProgram();


int main() {

    /*
     * Main function which does all the magic
     */

    testProgram();

    int len = 0, vector[100001];
    //int *v;

    while(1) {

        printf("Hello user! Please select one of the following options: \n");
        printf("1. Read a vector of numbers\n2. Solve task 1\n3. Solve task 2\n4. Exit the program\n5. Solve lab work\n");

        int option;
        printf("Please enter an option: ");
        scanf("%d", &option);
        printf("\n");

        if(option == 4) {
            printf("Goodbye!");
            //free(v);
            return 0;
        }

        if(option == 1)
            readVector(&len, vector);
        else
            if(option == 2)
                solveTaskOne();
            else
                if(option == 3)
                    solveTaskTwo(len, vector);
                else
                    if(option == 5)
                        solveLabWork();
    }
    return 0;

}


/*
 * Tests
 */

void testProgram() {

    /*
     * Test function for all non-ui functions
     */

    int v[] = {1, 13, 15, 20, 24, 55, 42, 3}, len = 8, sol[2];

    longestDecreasingSub(len, v, sol);
    assert(sol[0] == 5 && sol[1] == 7);

    int v1[] = {8, 7, 6, 5, 4, 3, 2, 1};
    longestDecreasingSub(8, v1, sol);
    assert(sol[0] == 0 && sol[1] == 7);

    int v2[] = {1, 2, 3, 4, 5, 6, 7, 8};
    longestDecreasingSub(8, v2, sol);
    assert(sol[0] == 0 && sol[1] == 0);

    assert(checkPair(3, 5) == 1);
    assert(checkPair(1, 2) == 0);
    assert(checkPair(13, 15) == 0);
    assert(checkPair(17, 19) == 1);

    assert(checkIfPrime(2) == 1);
    assert(checkIfPrime(9) == 0);
    assert(checkIfPrime(83) == 1);
    assert(checkIfPrime(117) == 0);

    printf("All tests successfully passed!\n\n");
}
