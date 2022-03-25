#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>
using namespace std;


FixedCapBiMapIterator::FixedCapBiMapIterator(const FixedCapBiMap& d) : map(d)
{
	this->current = 0;
}


void FixedCapBiMapIterator::first() {

	this->current = 0;
}


void FixedCapBiMapIterator::next() {
	if(!valid())
        throw std::exception();
    this->current++;
}


TElem FixedCapBiMapIterator::getCurrent(){
	if(!valid())
        throw std::exception();
	return this->map.elements[current];
}


bool FixedCapBiMapIterator::valid() const {
	return this->current < this->map.nrPairs;
}



