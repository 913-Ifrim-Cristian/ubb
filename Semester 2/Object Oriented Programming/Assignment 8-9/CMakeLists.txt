cmake_minimum_required(VERSION 3.21)
project(a8_9_913_Ifrim_Cristian)

set(CMAKE_CXX_STANDARD 14)

include_directories(array)
include_directories(domain)
include_directories(exceptions)
include_directories(repo)
include_directories(services)
include_directories(tests)
include_directories(ui)
include_directories(utilities)

add_executable(a8_9_913_Ifrim_Cristian
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
        services/validator.cpp
        services/validator.h
        tests/tests.cpp
        tests/tests.h
        ui/ui.cpp
        ui/ui.h
        utilities/utility.cpp
        utilities/utility.h
        main.cpp repo/FileRepository.cpp repo/FileRepository.h repo/AdoptionList.cpp repo/AdoptionList.h utilities/comparator.cpp utilities/comparator.h)
