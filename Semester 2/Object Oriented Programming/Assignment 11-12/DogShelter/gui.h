#pragma once
#include <QtWidgets/QMainWindow>
#include "ui_gui.h"
#include "service.h"
#include "UserChoice.h"
#include "AdminGUI.h"

class GUI : public QMainWindow
{
    Q_OBJECT

public:
    GUI(AdminService& adm, UserService& srv, QWidget *parent = Q_NULLPTR);
    ~GUI();
    void openAdmin();
    void openUser();

private:
    Ui::GUIClass ui;
    UserChoice* userChoice;
    UserGUI* userGui;
    AdminGUI* adminGui;
    AdminService& admin;
    UserService& user;
    void connectSignalsAndSlots();
};
