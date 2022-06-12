/********************************************************************************
** Form generated from reading UI file 'AdoptionListView.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADOPTIONLISTVIEW_H
#define UI_ADOPTIONLISTVIEW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTableView>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AdoptionListView
{
public:
    QVBoxLayout *verticalLayout;
    QTableView *tableView;

    void setupUi(QWidget *AdoptionListView)
    {
        if (AdoptionListView->objectName().isEmpty())
            AdoptionListView->setObjectName(QString::fromUtf8("AdoptionListView"));
        AdoptionListView->resize(698, 382);
        AdoptionListView->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 52, 52);\n"
"font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        verticalLayout = new QVBoxLayout(AdoptionListView);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        tableView = new QTableView(AdoptionListView);
        tableView->setObjectName(QString::fromUtf8("tableView"));

        verticalLayout->addWidget(tableView);


        retranslateUi(AdoptionListView);

        QMetaObject::connectSlotsByName(AdoptionListView);
    } // setupUi

    void retranslateUi(QWidget *AdoptionListView)
    {
        AdoptionListView->setWindowTitle(QCoreApplication::translate("AdoptionListView", "Adoption List", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdoptionListView: public Ui_AdoptionListView {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADOPTIONLISTVIEW_H
