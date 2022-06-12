#include "weatherapp.h"
#include <qmessagebox.h>
#include <sstream>

WeatherApp::WeatherApp(Controller& srv, QWidget *parent)
    : QMainWindow(parent), service{srv}
{
    ui.setupUi(this);
    this->populateList();
    this->connectSignalsAndSlots();
}

void WeatherApp::filterPrecipitations()
{
    int prec = -1;
    if(!this->ui.precipitationsEdit->text().isEmpty())
        prec = this->ui.precipitationsEdit->text().toInt();

    this->populateList(prec);
}

void WeatherApp::calculateHours()
{
    int start = this->ui.startEdit->text().toInt();
    std::string desc = this->ui.descEdit->text().toStdString();

    int sum = service.totalHours(desc, start);
    if(sum == 0) { //error
        QMessageBox msgBox;
        msgBox.setText("ERROR: There are no intervals that respect the given conditions.");
        msgBox.exec();
        return;
    }
    QMessageBox msgBox;
    std::stringstream ss{};
    ss << "Total hours of " << desc << " weather after " << start << " o'clock: " << sum << ".";
    msgBox.setText(QString::fromStdString(ss.str()));
    msgBox.exec();

}

void WeatherApp::populateList(int probability)
{
    std::vector<Interval> list = service.getIntervals(probability);
    this->ui.intervalsList->clear();
    for (auto it : list) {
        this->ui.intervalsList->addItem(QString::fromStdString(it.toString()));
    }
}

void WeatherApp::connectSignalsAndSlots()
{
    QObject::connect(this->ui.precipitationsEdit, &QLineEdit::textChanged, this, &WeatherApp::filterPrecipitations);
    QObject::connect(this->ui.calculateBtn, &QAbstractButton::clicked, this, &WeatherApp::calculateHours);
}
