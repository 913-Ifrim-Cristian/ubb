//
// Created by Cristi Ifrim on 3/16/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_DYNAMICARRAY_H
#define A5_6_913_IFRIM_CRISTIAN_DYNAMICARRAY_H

template<class T>
class DynamicArray {
private:
    int capacity;
    int size;
    T* data;

    void resize();

public:
    DynamicArray();
    DynamicArray(int capacity);
    DynamicArray(const DynamicArray&);
    ~DynamicArray();
    int getSize() const;
    T& operator[](int) const;
    DynamicArray& operator=(const DynamicArray&);
    void add(T);
    friend DynamicArray& operator+(DynamicArray& arr, T elem) { arr.add(elem); return arr; }
    friend DynamicArray& operator+(T elem, DynamicArray& arr) { arr.add(elem); return arr; }
    void remove(int);
    bool isEmpty() const { return this->size == 0; }
    bool isFull() const { return this->size == this->capacity; }
};


#endif //A5_6_913_IFRIM_CRISTIAN_DYNAMICARRAY_H
