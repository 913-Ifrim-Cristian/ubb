//
// Created by Cristi Ifrim on 3/4/2022.
//

#ifndef A3_4_913_IFRIM_CRISTIAN_VECTOR_H
#define A3_4_913_IFRIM_CRISTIAN_VECTOR_H

typedef void* TElem;
typedef void (*destroyTElem)(TElem);
typedef TElem (*copyTElem)(TElem);

typedef struct {
    int size, capacity;
    TElem* data;
    destroyTElem delVector;
    copyTElem cpyVector;
}Vector;

Vector* createVector(int capacity, destroyTElem delptr, copyTElem cpyptr);
void destroyVector(Vector* v);
void resizeVector(Vector* v);
void addToVector(Vector* v, TElem e);
int vectorSize(Vector* v);
TElem getItem(Vector* v, int position);
Vector* copyVector(Vector* v);
void testVector();


#endif //A3_4_913_IFRIM_CRISTIAN_VECTOR_H
