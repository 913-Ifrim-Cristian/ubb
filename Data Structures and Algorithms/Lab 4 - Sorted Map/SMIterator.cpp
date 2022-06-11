#include <algorithm>
#include <stdexcept>
#include "SMIterator.h"
#include "SortedMap.h"

void quickSort(Node* arr[], int low, int high, Relation rel);

SMIterator::SMIterator(const SortedMap& d) : map{ d } {
    /*
     * O(capacity + numberOfChains*log(numberOfChains))
     */
    chains = new Node*[map.cap];
    numberOfChains = 0;

    for (int i = 0; i < map.cap; ++i) {
        auto node = map.data[i];

        if (node != nullptr)
            chains[numberOfChains++] = node;
    }

    quickSort(chains, 0,  numberOfChains - 1, map.rel);

    currentListIndex = 0;
    if (numberOfChains != 0)
        currentNode = chains[currentListIndex];
    else
        currentNode = nullptr;
}

SMIterator::~SMIterator() {
    //Theta(1)
    delete[] chains;
}

void SMIterator::first() {
    //Theta(1)
    currentListIndex = 0;
    currentNode = chains[currentListIndex];
}

void SMIterator::next() {
    //Theta(1)
    if (!valid())
        throw std::exception{};

    currentNode = currentNode->next;

    if (currentNode == nullptr && currentListIndex <  numberOfChains - 1) {
        ++currentListIndex;
        currentNode = chains[currentListIndex];
    }
}

bool SMIterator::valid() const {
    //Theta(1)
    if (currentListIndex >=  numberOfChains || currentNode == nullptr)
        return false;
    return true;
}

TElem SMIterator::getCurrent() const {
    //Theta(1)
    if (!valid())
        throw std::exception{};

    return currentNode->info;
}

void swap(Node** a, Node** b) {
    //Theta(1)
    auto aux = *a;
    *a = *b;
    *b = aux;
}

int partition(Node* arr[], int low, int high, Relation rel) {
    int pivot = arr[high]->info.first;
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (rel(arr[j]->info.first, pivot)) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(Node* arr[], int low, int high, Relation rel) {
    //O(nlogn)
    if (low < high) {
        int pi = partition(arr, low, high, rel);

        quickSort(arr, low, pi - 1, rel);
        quickSort(arr, pi + 1, high, rel);
    }
}
