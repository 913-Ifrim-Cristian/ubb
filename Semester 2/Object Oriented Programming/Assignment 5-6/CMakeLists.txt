cmake_minimum_required(VERSION 3.21)
project(a5_6_913_Ifrim_Cristian)

set(CMAKE_CXX_STANDARD 14)

include_directories(array)
include_directories(domain)
include_directories(exceptions)
include_directories(repo)
include_directories(services)
include_directories(tests)
include_directories(ui)

add_executable(a5_6_913_Ifrim_Cristian
        array/DynamicArray.cpp
        array/DynamicArray.h
        domain/dog.cpp
        domain/dog.h
        exceptions/exceptions.cpp
        exceptions/exceptions.h
        repo/repository.cpp
        repo/repository.h
        services/service.cpp
        services/service.h
        tests/tests.cpp
        tests/tests.h
        ui/ui.cpp
        ui/ui.h
        main.cpp utilities/utility.cpp utilities/utility.h)
