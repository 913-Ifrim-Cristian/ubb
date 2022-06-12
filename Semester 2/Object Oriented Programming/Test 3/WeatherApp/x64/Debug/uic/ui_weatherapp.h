/********************************************************************************
** Form generated from reading UI file 'weatherapp.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WEATHERAPP_H
#define UI_WEATHERAPP_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_WeatherAppClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QListWidget *intervalsList;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QLineEdit *precipitationsEdit;
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QLineEdit *startEdit;
    QLabel *label_3;
    QLineEdit *descEdit;
    QPushButton *calculateBtn;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *WeatherAppClass)
    {
        if (WeatherAppClass->objectName().isEmpty())
            WeatherAppClass->setObjectName(QString::fromUtf8("WeatherAppClass"));
        WeatherAppClass->resize(322, 467);
        centralWidget = new QWidget(WeatherAppClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        intervalsList = new QListWidget(centralWidget);
        intervalsList->setObjectName(QString::fromUtf8("intervalsList"));

        verticalLayout_2->addWidget(intervalsList);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("font: 700 11pt \"Segoe UI\";"));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        precipitationsEdit = new QLineEdit(centralWidget);
        precipitationsEdit->setObjectName(QString::fromUtf8("precipitationsEdit"));

        gridLayout_2->addWidget(precipitationsEdit, 0, 1, 1, 1);


        verticalLayout_2->addLayout(gridLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setStyleSheet(QString::fromUtf8("font: 700 11pt \"Segoe UI\";"));

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        startEdit = new QLineEdit(centralWidget);
        startEdit->setObjectName(QString::fromUtf8("startEdit"));

        gridLayout->addWidget(startEdit, 0, 1, 1, 1);

        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("font: 700 11pt \"Segoe UI\";"));

        gridLayout->addWidget(label_3, 1, 0, 1, 1);

        descEdit = new QLineEdit(centralWidget);
        descEdit->setObjectName(QString::fromUtf8("descEdit"));

        gridLayout->addWidget(descEdit, 1, 1, 1, 1);


        verticalLayout->addLayout(gridLayout);

        calculateBtn = new QPushButton(centralWidget);
        calculateBtn->setObjectName(QString::fromUtf8("calculateBtn"));

        verticalLayout->addWidget(calculateBtn);


        verticalLayout_2->addLayout(verticalLayout);

        WeatherAppClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(WeatherAppClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        WeatherAppClass->setStatusBar(statusBar);

        retranslateUi(WeatherAppClass);

        QMetaObject::connectSlotsByName(WeatherAppClass);
    } // setupUi

    void retranslateUi(QMainWindow *WeatherAppClass)
    {
        WeatherAppClass->setWindowTitle(QCoreApplication::translate("WeatherAppClass", "WeatherApp", nullptr));
        label->setText(QCoreApplication::translate("WeatherAppClass", "Filter by precipitation", nullptr));
        label_2->setText(QCoreApplication::translate("WeatherAppClass", "Start hour", nullptr));
        label_3->setText(QCoreApplication::translate("WeatherAppClass", "Description", nullptr));
        calculateBtn->setText(QCoreApplication::translate("WeatherAppClass", "Calculate hours", nullptr));
    } // retranslateUi

};

namespace Ui {
    class WeatherAppClass: public Ui_WeatherAppClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WEATHERAPP_H
