#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	currNode = map.head;
    currVal = 0;

    if(map.isEmpty()) {
        currNode = -1;
        return;
    }

    while (currNode != -1) //while current pos is valid
    {
        s.push(currNode);
        currNode = map.left[currNode];
    } //current pos is the left until no more lefts
    if (!s.empty())
    {
        currNode = s.top();
        currVal = 0;
    }
}

void SMMIterator::first() {
    currNode = map.head;
    currVal = 0;

    s = std::stack<int>();

    if (map.isEmpty()) {
        currNode = -1;
        return;
    }

    while (currNode != -1) //while current pos is valid
    {
        s.push(currNode);
        currNode = map.left[currNode];
    } //current pos is the left until no more lefts
    if (!s.empty()) {
        currNode = s.top();
        currVal = 0;
    } else {
        currNode = -1;
    }

}

void SMMIterator::next(){
    if (!valid())
        throw exception();

    if(currVal++ < map.data[currNode].size - 1) {
        return;
    }

    int node = s.top();
    s.pop();

    if(map.right[node] != -1) {
        node = map.right[node];
        while(node != -1) {
            s.push(node);
            node = map.left[node];
        }
    }

    if(!s.empty()) {
        currNode = s.top();
    }
    else {
        currNode = -1;
    }
    currVal = 0;

}

bool SMMIterator::valid() const {

    return currNode != -1;
}

TElem SMMIterator::getCurrent() const{

    if (!valid())
        throw exception();

    TElem elem;
    elem.first = map.data[currNode].k;
    elem.second = map.data[currNode].elems[currVal];
    return elem;

}


