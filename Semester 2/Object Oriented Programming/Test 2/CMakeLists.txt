cmake_minimum_required(VERSION 3.21)
project(t2_913_Ifrim_Cristian_1)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(t2_913_Ifrim_Cristian_1
        Dwelling.cpp
        Dwelling.h Client.cpp Client.h RealEstateAgency.cpp RealEstateAgency.h UI.cpp UI.h main.cpp)
