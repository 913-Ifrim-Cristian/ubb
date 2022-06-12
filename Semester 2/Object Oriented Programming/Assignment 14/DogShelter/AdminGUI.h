#pragma once

#include "ui_AdminGUI.h"
#include "service.h"
#include <QCloseEvent>
#include <qshortcut.h>


class AdminGUI : public QWidget
{
	Q_OBJECT

public:
	AdminGUI(AdminService& serv, QWidget* asc, QWidget *parent = Q_NULLPTR);
	~AdminGUI();

	void add();
	void remove();
	void update();
	void undo();
	void redo();
	void updateSlider();
	void updateAge();
	void filterList();
	void closeEvent(QCloseEvent* event) override;

private:
	Ui::AdminGUI ui;
	QWidget* ascendent;
	AdminService& srv;
	QShortcut* undoShort;
	QShortcut* redoShort;
	void populateList(const std::string& filter = "");
	void connectSignalsAndSlots();
};
