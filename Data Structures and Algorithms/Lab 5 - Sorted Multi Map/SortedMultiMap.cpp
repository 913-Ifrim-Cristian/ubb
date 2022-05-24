#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
    rel = r;
    capacity = 16;
    firstFree = 0;
    data = new BSTNode[capacity];
    left = new int[capacity];
    right = new int[capacity];
    head = -1;
    elems = 0;
    for(int i = 0; i < 16; ++i) {
        left[i] = i + 1;
        right[i] = -1;
    }
    left[15] = -1;
}

BSTNode SortedMultiMap::createNode(TKey k) {
    BSTNode e{};
    e.k = k;
    e.elems = new TValue[16];
    e.capacity = 16;
    e.size = 0;

    return e;



}

void SortedMultiMap::add(TKey c, TValue v) {

    if (head == -1)
    {
        head = 0;
        data[head] = createNode(c);
        data[head].add(v);
        firstFree = left[firstFree];
        left[head] = -1;
        right[head] = -1;

        elems++;
        return;
    }

    int currentPos = head;
    int prevPos = -1;
    while (currentPos != -1)
    {
        if (data[currentPos].k == c)
            break;
        else if (rel(data[currentPos].k, c)) //current node  is "smaller" go right
        {
            prevPos = currentPos;
            currentPos = right[currentPos];
        }
        else if (!rel(data[currentPos].k, c))///search for an empty pos/existing pos
        {
            prevPos = currentPos;
            currentPos = left[currentPos];
        }
    }
    if (currentPos != -1) //if the key already exists
    {
        if (data[currentPos].size == data[currentPos].capacity)
            data[currentPos].resize();

        data[currentPos].add(v);

        elems++;
    }
    if (currentPos == -1) // if the key does not exist we must add it
    {
        if (firstFree == -1)
            resize();

        currentPos = firstFree;
        data[currentPos] = createNode(c);
        data[currentPos].add(v);

        if (rel(data[prevPos].k, c)) // previus node is "smaller" than the one we are adding, so add to the right
            right[prevPos] = currentPos;
        else
            left[prevPos] = currentPos;

        firstFree = left[currentPos];
        left[currentPos] = -1;
        right[currentPos] = -1;
        elems++;
    }
}

vector<TValue> SortedMultiMap::search(TKey c) const {
    int currentPos = head;
    while (currentPos != -1)
    {
        if (data[currentPos].k == c)
            return data[currentPos].getValues();

        else if (rel(data[currentPos].k, c)) //current node  is "smaller" go right
            currentPos = right[currentPos];

        else if (!rel(data[currentPos].k, c))///search for an empty pos/existing pos
            currentPos = left[currentPos];
    }

    return {};
}

bool SortedMultiMap::remove(TKey c, TValue v) {


    int currentPos = head;
    int prevPos = -1;
    while (currentPos != -1)
    {
        if (data[currentPos].k == c) {

            if(!data[currentPos].remove(v))
                return false;

            if(data[currentPos].size == 0) {
                removeNode(currentPos, prevPos);
            }

            elems--;
            return true;

        }
        else if (rel(data[currentPos].k, c)) //current node  is "smaller" go right
        {
            prevPos = currentPos;
            currentPos = right[currentPos];
        }
        else if (!rel(data[currentPos].k, c))///search for an empty pos/existing pos
        {
            prevPos = currentPos;
            currentPos = left[currentPos];
        }
    }

    return false;
}


int SortedMultiMap::size() const {

    return this->elems;
}

bool SortedMultiMap::isEmpty() const {

    return this->elems == 0;
}

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}

SortedMultiMap::~SortedMultiMap() {


    SMMIterator it = iterator();
    while (it.valid())
    {
        if (it.currVal == it.map.data[it.currNode].size)
        {
            delete[] it.map.data[it.currNode].elems;
        }
        it.next();
    }
    delete[] data;
    delete[] left;
    delete[] right;
}

void BSTNode::add(TValue e) {
    if(size == capacity)
        resize();

    elems[size++] = e;
}

void SortedMultiMap::removeNode(int pos, int prev) {

    if(prev != -1) {

        if (left[pos] == -1 && right[pos] == -1) {
            if (left[prev] == pos)
                left[prev] = -1;
            else
                right[prev] = -1;

            left[pos] = firstFree;
            firstFree = pos;

            return;
        }
        if (left[pos] == -1 || right[pos] == -1) {
            int desc;
            if (left[pos] != -1)
                desc = left[pos];
            else
                desc = right[pos];

            if (left[prev] == pos)
                left[prev] = desc;
            else
                right[prev] = desc;

            left[pos] = firstFree;
            firstFree = pos;

        } else {
            int currentPos = pos;
            int prevPos = prev;
            while (left[currentPos] != -1) {
                prevPos = currentPos;
                currentPos = left[currentPos];
            }

            delete[] data[pos].elems;
            data[pos] = data[currentPos];

            removeNode(currentPos, prevPos);

            left[currentPos] = firstFree;
            firstFree = currentPos;

        }
    }
    else //remove root
    {

        if (left[pos] == -1) //root has only right descendants
        {
            delete[] data[pos].elems;
            head = right[pos];

            left[pos] = firstFree;
            firstFree = pos;

            return;
        }

        delete[] data[pos].elems;
        head = left[pos];

        left[pos] = firstFree;
        firstFree = pos;
    }
}



void BSTNode::resize() {
    auto newList = new TValue[capacity * 2];

    for(int i = 0; i < capacity; ++i)
        newList[i] = elems[i];

    capacity *= 2;

    delete[] elems;

    elems = newList;
}

bool BSTNode::remove(TValue e) {
    for(int i = 0; i < size; ++i)
        if(elems[i] == e) {
            elems[i] = elems[--size];
            return true;
        }
    return false;
}

std::vector<TValue> BSTNode::getValues() const {
    std::vector<TValue> vct;

    vct.reserve(size);
    for(int i = 0; i < size; ++i)
        vct.push_back(elems[i]);

    return vct;
}

void SortedMultiMap::resize() {
    auto newList = new BSTNode[capacity * 2];
    auto newLeft = new int[capacity * 2];
    auto newRight = new int[capacity * 2];

    for(int i = 0; i < capacity; ++i) {
        newList[i] = data[i];
        newLeft[i] = left[i];
        newRight[i] = right[i];
    }

    for(int i = capacity; i < capacity * 2; ++i) {
        newRight[i] = -1;
        newLeft[i] = i + 1;
    }
    firstFree = capacity;
    capacity *= 2;

    newRight[capacity - 1] = -1;
    newLeft[capacity - 1] = -1;

    delete[] data;
    delete[] left;
    delete[] right;

    data = newList;
    left = newLeft;
    right = newRight;
}
