#pragma once

#include <QWidget>
#include "ui_UserGUI.h"
#include "service.h"
#include <QByteArray>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QCloseEvent>
#include "AdoptionListView.h"
#include "DogModel.h"
#include <qshortcut>

class UserGUI : public QWidget
{
	Q_OBJECT

public:
	UserGUI(UserService& srv, AdminService& adm, QWidget* asc, QWidget *parent = Q_NULLPTR);
	void filterAdopt();
	void next();
	void adopt();
	void open();
	void view();
	void init();
	void undo();
	void redo();
	void closeEvent(QCloseEvent* event) override;
	~UserGUI();

public slots:
	void loadImage(QNetworkReply* reply);

private:
	Ui::UserGUI ui;
	UserService& srv;
	AdminService& admin;
	QWidget* ascendent;
	DogsModel* model;
	AdoptionListView* listView;
	QShortcut* undoShort;
	QShortcut* redoShort;
	std::vector<Dog> toBeAdopted;
	QNetworkAccessManager* nam;
	int index;
	void connectSignalsAndSlots();
	void initAdoption(const std::string& breed = "", int age = 9999);
	void populateList();
};
