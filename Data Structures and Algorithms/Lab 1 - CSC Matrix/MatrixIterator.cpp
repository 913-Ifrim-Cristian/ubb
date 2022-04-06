//
// Created by Cristi Ifrim on 3/23/2022.
//

#include "MatrixIterator.h"
#include <exception>

MatrixIterator::MatrixIterator(const Matrix& matrix, int line): matrix(matrix), line(line) {
    /*
     * Theta(1)
     */
    if(this->line < 0 || this->line >= matrix.nrLines())
        throw std::exception();

    this->currentCol = 0;
}

void MatrixIterator::first() {
    /*
     * Theta(1)
     */
    this->currentCol = 0;
}

void MatrixIterator::next() {
    /*
     * Theta(1)
     */
    if(!this->valid())
        throw std::exception();
    this->currentCol++;
}

TElem MatrixIterator::getCurrent() {

    /*
     * Best Case: Theta(1) -> element is on line 0
     * Worst Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j] -> the last elem or is 0
     * Average Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j]
     * Total: O(n)
     */

    return matrix.element(this->line, this->currentCol);
}

bool MatrixIterator::valid() const {
    /*
     * Theta(1)
     */

    if(this->currentCol < 0 || this->currentCol >= matrix.nrColumns() - 1)
        return false;

    return true;
}