/********************************************************************************
** Form generated from reading UI file 'UserChoice.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_USERCHOICE_H
#define UI_USERCHOICE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_UserChoice
{
public:
    QVBoxLayout *verticalLayout;
    QTextEdit *textEdit;
    QGridLayout *gridLayout;
    QPushButton *htmlBtn;
    QPushButton *csvBtn;

    void setupUi(QWidget *UserChoice)
    {
        if (UserChoice->objectName().isEmpty())
            UserChoice->setObjectName(QString::fromUtf8("UserChoice"));
        UserChoice->resize(259, 156);
        UserChoice->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 52,52);"));
        verticalLayout = new QVBoxLayout(UserChoice);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        textEdit = new QTextEdit(UserChoice);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setMaximumSize(QSize(16777215, 90));
        textEdit->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));
        textEdit->setFrameShape(QFrame::Box);
        textEdit->setReadOnly(true);

        verticalLayout->addWidget(textEdit);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        htmlBtn = new QPushButton(UserChoice);
        htmlBtn->setObjectName(QString::fromUtf8("htmlBtn"));
        htmlBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(htmlBtn, 0, 0, 1, 1);

        csvBtn = new QPushButton(UserChoice);
        csvBtn->setObjectName(QString::fromUtf8("csvBtn"));
        csvBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));
        csvBtn->setCheckable(false);
        csvBtn->setFlat(false);

        gridLayout->addWidget(csvBtn, 0, 1, 1, 1);


        verticalLayout->addLayout(gridLayout);


        retranslateUi(UserChoice);

        QMetaObject::connectSlotsByName(UserChoice);
    } // setupUi

    void retranslateUi(QWidget *UserChoice)
    {
        UserChoice->setWindowTitle(QCoreApplication::translate("UserChoice", "UserChoice", nullptr));
        textEdit->setHtml(QCoreApplication::translate("UserChoice", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Century'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Please select wether you want to save your adoption list to a HTML file or a CSV file.</span></p></body></html>", nullptr));
        htmlBtn->setText(QCoreApplication::translate("UserChoice", "HTML", nullptr));
        csvBtn->setText(QCoreApplication::translate("UserChoice", "CSV", nullptr));
    } // retranslateUi

};

namespace Ui {
    class UserChoice: public Ui_UserChoice {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_USERCHOICE_H
