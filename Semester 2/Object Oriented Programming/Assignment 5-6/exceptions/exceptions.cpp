//
// Created by Cristi Ifrim on 3/23/2022.
//

#include "exceptions.h"

std::string errorMsg(int errorid) {
    /*
     * Returns the error text message based on it's id.
     */
    switch(errorid) {
        case ELEM_ERROR:
            return "ERROR: The element is not in the database!";
        case VALUE_ERROR:
            return "ERROR: The element is already in the database!";
        case INDEX_ERROR:
            return "ERROR: Array index out of bounds!";
        case INPUT_ERROR:
            return "ERROR: Invalid input!";
        default:
            return "";
    }
}
