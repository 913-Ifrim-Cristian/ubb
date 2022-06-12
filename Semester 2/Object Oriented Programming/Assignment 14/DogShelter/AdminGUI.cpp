#include "AdminGUI.h"
#include <sstream>
#include "exceptions.h"
#include "qmessagebox.h"
#include <cassert>

AdminGUI::AdminGUI(AdminService& serv, QWidget* asc, QWidget *parent)
	: srv{ serv }, ascendent{ asc }, QWidget(parent)
{
	ui.setupUi(this);
	this->populateList();
	undoShort = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Z), this);
	redoShort = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Y), this);
	connectSignalsAndSlots();
}

AdminGUI::~AdminGUI()
{
	delete undoShort;
	delete redoShort;
}

void AdminGUI::add()
{
	std::string name, breed, url;
	int age = this->ui.ageLabel->text().toInt();
	name = this->ui.nameEdit->text().toStdString();
	breed = this->ui.breedEdit->text().toStdString();
	url = this->ui.urlEdit->text().toStdString();

	try {
		this->srv.add(name, breed, age, url);
		this->populateList();
		this->ui.nameEdit->clear();
		this->ui.breedEdit->clear();
		this->ui.urlEdit->clear();
		this->ui.ageSlider->setValue(0);
	}
	catch (std::exception& ve) {
		QMessageBox msgBox;
		msgBox.setText(QString::fromStdString(ve.what()));
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
	}
}

void AdminGUI::remove()
{
	for (auto it : this->ui.dogList->selectedItems()) {
		std::stringstream text{ it->text().toStdString() };
		std::string token;
		std::getline(text, token, ',');

		std::stringstream text2{ token };
		std::getline(text2, token, ':');
		std::getline(text2, token, ':');

		std::stringstream text3{ token };
		std::getline(text3, token, ' ');
		std::getline(text3, token, ' ');

		try {
			this->srv.remove(token);
			this->populateList();
		}
		catch (std::exception& ve) {
			QMessageBox msgBox;
			msgBox.setText(QString::fromStdString(ve.what()));
			msgBox.setWindowTitle("Dog shelter");
			msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
			msgBox.exec();
		}
	}
}

void AdminGUI::update()
{
	if (this->ui.dogList->selectedItems().size() != 1) {
		QMessageBox msgBox;
		msgBox.setText("ERROR: Please select only one item");
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
		return;
	}
	for (auto it : this->ui.dogList->selectedItems()) {
		std::stringstream text{ it->text().toStdString() };
		std::string token;
		std::getline(text, token, ',');

		std::stringstream text2{ token };
		std::getline(text2, token, ':');
		std::getline(text2, token, ':');

		std::stringstream text3{ token };
		std::getline(text3, token, ' ');
		std::getline(text3, token, ' ');

		std::string age;
		for(int i = 0; i < 5; ++i)
			std::getline(text, age, ',');

		std::stringstream text4{ age };
		std::getline(text4, age, '.');

		//-------------------------------------------------
		std::vector<std::string> args;
		std::string newName = this->ui.nameEdit->text().toStdString();
		args.push_back(newName);
		std::string newBreed = this->ui.breedEdit->text().toStdString();
		args.push_back(newBreed);
		std::string newURL = this->ui.breedEdit->text().toStdString();
		args.push_back(newURL);
		//--------------------------------------------------
		int years = this->ui.ageSlider->value();

		try {
			this->srv.cascadeUpdate(token, args, years);
			this->populateList();
			this->ui.nameEdit->clear();
			this->ui.breedEdit->clear();
			this->ui.urlEdit->clear();
			this->ui.ageSlider->setValue(0);
		}
		catch (std::exception& ve) {
			QMessageBox msgBox;
			msgBox.setText(QString::fromStdString(ve.what()));
			msgBox.setWindowTitle("Dog shelter");
			msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
			msgBox.exec();
		}
	}

}

void AdminGUI::undo()
{
	try {
		this->srv.undo();
		this->populateList();
	}
	catch (std::exception& ve) {
		QMessageBox msgBox;
		msgBox.setText(QString::fromStdString(ve.what()));
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
	}
}

void AdminGUI::redo()
{
	try {
		this->srv.redo();
		this->populateList();
	}
	catch (std::exception& ve) {
		QMessageBox msgBox;
		msgBox.setText(QString::fromStdString(ve.what()));
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
	}
}

void AdminGUI::updateSlider()
{
	for (auto it : this->ui.dogList->selectedItems()) {
		std::stringstream text{ it->text().toStdString() };
		std::string age;
		for (int i = 0; i < 4; ++i)
			std::getline(text, age, ':');

		std::stringstream text4{ age };
		std::getline(text4, age, '.');
		this->ui.ageSlider->setValue(stoi(age));
	}
}

void AdminGUI::updateAge()
{
	int val = this->ui.ageSlider->value();
	this->ui.ageLabel->setText(QString::fromStdString(std::to_string(val)));
}

void AdminGUI::filterList()
{
	std::string filter = this->ui.filterEdit->text().toStdString();
	this->populateList(filter);
}

void AdminGUI::populateList(const std::string& filter)
{
	this->ui.dogList->clear();
	for (auto it : this->srv.getRepo().getData()) {
		if (filter.empty() || it.toString().find(filter) != std::string::npos)
			this->ui.dogList->addItem(QString::fromStdString(it.toString()));
			
	}
}

void AdminGUI::connectSignalsAndSlots()
{
	QObject::connect(this->ui.ageSlider, &QAbstractSlider::valueChanged, this, &AdminGUI::updateAge);
	QObject::connect(this->ui.filterEdit, &QLineEdit::textChanged, this, &AdminGUI::filterList);
	QObject::connect(this->ui.addBtn, &QAbstractButton::clicked, this, &AdminGUI::add);
	QObject::connect(this->ui.removeBtn, &QAbstractButton::clicked, this, &AdminGUI::remove);
	QObject::connect(this->ui.undoBtn, &QAbstractButton::clicked, this, &AdminGUI::undo);
	QObject::connect(this->ui.redoBtn, &QAbstractButton::clicked, this, &AdminGUI::redo);
	QObject::connect(this->ui.updateBtn, &QAbstractButton::clicked, this, &AdminGUI::update);
	QObject::connect(this->ui.dogList, &QListWidget::itemClicked, this, &AdminGUI::updateSlider);
	QObject::connect(this->undoShort, &QShortcut::activated, this, &AdminGUI::undo);
	QObject::connect(this->redoShort, &QShortcut::activated, this, &AdminGUI::redo);
}

void AdminGUI::closeEvent(QCloseEvent* event)
{
	this->ascendent->show();
	event->accept();
}
