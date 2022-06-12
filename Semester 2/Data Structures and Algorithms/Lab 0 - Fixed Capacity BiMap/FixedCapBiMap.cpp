#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>

FixedCapBiMap::FixedCapBiMap(int capacity) {
	//TODO - Implementation
    if(capacity <= 0)
        throw std::exception();
    this->capacity = capacity;
    this->nrPairs = 0;
    this->elements = new TElem[capacity];
}

FixedCapBiMap::~FixedCapBiMap() {
    delete[] this->elements;
	//TODO - Implementation
}

bool FixedCapBiMap::add(TKey c, TValue v){
	if(this->capacity == this->nrPairs) {
        throw std::exception();
    }
    int index = 0, count = 0;
    while(count < 2 && index < this->nrPairs) {
        if(this->elements[index].first == c)
            count++;
        index++;
    }
    if(count == 2)
        return false;
    else {
        this->elements[this->nrPairs].first = c;
        this->elements[this->nrPairs].second = v;
        ++this->nrPairs;
        return true;
    }
	return false;
}

ValuePair FixedCapBiMap::search(TKey c) const{
	//TODO - Implementation
    ValuePair returnedValue;
    returnedValue.first = NULL_TVALUE;
    returnedValue.second = NULL_TVALUE;

    int count = 0, index = 0;
    while(count < 2 && index < this->nrPairs) {
        if(this->elements[index].first == c) {
            if (count == 0)
                returnedValue.first = this->elements[index].second;
            else
                returnedValue.second = this->elements[index].second;
            count++;
        }
        index++;
    }
	return returnedValue;
}

bool FixedCapBiMap::remove(TKey c, TValue v){
	int index = 0;
    bool found = false;
    while(index < this->nrPairs && !found) {
        if(this->elements[index].first == c && this->elements[index].second == v)
            found = true;
        else index++;
    }
    if(!found)
        return false;

    this->elements[index] = this->elements[this->nrPairs - 1];
    this->nrPairs--;
	return true;
}

ValuePair FixedCapBiMap::removeKey(TKey c) {
    ValuePair returnValue;
    returnValue.first = NULL_TVALUE;
    returnValue.second = NULL_TVALUE;

    int index = 0, count = 0;
    while(index < this->nrPairs && count < 2) {
        if(this->elements[index].first == c) {
            if (count == 0) {
                returnValue.first = this->elements[index].second;
                this->elements[index] = this->elements[--this->nrPairs];
                if(this->elements[index].first == c)
                    index--;
            }
            else {
                returnValue.second = this->elements[index].second;
                this->elements[index] = this->elements[--this->nrPairs];
            }
            count++;
        }
        index++;
    }

    return returnValue;
}


int FixedCapBiMap::size() const {

	return this->nrPairs;
}

bool FixedCapBiMap::isEmpty() const{

	return this->nrPairs == 0;
}

bool FixedCapBiMap::isFull() const {
	//TODO - Implementation
	return this->nrPairs == this->capacity;
}

FixedCapBiMapIterator FixedCapBiMap::iterator() const {
	return FixedCapBiMapIterator(*this);
}



