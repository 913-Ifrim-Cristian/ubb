/********************************************************************************
** Form generated from reading UI file 'GUI.ui'
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
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GUIClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QGridLayout *gridLayout;
    QLabel *idLabel;
    QLineEdit *lineEdit;
    QLabel *textLabel;
    QLineEdit *lineEdit_2;
    QLabel *answerLabel;
    QLineEdit *lineEdit_3;
    QLabel *scoreLabel;
    QLineEdit *lineEdit_4;
    QPushButton *pushButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *GUIClass)
    {
        if (GUIClass->objectName().isEmpty())
            GUIClass->setObjectName(QString::fromUtf8("GUIClass"));
        GUIClass->resize(538, 504);
        centralWidget = new QWidget(GUIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        idLabel = new QLabel(centralWidget);
        idLabel->setObjectName(QString::fromUtf8("idLabel"));
        idLabel->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";"));
        idLabel->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(idLabel, 0, 0, 1, 1);

        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 1, 1, 3);

        textLabel = new QLabel(centralWidget);
        textLabel->setObjectName(QString::fromUtf8("textLabel"));
        textLabel->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";"));
        textLabel->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(textLabel, 1, 0, 1, 1);

        lineEdit_2 = new QLineEdit(centralWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 1, 1, 1, 3);

        answerLabel = new QLabel(centralWidget);
        answerLabel->setObjectName(QString::fromUtf8("answerLabel"));
        answerLabel->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";"));
        answerLabel->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(answerLabel, 2, 0, 1, 2);

        lineEdit_3 = new QLineEdit(centralWidget);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        gridLayout->addWidget(lineEdit_3, 2, 2, 1, 2);

        scoreLabel = new QLabel(centralWidget);
        scoreLabel->setObjectName(QString::fromUtf8("scoreLabel"));
        scoreLabel->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";"));
        scoreLabel->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(scoreLabel, 3, 0, 1, 3);

        lineEdit_4 = new QLineEdit(centralWidget);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));

        gridLayout->addWidget(lineEdit_4, 3, 3, 1, 1);


        verticalLayout->addLayout(gridLayout);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);

        GUIClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(GUIClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 538, 22));
        GUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(GUIClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        GUIClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(GUIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        GUIClass->setStatusBar(statusBar);

        retranslateUi(GUIClass);

        QMetaObject::connectSlotsByName(GUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *GUIClass)
    {
        GUIClass->setWindowTitle(QCoreApplication::translate("GUIClass", "GUI", nullptr));
        idLabel->setText(QCoreApplication::translate("GUIClass", "ID", nullptr));
        textLabel->setText(QCoreApplication::translate("GUIClass", "Text", nullptr));
        answerLabel->setText(QCoreApplication::translate("GUIClass", "Answer", nullptr));
        scoreLabel->setText(QCoreApplication::translate("GUIClass", "Score", nullptr));
        pushButton->setText(QCoreApplication::translate("GUIClass", "Add", nullptr));
    } // retranslateUi

};

namespace Ui {
    class GUIClass: public Ui_GUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GUI_H
