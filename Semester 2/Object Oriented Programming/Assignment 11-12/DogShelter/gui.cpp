#include "gui.h"

GUI::GUI(AdminService& adm, UserService& srv, QWidget *parent)
    : admin{ adm }, user{ srv }, QMainWindow(parent)
{
    ui.setupUi(this);
    adminGui = new AdminGUI{ admin, this };
    userGui = new UserGUI{ user, admin, this };
    userChoice = new UserChoice{ user, userGui };
    connectSignalsAndSlots();
}

void GUI::openAdmin()
{
    this->adminGui->show();
    this->hide();
}

void GUI::openUser()
{
    this->userChoice->show();
    this->hide();
}

void GUI::connectSignalsAndSlots()
{
    QObject::connect(this->ui.adminBtn, &QAbstractButton::clicked, this, &GUI::openAdmin);
    QObject::connect(this->ui.userBtn, &QAbstractButton::clicked, this, &GUI::openUser);
}

GUI::~GUI() {
    delete adminGui;
    delete userGui;
    delete userChoice;
}
