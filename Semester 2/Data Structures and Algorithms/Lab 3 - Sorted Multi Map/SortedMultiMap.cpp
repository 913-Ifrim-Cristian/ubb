#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
    rel = r;
    capacity = 15;
    firstFree = 0;
    data = new ValuesList[capacity];
    next = new int[capacity];
    head = -1;
    elems = 0;
    for(int i = 0; i < 15; ++i)
        next[i] = i + 1;
    next[14] = -1;
}

void SortedMultiMap::add(TKey c, TValue v) {
    if(firstFree == -1)
        resize();

    if(head == -1) {
        head = 0;
        tail = 0;

        data[head] = valuesList(c);
        data[head].add(v);

        firstFree = 1;
        next[head] = -1;

        elems++;
        return;
    }

    int pos = firstFree;
    firstFree = next[firstFree];

    if(!rel(data[head].key, c)) {
        data[pos] = valuesList(c);
        data[pos].add(v);

        next[pos] = head;
        head = pos;

        elems++;
        return;
    }

    if(data[tail].key == c) {
        data[tail].add(v);
        elems++;
        return;
    }

    if(rel(data[tail].key, c)) {
        data[pos] = valuesList(c);
        data[pos].add(v);

        next[pos] = -1;
        next[tail] = pos;
        tail = pos;

        elems++;
        return;
    }

    int curr = head;
    int prev = -1;
    while(curr != -1 && rel(data[curr].key, c) && data[curr].key != c)  {
        prev = curr;
        curr = next[curr];
    }

    if(data[curr].key == c) {
        data[curr].add(v);

        elems++;
        return;
    }

    if(!rel(data[curr].key, c)) {
        data[pos] = valuesList(c);
        data[pos].add(v);

        next[pos] = curr;
        next[prev] = pos;

        elems++;
        return;
    }



}

vector<TValue> SortedMultiMap::search(TKey c) const {


    int curr = head;

   while(curr != -1 && data[curr].key != c)
        curr = next[curr];

    if(curr == -1)
        return vector<TValue>();

    return data[curr].getElements();
}

bool SortedMultiMap::remove(TKey c, TValue v) {

    int curr = head;
    int prev = -1;

    while(curr != -1 && data[curr].key != c) {
        prev = curr;
        curr = next[curr];
    }
    if(curr == -1)
        return false;

    if(!data[curr].remove(v))
        return false;

    if(data[curr].elems == 0) {
        if(prev != -1)
            next[prev] = next[curr];
        else
            head = next[curr];

        next[curr] = firstFree;
        firstFree = curr;

        delete[] data[curr].data;
        delete[] data[curr].next;
    }

    elems--;
    return true;
}


int SortedMultiMap::size() const {
	return elems;
}

bool SortedMultiMap::isEmpty() const {
    return elems == 0;
}

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}

SortedMultiMap::~SortedMultiMap() {
    //delete[] data;
    //delete[] next;
}

SortedMultiMap::ValuesList SortedMultiMap::valuesList(TKey k)  {
    ValuesList v;
    v.key = k;
    v.capacity = 15;
    v.firstFree = 0;
    v.data = new TValue[capacity];
    v.next = new int[capacity];
    v.head = -1;
    v.elems = 0;
    for(int i = 0; i < 15; ++i) {
        v.next[i] = i + 1;
    }
    v.next[14] = -1;
    return v;
}

/*SortedMultiMap::ValuesList::~ValuesList() {
    delete[] next;
    delete[] data;
}*/

void SortedMultiMap::ValuesList::add(TValue e) {
    /*
     * Total complexity: Theta(1) without resize.
     */
    if(firstFree == -1)
        resize();

    if(head == -1) {
        head = 0;
        data[head] = e;

        firstFree = next[firstFree];
        next[head] = -1;

        elems++;
        return;
    }

    int pos = firstFree;
    firstFree = next[firstFree];
    data[pos] = e;
    next[pos] = head;
    head = pos;

    elems++;
}

void SortedMultiMap::ValuesList::resize() {

    /*
     * Total complexity: Theta(capacity)
     */

    auto newData = new TValue[capacity + 15];
    auto newNext = new int[capacity + 15];

    for(int i = 0; i < capacity; ++i) {
        newData[i] = data[i];
        newNext[i] = next[i];
    }
    for(int i = capacity; i < capacity + 15; ++i)
        newNext[i] = i + 1;
    newNext[capacity + 14] = -1;

    firstFree = capacity;
    capacity += 15;

    delete[] data;
    delete[] next;

    data = newData;
    next = newNext;
}

bool SortedMultiMap::ValuesList::remove(TValue e) {
    int curr = head;
    int prev = -1;


    while(curr != -1 && data[curr] != e) {
        prev = curr;
        curr = next[curr];
    }

    if(curr == -1)
        return false;

    if(prev == -1) {
        int pos = firstFree;
        firstFree = head;

        head = next[head];
        next[firstFree] = pos;

        elems--;
        return true;
    }

    int pos = firstFree;
    firstFree = curr;

    next[prev] = next[curr];
    next[curr] = next[pos];

    elems--;
    return true;
}

vector<TValue> SortedMultiMap::ValuesList::getElements() const {
    vector<TValue> vals{};

    int i = head;
    while(i != -1) {
        vals.push_back(data[i]);
        i = next[i];
    }

    return vals;
}

void SortedMultiMap::resize() {
    auto newData = new ValuesList[capacity + 15];
    auto newNext = new int[capacity + 15];

    for(int i = 0; i < capacity; ++i) {
        newData[i] = data[i];
        newNext[i] = next[i];
    }
    for(int i = capacity; i < capacity + 15; ++i)
        newNext[i] = i + 1;

    newNext[capacity + 14] = -1;

    firstFree = capacity;
    capacity += 15;

    delete[] data;
    delete[] next;

    data = newData;
    next = newNext;
}
