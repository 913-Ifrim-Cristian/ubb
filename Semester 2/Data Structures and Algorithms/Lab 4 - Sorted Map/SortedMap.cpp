#include <exception>
#include "SMIterator.h"
#include "SortedMap.h"
#include <iostream>


SortedMap::SortedMap(Relation r) : rel{ r }, elems{ 0 }, cap{8}{
    this->data = new Node*[this->cap]{};
}


//returns a pointer to the array element corresponding to the key's hash value
Node** SortedMap::position(TKey key) const {
    /*
     * Theta(1)
     */
    auto index = this->hashFunction(key);
    return &this->data[index];
}

void SortedMap::resize() {
    /*
 * Theta(capacity)
 */
    auto old = this->data;

    this->cap *= 2;
    this->data = new Node*[this->cap]{};
    elems = 0;

    for (int i = 0; i < this->cap / 2; ++i) {
        auto node = old[i];

        while (node != nullptr) {
            add(node->info.first, node->info.second);
            node = node->next;
        }
    }

    delete[] old;
}

TValue SortedMap::add(TKey k, TValue v) {
    /*
    * Best case: Theta(1)
     * Worst case: Theta(capacity)
     * Average case: Theta(capacity)
     * Total: O(capacity)
    */
    double loadFactor = (double)this->elems / (double)this->cap;

    if (loadFactor >= 0.7)
        this->resize();

    auto ptr = this->position(k);

    if (*ptr == nullptr) {
        *ptr = new Node{ {k, v}, nullptr };
        ++elems;
        return NULL_TVALUE;
    }

    while (*ptr != nullptr && (*ptr)->info.first != k && rel((*ptr)->info.first, k))
        ptr = &((*ptr)->next);

    if (*ptr != nullptr) {
        if ((*ptr)->info.first == k) {             //we found an element with the same key
            auto oldValue = (*ptr)->info.second;
            (*ptr)->info.second = v;

            return oldValue;
        }
        else {                                      //we add according to relation
            auto newInfo = (*ptr)->info;
            (*ptr)->info = { k, v };
            (*ptr)->next = new Node{ newInfo, (*ptr)->next };

            ++elems;
            return NULL_TVALUE;
        }
    }
    else {
        *ptr = new Node{ {k, v}, nullptr };
        ++elems;

        return NULL_TVALUE;
    }
}

TValue SortedMap::search(TKey k) const {
    /*
     * Best case: Theta(1)
     * Worst case: Theta(number of elements in hashtable[i])
     * Average case: Theta(number of elements in hashtable[i])
     * Total: O(number of elements in hashtable[i])
     */
    auto ptr = this->position(k);

    while (*ptr != nullptr && (*ptr)->info.first != k)
        ptr = &((*ptr)->next);

    if (*ptr != nullptr)
        return (*ptr)->info.second;

    return NULL_TVALUE;
}

TValue SortedMap::remove(TKey k) {
    /*
     * Best case: Theta(1)
     * Worst case: Theta(number of elements in hashtable[i])
     * Average case: Theta(number of elements in hashtable[i])
     * Total: O(number of elements in hashtable[i])
     */
    auto ptr = this->position(k);

    if (*ptr == nullptr)
        return NULL_TVALUE;

    if ((*ptr)->info.first == k) {
        auto value = (*ptr)->info.second;
        auto oldNode = *ptr;

        *ptr = (*ptr)->next;

        delete oldNode;

        --elems;
        return value;
    }

    auto next = &((*ptr)->next);

    while (*next != nullptr && (*next)->info.first != k) {
        ptr = next;
        next = &((*ptr)->next);
    }

    if (*next != nullptr) {
        (*ptr)->next = (*next)->next;
        auto value = (*next)->info.second;

        delete next;
        --elems;
        return value;
    }

    return NULL_TVALUE;
}

//Theta(1)
int SortedMap::size() const {
    return elems;
}

//Theta(1)
bool SortedMap::isEmpty() const {
    return elems == 0;
}

//Theta(1)
SMIterator SortedMap::iterator() const {
    return SMIterator( *this );
}

SortedMap::~SortedMap() {
    /*
     * Total: Theta(capacity)
     */
    for (int i = 0; i < this->cap; ++i) {
        auto currentNode = this->data[i];

        while (currentNode != nullptr) {
            auto oldNode = currentNode;
            currentNode = currentNode->next;
            delete oldNode;
        }
    }
    delete[] this->data;
}

int SortedMap::hashFunction(TKey c) const {
    return (unsigned)c % this->cap;
}

void SortedMap::filter(Condition cond) {
    /*
     * O(this->capacity)
     */
    for (int i = 0; i < this->cap; ++i) {
        auto currentNode = &this->data[i];
        if(*currentNode == nullptr)
            continue;

        if(!cond((*currentNode)->info.second)) {
            auto oldNode = (*currentNode);
            *currentNode = (*currentNode)->next;
            delete oldNode;
            elems--;
            continue;
        }

        auto next = &((*currentNode)->next);

        while(*next != nullptr && cond((*next)->info.second)) {
            currentNode = next;
            next = &((*currentNode)->next);
        }

        if (*next != nullptr) {
            (*currentNode)->next = (*next)->next;
            delete next;
            --elems;
        }

    }
}
