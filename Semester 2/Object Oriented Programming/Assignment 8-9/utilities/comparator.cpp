//
// Created by Cristi Ifrim on 6/6/2022.
//

#include "comparator.h"

bool ComparatorAscendingByName::compare(Dog a, Dog b) {
    if(a.getName().compare(b.getName()) > 0)
        return true;
    return false;
}

bool ComparatorDescendingByAge::compare(Dog a, Dog b) {
    return a.getAge() <= b.getAge();
}

template<class T>
void sort(std::vector<T>& v, std::unique_ptr<Comparator<T>> c) {
    for(int i = 0; i < v.size() - 1; ++i)
        for(int j = i+1; j < v.size(); ++j)
            if(c->compare(v[i], v[j])) {
                T aux = v[j];
                v[j] = v[i];
                v[i] = aux;
            }
}
template void sort<Dog>(std::vector<Dog>& v, std::unique_ptr<Comparator<Dog>> c);