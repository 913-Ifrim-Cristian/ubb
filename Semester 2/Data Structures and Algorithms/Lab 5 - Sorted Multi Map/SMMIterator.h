#pragma once

#include "SortedMultiMap.h"
#include <stack>


class SMMIterator{
	friend class SortedMultiMap;
private:
	//DO NOT CHANGE THIS PART
	const SortedMultiMap& map;
	SMMIterator(const SortedMultiMap& map);

    struct Node {
        int el;
        Node* next;
    };

    Node* stackHead;
    int stackElems;
    void addToStack(int e);
    void popFromStack();
    int stackTop();


    int currNode;
    int currVal;

public:
	void first();
	void next();
	bool valid() const;
   	TElem getCurrent() const;
};



