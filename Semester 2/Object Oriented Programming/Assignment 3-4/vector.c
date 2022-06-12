//
// Created by Cristi Ifrim on 3/4/2022.
//
#include "vector.h"
#include <stdlib.h>
#include "country.h"
#include <string.h>
#include <assert.h>

Vector* createVector(int capacity, destroyTElem delptr, copyTElem cpyptr) {
    /*
     * Creates a pointer to a vector structure, initializes it and returns it
     */
    Vector* v = malloc(sizeof(Vector));
    if(v == NULL) {
        return NULL;
    }
    if(delptr == NULL) {
        return NULL;
    }
    v->delVector = delptr;
    v->cpyVector = cpyptr;
    v->size = 0;
    v->capacity = capacity;
    v->data = malloc(sizeof(TElem) * v->capacity);
    if(v->data == NULL) {
        free(v);
        return NULL;
    }
    return v;
}

Vector* copyVector(Vector* v) {
    /*
     * This function does a deep copy of a pointer to a vector structure and returns it
     */
    if(v == NULL)
        return NULL;

    Vector* copy = malloc(sizeof(Vector));
    copy->size = v->size;
    copy->delVector = v->delVector;
    copy->cpyVector = v->cpyVector;
    copy->capacity = v->capacity;
    copy->data = malloc(sizeof(TElem) * copy->capacity);
    for(int i = 0; i < v->size; ++i) {
        copy->data[i] = v->cpyVector(v->data[i]);
    }
    return copy;
}

TElem getItem(Vector* v, int position) {
    /*
     * Getter function for the element in the vector v on a specific position
     */
    if(position < 0 || position >= v->size)
        return NULL;

    return v->data[position];
}

void destroyVector(Vector* v) {
    /*
     * Destroys a vector and frees the memory
     */
    if(v == NULL)
        return;

    for(int i = 0; i < v->size; ++i) {
        if(v->data[i] != NULL) {
            v->delVector(v->data[i]);
        }
    }
    free(v->data);
    free(v);
}

void resizeVector(Vector* v) {
    /*
     * Resizes the vector in order to store more elements
     */
    v->capacity += 10;
    TElem* newData = malloc(sizeof(TElem) * v->capacity);

    for(int i = 0; i < v->size; ++i) {
        newData[i] = v->data[i];
    }

    free(v->data);
    v->data = newData;
}

void addToVector(Vector* v, TElem e) {
    /*
     * This function adds an element to the vector and if the vector is full, resizes it
     */
    if(v->size == v->capacity)
        resizeVector(v);

    v->data[v->size++] = e;
}

int vectorSize(Vector* v) {
    /*
     * Getter function for the size of the vector
     */
    return v->size;
}



