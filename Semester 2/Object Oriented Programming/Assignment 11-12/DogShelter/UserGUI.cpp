#include "UserGUI.h"
#include <qmessagebox.h>

UserGUI::UserGUI(UserService& srv, AdminService& adm, QWidget* asc, QWidget *parent)
	: srv{ srv }, admin{ adm }, ascendent{ asc }, QWidget(parent)
{
	int index = 0;
	ui.setupUi(this);
	undoShort = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Z), this);
	redoShort = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Y), this);
	model = Q_NULLPTR;
	listView = Q_NULLPTR;
	connectSignalsAndSlots();
	initAdoption();
	nam = Q_NULLPTR;
}

void UserGUI::filterAdopt()
{
	std::string breed = this->ui.breedFilter->text().toStdString();
	int age;
	if (this->ui.ageFilter->text().isEmpty())
		age = 9999;
	else
		age = this->ui.ageFilter->text().toInt();
	initAdoption(breed, age);
}

void UserGUI::next()
{
	if (this->toBeAdopted.empty()) {
		this->ui.nameShow->clear();
		this->ui.breedShow->clear();
		this->ui.ageShow->clear();
		this->ui.ageShow_2->clear();

		this->ui.adoptBtn->setEnabled(false);
		this->ui.nextBtn->setEnabled(false);
		return;
	}

	if (++index >= toBeAdopted.size() && index > 0)
		index = 0;

	Dog d = this->toBeAdopted[index];
	this->ui.nameShow->setText(QString::fromStdString(d.getName()));
	this->ui.breedShow->setText(QString::fromStdString(d.getBreed()));
	this->ui.ageShow->setText(QString::fromStdString(std::to_string(d.getAge())));
	this->ui.ageShow_2->setText(QString::fromStdString(d.getPhotograph()));
	
	if (nam != Q_NULLPTR)
		delete nam;

	nam = new QNetworkAccessManager(this);
	connect(nam, SIGNAL(finished(QNetworkReply*)), this, SLOT(loadImage(QNetworkReply*)));
	const QUrl url = QUrl(QString::fromStdString(d.getPhotograph()));
	QNetworkRequest request(url);
	nam->get(request);
}

void UserGUI::adopt()
{
	this->srv.adoptDog(this->toBeAdopted[index]);
	this->admin.remove(this->toBeAdopted[index].getName());
	this->toBeAdopted.erase(this->toBeAdopted.begin() + index);
	index--;
	this->next();
	this->populateList();
}

void UserGUI::open()
{
	this->srv.openAdoptionList();
}

void UserGUI::undo()
{
	try {
		this->srv.undo();
		this->populateList();
		filterAdopt();
	}
	catch (std::exception& ve) {
		QMessageBox msgBox;
		msgBox.setText(QString::fromStdString(ve.what()));
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
	}
}

void UserGUI::redo()
{
	try {
		this->srv.redo();
		this->populateList();
		filterAdopt();
	}
	catch (std::exception& ve) {
		QMessageBox msgBox;
		msgBox.setText(QString::fromStdString(ve.what()));
		msgBox.setWindowTitle("Dog shelter");
		msgBox.setStyleSheet("background-color: rgb(52, 52, 52); color: rgb(255, 0, 0);");
		msgBox.exec();
	}
}

void UserGUI::view()
{
	this->listView->show();
}

void UserGUI::init()
{
	index = 0;
	filterAdopt();
	if(this->srv.getAdoption() != nullptr)
		model = new DogsModel{ this->srv.getAdoption() };
		listView = new AdoptionListView{ model };
}

UserGUI::~UserGUI()
{
	if (model != Q_NULLPTR && listView != Q_NULLPTR) {
		delete model;
		delete listView;
	}
	delete nam;
	delete undoShort;
	delete redoShort;
}

void UserGUI::connectSignalsAndSlots()
{
	QObject::connect(this->ui.breedFilter, &QLineEdit::textChanged, this, &UserGUI::filterAdopt);
	QObject::connect(this->ui.ageFilter, &QLineEdit::textChanged, this, &UserGUI::filterAdopt);
	QObject::connect(this->ui.adoptBtn, &QAbstractButton::clicked, this, &UserGUI::adopt);
	QObject::connect(this->ui.nextBtn, &QAbstractButton::clicked, this, &UserGUI::next);
	QObject::connect(this->ui.openBtn, &QAbstractButton::clicked, this, &UserGUI::open);
	QObject::connect(this->ui.viewBtn, &QAbstractButton::clicked, this, &UserGUI::view);
	QObject::connect(this->undoShort, &QShortcut::activated, this, &UserGUI::undo);
	QObject::connect(this->redoShort, &QShortcut::activated, this, &UserGUI::redo);
}

void UserGUI::initAdoption(const std::string& breed, int age)
{
	if (!breed.empty() || age != 9999)
		this->toBeAdopted = this->srv.getDogListByFilter(breed, age);
	else
		this->toBeAdopted = this->srv.getDogList();

	if (this->toBeAdopted.empty()) {
		this->ui.nameShow->clear();
		this->ui.breedShow->clear();
		this->ui.ageShow->clear();
		this->ui.ageShow_2->clear();

		this->ui.adoptBtn->setEnabled(false);
		this->ui.nextBtn->setEnabled(false);
		return;
	}
	index = 0;
	Dog d = this->toBeAdopted[index];
	this->ui.nameShow->setText(QString::fromStdString(d.getName()));
	this->ui.breedShow->setText(QString::fromStdString(d.getBreed()));
	this->ui.ageShow->setText(QString::fromStdString(std::to_string(d.getAge())));
	this->ui.ageShow_2->setText(QString::fromStdString(d.getPhotograph()));
	this->ui.adoptBtn->setEnabled(true);
	this->ui.nextBtn->setEnabled(true);

	QNetworkAccessManager* nam = new QNetworkAccessManager(this);
	connect(nam, &QNetworkAccessManager::finished, this, &UserGUI::loadImage);
	const QUrl url = QUrl(QString::fromStdString(d.getPhotograph()));
	QNetworkRequest request(url);
	nam->get(request);
}

void UserGUI::loadImage(QNetworkReply* reply) {
	QPixmap pm;
	pm.loadFromData(reply->readAll());
	this->ui.dogPhoto->setPixmap(pm);
	this->ui.dogPhoto->setMask(pm.mask());
}

void UserGUI::populateList()
{
	this->ui.listWidget->clear();
	for (auto it : this->srv.getAdoptionList()) {
		this->ui.listWidget->addItem(QString::fromStdString(it.toString()));
	}
}

void UserGUI::closeEvent(QCloseEvent* event)
{
	this->ascendent->show();
	event->accept();
}