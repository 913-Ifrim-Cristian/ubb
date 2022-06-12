//
// Created by Cristi Ifrim on 3/20/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_UI_H
#define A5_6_913_IFRIM_CRISTIAN_UI_H

#include "../repo/repository.h"
#include "../services/service.h"
#include "../exceptions/exceptions.h"


class UI {

    AdminService admin;
    UserService user;

public:
    UI(AdminService& srv, UserService& usrv): admin{srv}, user{usrv} {}
    void start();
    void adminPanel();
    void userPanel();

    void adminShow();
    void adminAdd();
    void adminRemove();
    void adminUpdate();

    void updateName();
    void updateAge();
    void updateBreed();
    void updatePhoto();


    void userShow(int option);
    void userAdoptionList();
    void openAdoptionList();

};


#endif //A5_6_913_IFRIM_CRISTIAN_UI_H
