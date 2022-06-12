#pragma once
#include "SortedMap.h"

//DO NOT CHANGE THIS PART
class SMIterator {
    friend class SortedMap;

    const SortedMap& map;

    int numberOfChains;
    Node** chains;

    int currentListIndex;
    Node* currentNode;

    SMIterator(const SortedMap& d);

public:
    ~SMIterator();

    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};

