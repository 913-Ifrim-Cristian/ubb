#pragma once
//DO NOT INCLUDE SORTEDMAPITERATOR
#include <functional>
#include <vector>
#include <utility>
#include <iostream>

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;

typedef bool(*Condition)(TValue);

#define NULL_TVALUE -111111
#define NULL_TPAIR std::pair<TKey, TValue>(-111111, -111111)

class SMIterator;
typedef bool (*Relation)(TKey, TKey);

struct Node {
    TElem info;
    Node* next;
};


class SortedMap {
    friend class SMIterator;

private:

    Node** data;
    int cap;
    Relation rel;
    int elems;

    int hashFunction(TKey c) const;
    Node** position(TKey key) const;


public:
    // implicit constructor
    SortedMap(Relation r);

    void resize();

    //adds a pair (key,value) to the map
    //if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
    //if the key SMes not exist, a new pair is added and the value null is returned
    TValue add(TKey c, TValue v);

    //searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
    TValue search(TKey c) const;

    //removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
    TValue remove(TKey c);

    //returns the number of pairs (key,value) from the map
    int size() const;

    //checks whether the map is empty or not
    bool isEmpty() const;

    // return the iterator for the map
    // the iterator will return the keys following the order given by the relation
    SMIterator iterator() const;

    void filter(Condition cond);

    // destructor
    ~SortedMap();
};
