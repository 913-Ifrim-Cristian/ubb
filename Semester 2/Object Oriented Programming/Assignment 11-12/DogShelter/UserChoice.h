#pragma once

#include <QWidget>
#include "ui_UserChoice.h"
#include "service.h"
#include "UserGUI.h"

class UserChoice : public QWidget
{
	Q_OBJECT

public:
	UserChoice(UserService& srv, UserGUI* gui, QWidget *parent = Q_NULLPTR);
	~UserChoice();

	void openCSV();
	void openHTML();

private:
	Ui::UserChoice ui;
	UserGUI* userGUI;
	UserService& srv;
	void connectSignalsAndSlots();
};
