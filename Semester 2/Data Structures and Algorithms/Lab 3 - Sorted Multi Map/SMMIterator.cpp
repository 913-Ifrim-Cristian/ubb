#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	head = map.head;
    if(head != -1)
        valuesHead = map.data[head].head;
    visited = 0;
}

void SMMIterator::first(){
	head = map.head;
    visited = 0;
    if(head != -1)
        valuesHead = map.data[head].head;
}

void SMMIterator::next(){

    if(!valid())
        throw exception();

	if(valuesHead != -1 && map.data[head].next[valuesHead] != -1) {
        valuesHead = map.data[head].next[valuesHead];
    } else {
        head = map.next[head];
        if(head != -1)
            valuesHead = map.data[head].head, visited++;
    }
}

bool SMMIterator::valid(int k) const{

	return head != -1 && map.size() - visited >= k;
}

TElem SMMIterator::getCurrent() const {
    if(!valid())
        throw exception();

	return {map.data[head].key, map.data[head].data[valuesHead]};
}

void SMMIterator::jumpForward(int k) {
    if(k <= 0)
        throw exception();

    if(!valid(k))
        throw exception();

    for(int i = 0; i < k; ++i)
        this->next();
}


