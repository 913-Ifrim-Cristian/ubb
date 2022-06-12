cmake_minimum_required(VERSION 3.21)
project(Lab_2___Priority_Queue)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Lab_2___Priority_Queue
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        PriorityQueue.cpp
        PriorityQueue.h
        ShortTest.cpp
        ShortTest.h)
