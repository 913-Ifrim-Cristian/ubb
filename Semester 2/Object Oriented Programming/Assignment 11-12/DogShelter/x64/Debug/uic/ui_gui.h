/********************************************************************************
** Form generated from reading UI file 'gui.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GUI_H
#define UI_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GUIClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QGridLayout *gridLayout;
    QPushButton *adminBtn;
    QPushButton *userBtn;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *GUIClass)
    {
        if (GUIClass->objectName().isEmpty())
            GUIClass->setObjectName(QString::fromUtf8("GUIClass"));
        GUIClass->resize(284, 200);
        GUIClass->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 52, 52);"));
        centralWidget = new QWidget(GUIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);\n"
"font: 700 12pt \"Cascadia Mono\";"));
        label->setTextFormat(Qt::AutoText);
        label->setScaledContents(false);
        label->setAlignment(Qt::AlignCenter);
        label->setWordWrap(true);

        verticalLayout->addWidget(label);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        adminBtn = new QPushButton(centralWidget);
        adminBtn->setObjectName(QString::fromUtf8("adminBtn"));
        adminBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 700 11pt \"Cascadia Mono\";\n"
"color: rgb(52, 52, 52);"));

        gridLayout->addWidget(adminBtn, 0, 0, 1, 1);

        userBtn = new QPushButton(centralWidget);
        userBtn->setObjectName(QString::fromUtf8("userBtn"));
        userBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 700 11pt \"Cascadia Mono\";\n"
"color: rgb(52, 52, 52);"));

        gridLayout->addWidget(userBtn, 0, 1, 1, 1);


        verticalLayout->addLayout(gridLayout);

        GUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(GUIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        GUIClass->setStatusBar(statusBar);

        retranslateUi(GUIClass);

        QMetaObject::connectSlotsByName(GUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *GUIClass)
    {
        GUIClass->setWindowTitle(QCoreApplication::translate("GUIClass", "DogShelter", nullptr));
        label->setText(QCoreApplication::translate("GUIClass", "Please select wether you want to use the apllication in user mode or in admin mode.", nullptr));
        adminBtn->setText(QCoreApplication::translate("GUIClass", "Admin", nullptr));
        userBtn->setText(QCoreApplication::translate("GUIClass", "User", nullptr));
    } // retranslateUi

};

namespace Ui {
    class GUIClass: public Ui_GUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GUI_H
