cmake_minimum_required(VERSION 3.21)
project(t1_913_Ifrim_Cristian_1)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(t1_913_Ifrim_Cristian_1
        bill.cpp
        bill.h
        main.cpp
        repository.cpp
        repository.h
        service.cpp
        service.h
        utility.cpp
        utility.h
        tests.cpp
        tests.h
        ui.cpp
        ui.h)
