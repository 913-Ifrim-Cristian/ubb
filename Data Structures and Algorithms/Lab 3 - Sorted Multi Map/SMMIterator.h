#pragma once

#include "SortedMultiMap.h"


class SMMIterator{
	friend class SortedMultiMap;
private:
	//DO NOT CHANGE THIS PART
	const SortedMultiMap& map;
	SMMIterator(const SortedMultiMap& map);

	int head;
    int valuesHead;
    int visited;

public:
	void first();
	void next();
	bool valid(int k = 0) const;
    void jumpForward(int k);
   	TElem getCurrent() const;
};


