#include "weatherapp.h"
#include <QtWidgets/QApplication>
#include "Controller.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Controller serv;

    WeatherApp w{serv};
    w.show();
    return a.exec();
}
