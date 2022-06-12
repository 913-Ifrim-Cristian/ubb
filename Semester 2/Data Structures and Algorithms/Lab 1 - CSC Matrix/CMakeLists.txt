cmake_minimum_required(VERSION 3.21)
project(Lab_1___CSC_Matrix)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Lab_1___CSC_Matrix
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        Matrix.cpp
        Matrix.h
        MatrixIterator.cpp
        MatrixIterator.h
        ShortTest.cpp
        ShortTest.h)
