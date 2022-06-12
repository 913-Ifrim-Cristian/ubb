//
// Created by Cristi Ifrim on 3/16/2022.
//

#include "DynamicArray.h"
#include "../domain/dog.h"
#include "../exceptions/exceptions.h"

template<class T>
DynamicArray<T>::DynamicArray(): size{ 0 }, capacity{ 10 } {
    /*
     * Constructor class for DynamicArray class
     */
    this->data = new T[this->capacity];
}

template<class T>
DynamicArray<T>::DynamicArray(int capacity): size{ 0 }, capacity{ capacity } {
    /*
     * Overloaded constructor for DynamicArray class
     * Sets the initial capacity to a given integer
     */
    this->data = new T[this->capacity];
}



template<class T>
DynamicArray<T>::~DynamicArray() {
    /*
     * Destructor for DynamicArray class
     */
    delete[] this->data;
}

template<class T>
int DynamicArray<T>::getSize() const {
    /*
     * Getter of the size of the array
     */
    return this->size;
}

template<class T>
void DynamicArray<T>::resize() {
    /*
     * Resizes the array
     */
    this->capacity += 10;
    auto newData = new T[this->capacity];

    for(int i = 0; i < this->size; ++i)
        newData[i] = this->data[i];

    delete[] this->data;
    this->data = newData;
}

template<class T>
T& DynamicArray<T>::operator[](int i) const {
    /*
     * [] operator
     * Returns the item on a given index or throws an error if it doesn't exit
     */
    if(i < 0 || i >= this->size)
        throw INDEX_ERROR;

    return this->data[i];
}

template<class T>
void DynamicArray<T>::add(T elem) {
    /*
     * Adds an element to the array
     */
    if(this->isFull())
        this->resize();
    this->data[this->size++] = elem;
}

template<class T>
void DynamicArray<T>::remove(int index) {
    /*
     * Deletes an element from the array
     */
    if(index < 0 || index >= this->size)
        throw INDEX_ERROR;

    this->data[index] = this->data[--this->size];
}

template<class T>
DynamicArray<T>::DynamicArray(const DynamicArray& cpy) {
    /*
     * Copy constructor for the DynamicArray class
     */

    this->size = cpy.size;
    this->capacity = cpy.capacity;
    this->data = new T[this->capacity];
    for(int i = 0; i < this->size; ++i)
        this->data[i] = cpy[i];

}

template<class T>
DynamicArray<T>& DynamicArray<T>::operator=(const DynamicArray &v) {
    /*
     * Assignment operator overloaded
     */
    if (this == &v)
        return *this;

    this->capacity = v.capacity;
    this->size = v.size;

    delete[] this->data;
    this->data = new T[this->capacity];
    for (int i = 0; i < this->size; i++)
        this->data[i] = v[i];

    return *this;
}

template class DynamicArray<Dog>;
template class DynamicArray<std::string>;
template class DynamicArray<int>;