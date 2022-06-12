//
// Created by Cristi Ifrim on 3/20/2022.
//

#ifndef A5_6_913_IFRIM_CRISTIAN_UI_H
#define A5_6_913_IFRIM_CRISTIAN_UI_H

#include "../repo/repository.h"
#include "../services/service.h"
#include "../exceptions/exceptions.h"


class UI {

    AdminService __admin;
    UserService __user;

public:
    UI(AdminService& srv, UserService& usrv): __admin{srv}, __user{usrv} {}
    void start();
    void admin();
    void user();

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

};


#endif //A5_6_913_IFRIM_CRISTIAN_UI_H
