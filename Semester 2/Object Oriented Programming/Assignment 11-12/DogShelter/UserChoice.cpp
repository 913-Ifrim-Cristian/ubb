#include "UserChoice.h"
#include "UserGUI.h"

UserChoice::UserChoice(UserService& srv, UserGUI* usrgui, QWidget *parent) 
	: srv{ srv }, userGUI {usrgui}, QWidget(parent)
{
	ui.setupUi(this);
	connectSignalsAndSlots();
}

UserChoice::~UserChoice()
{
}

void UserChoice::openHTML()
{
	this->srv.init(0);
	userGUI->init();
	userGUI->show();
	this->hide();
}

void UserChoice::openCSV()
{
	this->srv.init(1);
	userGUI->init();
	userGUI->show();
	this->hide();
}

void UserChoice::connectSignalsAndSlots()
{
	QObject::connect(this->ui.htmlBtn, &QAbstractButton::clicked, this, &UserChoice::openHTML);
	QObject::connect(this->ui.csvBtn, &QAbstractButton::clicked, this, &UserChoice::openCSV);
}
