#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_weatherapp.h"
#include "Controller.h"

class WeatherApp : public QMainWindow
{
    Q_OBJECT

public:
    WeatherApp(Controller& srv, QWidget *parent = Q_NULLPTR);
    void filterPrecipitations();
    void calculateHours();

private:
    Ui::WeatherAppClass ui;
    Controller& service;

    void populateList(int probability = -1);
    void connectSignalsAndSlots();
};
