#include "Matrix.h"
#include "MatrixIterator.h"
#include <exception>

using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
    /*
    * Total complexity: Theta(1)
    */

    this->cols = nrCols;
    this->rows = nrLines;
    this->lineSize = 0;
    this->sparseColumn = new int[this->cols + 1]{NULL_TELEM};
    this->sparseRow = new int[this->rows]{NULL_TELEM};
    this->values = new TElem[this->rows]{NULL_TELEM};
}

Matrix::~Matrix() {
    /*
    * Total complexity: Theta(1)
    */

    delete[] this->sparseColumn;
    delete[] this->sparseRow;
    delete[] this->values;
}


int Matrix::nrLines() const {
    /*
     * Total complexity: Theta(1)
     */

	return this->rows;
}


int Matrix::nrColumns() const {
    /*
     * Total complexity: Theta(1)
     */

	return this->cols;
}


TElem Matrix::element(int i, int j) const {
	/*
	 * Best Case: Theta(1) -> element is on line 0
	 * Worst Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j] -> the last elem or it doesn't exist
	 * Average Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j]
	 * Total: O(n)
	 */

    if(i < 0 || i > this->rows || j < 0 || j > this->cols)
        throw std::exception();

    int start = this->sparseColumn[j];
    int end = this->sparseColumn[j+1];

    while(start++ < end) {
        if(this->sparseRow[start] == i)
            return this->values[start];

    }

	return NULL_TELEM;
}

void Matrix::resize() {

    /*
     * Total complexity: Theta(lineSize)
     */

    auto newRows = new TElem[this->lineSize + 5];
    auto newValues = new TElem[this->lineSize + 5];

    for(int i = 0; i < this->lineSize; ++i) {
        newRows[i] = this->sparseRow[i];
        newValues[i] = this->values[i];
    }

    delete[] this->values;
    delete[] this->sparseRow;

    this->values = newValues;
    this->sparseRow = newRows;
}

TElem Matrix::modify(int i, int j, TElem e) {
	/*
	 * Best Case: Theta(1) -> Element exist and is the first in representation
	 * Worst Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j] -> Element does not exist
	 * Average Case: Theta(n) where n = sparseColumn[j+1] - sparseColumn[j]
	 * Total: O(n)
	 */

    if(i < 0 || i > this->rows || j < 0 || j > this->cols)
        throw std::exception();

    int start = this->sparseColumn[j];
    int end = this->sparseColumn[j+1];
    TElem old = NULL_TELEM;

    while(start++ < end) {
        if(this->sparseRow[start] == i) {
            old = this->values[start];
            if(e != NULL_TELEM)
                this->values[start] = e;
            else
                this->removeElem(start, j);

            return old;
        }

        if(this->sparseRow[start] > i) {

            old = this->values[start];

            this->addElem(start, i, j, e);

            return old;
        }
    }

    this->addElem(start, i, j, e);

	return NULL_TELEM;
}

void Matrix::addElem(int start, int i, int j, TElem e) {

    /*
     *  Total complexity: Theta(lineSize)
     */

    if(++this->lineSize % 5 == 0)
        this->resize();

    for(int index = this->lineSize; index > start; --index) {
        this->sparseRow[index] = this->sparseRow[index - 1];
        this->values[index] = this->values[index-1];
    }

    for(int index = j + 1; index <= this->cols; ++index)
        this->sparseColumn[index]++;

    this->sparseRow[start] = i;
    this->values[start] = e;
}

void Matrix::removeElem(int i, int j) {

    /*
    *  Total complexity: Theta(lineSize)
    */

    for(int _i = i; _i < this->lineSize; ++_i) {
        this->sparseRow[_i] = this->sparseRow[_i + 1];
        this->values[_i] = this->values[_i + 1];
    }

    for(int index = j + 1; index <= this->cols; ++index)
        this->sparseColumn[index]--;

}

MatrixIterator Matrix::iterator(int line) const {
    return MatrixIterator(*this, line);
}


