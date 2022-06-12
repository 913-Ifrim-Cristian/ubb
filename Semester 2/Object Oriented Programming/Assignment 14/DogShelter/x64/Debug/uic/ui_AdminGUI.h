/********************************************************************************
** Form generated from reading UI file 'AdminGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADMINGUI_H
#define UI_ADMINGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_AdminGUI
{
public:
    QVBoxLayout *verticalLayout;
    QListWidget *dogList;
    QGridLayout *gridLayout_2;
    QLabel *label_5;
    QLineEdit *filterEdit;
    QGridLayout *gridLayout_3;
    QLabel *label;
    QLineEdit *nameEdit;
    QLabel *label_2;
    QLineEdit *breedEdit;
    QLabel *label_3;
    QSlider *ageSlider;
    QLabel *ageLabel;
    QLabel *label_4;
    QLineEdit *urlEdit;
    QGridLayout *gridLayout;
    QPushButton *addBtn;
    QPushButton *removeBtn;
    QPushButton *updateBtn;
    QPushButton *undoBtn;
    QPushButton *redoBtn;

    void setupUi(QWidget *AdminGUI)
    {
        if (AdminGUI->objectName().isEmpty())
            AdminGUI->setObjectName(QString::fromUtf8("AdminGUI"));
        AdminGUI->resize(309, 468);
        AdminGUI->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 52, 52);"));
        verticalLayout = new QVBoxLayout(AdminGUI);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        dogList = new QListWidget(AdminGUI);
        dogList->setObjectName(QString::fromUtf8("dogList"));
        dogList->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);"));
        dogList->setWordWrap(false);
        dogList->setSelectionRectVisible(true);
        dogList->setItemAlignment(Qt::AlignLeading);

        verticalLayout->addWidget(dogList);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_5 = new QLabel(AdminGUI);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_5->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_5, 0, 0, 1, 1);

        filterEdit = new QLineEdit(AdminGUI);
        filterEdit->setObjectName(QString::fromUtf8("filterEdit"));
        filterEdit->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
            "color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(filterEdit, 0, 1, 1, 1);


        verticalLayout->addLayout(gridLayout_2);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setSpacing(6);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label = new QLabel(AdminGUI);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0)"));
        label->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label, 0, 0, 1, 1);

        nameEdit = new QLineEdit(AdminGUI);
        nameEdit->setObjectName(QString::fromUtf8("nameEdit"));
        nameEdit->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
            "color: rgb(0, 170, 0);"));

        gridLayout_3->addWidget(nameEdit, 0, 1, 1, 2);

        label_2 = new QLabel(AdminGUI);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_2, 1, 0, 1, 1);

        breedEdit = new QLineEdit(AdminGUI);
        breedEdit->setObjectName(QString::fromUtf8("breedEdit"));
        breedEdit->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
            "color: rgb(0, 170, 0);"));

        gridLayout_3->addWidget(breedEdit, 1, 1, 1, 2);

        label_3 = new QLabel(AdminGUI);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_3->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_3, 2, 0, 1, 1);

        ageSlider = new QSlider(AdminGUI);
        ageSlider->setObjectName(QString::fromUtf8("ageSlider"));
        ageSlider->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);"));
        ageSlider->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(ageSlider, 2, 1, 1, 1);

        ageLabel = new QLabel(AdminGUI);
        ageLabel->setObjectName(QString::fromUtf8("ageLabel"));
        ageLabel->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        ageLabel->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(ageLabel, 2, 2, 1, 1);

        label_4 = new QLabel(AdminGUI);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_4->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_4, 3, 0, 1, 1);

        urlEdit = new QLineEdit(AdminGUI);
        urlEdit->setObjectName(QString::fromUtf8("urlEdit"));
        urlEdit->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
            "color: rgb(0, 170, 0);"));

        gridLayout_3->addWidget(urlEdit, 3, 1, 1, 2);


        verticalLayout->addLayout(gridLayout_3);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        addBtn = new QPushButton(AdminGUI);
        addBtn->setObjectName(QString::fromUtf8("addBtn"));
        addBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(addBtn, 0, 0, 1, 1);

        removeBtn = new QPushButton(AdminGUI);
        removeBtn->setObjectName(QString::fromUtf8("removeBtn"));
        removeBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(removeBtn, 0, 1, 1, 2);

        updateBtn = new QPushButton(AdminGUI);
        updateBtn->setObjectName(QString::fromUtf8("updateBtn"));
        updateBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(updateBtn, 0, 3, 1, 1);

        undoBtn = new QPushButton(AdminGUI);
        undoBtn->setObjectName(QString::fromUtf8("undoBtn"));
        undoBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(undoBtn, 1, 0, 1, 2);

        redoBtn = new QPushButton(AdminGUI);
        redoBtn->setObjectName(QString::fromUtf8("redoBtn"));
        redoBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout->addWidget(redoBtn, 1, 2, 1, 2);


        verticalLayout->addLayout(gridLayout);


        retranslateUi(AdminGUI);

        QMetaObject::connectSlotsByName(AdminGUI);
    } // setupUi

    void retranslateUi(QWidget *AdminGUI)
    {
        AdminGUI->setWindowTitle(QCoreApplication::translate("AdminGUI", "AdminGUI", nullptr));
        label_5->setText(QCoreApplication::translate("AdminGUI", "Filter", nullptr));
        label->setText(QCoreApplication::translate("AdminGUI", "Name", nullptr));
        label_2->setText(QCoreApplication::translate("AdminGUI", "Breed", nullptr));
        label_3->setText(QCoreApplication::translate("AdminGUI", "Age", nullptr));
        ageLabel->setText(QCoreApplication::translate("AdminGUI", "0", nullptr));
        label_4->setText(QCoreApplication::translate("AdminGUI", "URL", nullptr));
        addBtn->setText(QCoreApplication::translate("AdminGUI", "Add", nullptr));
        removeBtn->setText(QCoreApplication::translate("AdminGUI", "Remove", nullptr));
        updateBtn->setText(QCoreApplication::translate("AdminGUI", "Update", nullptr));
        undoBtn->setText(QCoreApplication::translate("AdminGUI", "Undo", nullptr));
        redoBtn->setText(QCoreApplication::translate("AdminGUI", "Redo", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdminGUI: public Ui_AdminGUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMINGUI_H
