//
// Created by Cristi Ifrim on 3/23/2022.
//
#pragma once

#include "Matrix.h"

class MatrixIterator {

    friend class Matrix;

private:
    const Matrix& matrix;
    int line;
    int currentCol;


public:
    MatrixIterator(const Matrix& matrix, int line);
    void first();
    void next();
    TElem getCurrent();
    bool valid() const;

};