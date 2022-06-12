/********************************************************************************
** Form generated from reading UI file 'UserGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_USERGUI_H
#define UI_USERGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_UserGUI
{
public:
    QVBoxLayout *verticalLayout_3;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *dogPhoto;
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout_2;
    QLineEdit *ageShow_2;
    QLabel *label_3;
    QLineEdit *breedShow;
    QLineEdit *nameShow;
    QLineEdit *ageShow;
    QLabel *label;
    QLabel *label_5;
    QLabel *label_4;
    QGridLayout *gridLayout_3;
    QPushButton *adoptBtn;
    QPushButton *nextBtn;
    QGridLayout *gridLayout_4;
    QLineEdit *ageFilter;
    QLineEdit *breedFilter;
    QLabel *label_6;
    QLabel *label_7;
    QFrame *line;
    QGridLayout *gridLayout_6;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_2;
    QListWidget *listWidget;
    QGridLayout *gridLayout_5;
    QPushButton *viewBtn;
    QPushButton *openBtn;

    void setupUi(QWidget *UserGUI)
    {
        if (UserGUI->objectName().isEmpty())
            UserGUI->setObjectName(QString::fromUtf8("UserGUI"));
        UserGUI->setWindowModality(Qt::NonModal);
        UserGUI->resize(555, 545);
        UserGUI->setMinimumSize(QSize(555, 530));
        UserGUI->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 52, 52);"));
        verticalLayout_3 = new QVBoxLayout(UserGUI);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        dogPhoto = new QLabel(UserGUI);
        dogPhoto->setObjectName(QString::fromUtf8("dogPhoto"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(dogPhoto->sizePolicy().hasHeightForWidth());
        dogPhoto->setSizePolicy(sizePolicy);
        dogPhoto->setMinimumSize(QSize(180, 150));
        dogPhoto->setMaximumSize(QSize(180, 150));
        dogPhoto->setStyleSheet(QString::fromUtf8("border-color: rgb(0, 170, 0);"));
        dogPhoto->setTextFormat(Qt::RichText);
        dogPhoto->setScaledContents(true);

        horizontalLayout->addWidget(dogPhoto);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        ageShow_2 = new QLineEdit(UserGUI);
        ageShow_2->setObjectName(QString::fromUtf8("ageShow_2"));
        ageShow_2->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        ageShow_2->setReadOnly(true);

        gridLayout_2->addWidget(ageShow_2, 3, 1, 1, 1);

        label_3 = new QLabel(UserGUI);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(label_3, 1, 0, 1, 1);

        breedShow = new QLineEdit(UserGUI);
        breedShow->setObjectName(QString::fromUtf8("breedShow"));
        breedShow->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(breedShow, 1, 1, 1, 1);

        nameShow = new QLineEdit(UserGUI);
        nameShow->setObjectName(QString::fromUtf8("nameShow"));
        nameShow->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        nameShow->setReadOnly(true);

        gridLayout_2->addWidget(nameShow, 0, 1, 1, 1);

        ageShow = new QLineEdit(UserGUI);
        ageShow->setObjectName(QString::fromUtf8("ageShow"));
        ageShow->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        ageShow->setReadOnly(true);

        gridLayout_2->addWidget(ageShow, 2, 1, 1, 1);

        label = new QLabel(UserGUI);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        label_5 = new QLabel(UserGUI);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(label_5, 3, 0, 1, 1);

        label_4 = new QLabel(UserGUI);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_2->addWidget(label_4, 2, 0, 1, 1);


        verticalLayout->addLayout(gridLayout_2);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setSpacing(6);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        adoptBtn = new QPushButton(UserGUI);
        adoptBtn->setObjectName(QString::fromUtf8("adoptBtn"));
        adoptBtn->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"background-color: rgb(0, 170, 0);"));

        gridLayout_3->addWidget(adoptBtn, 0, 0, 1, 1);

        nextBtn = new QPushButton(UserGUI);
        nextBtn->setObjectName(QString::fromUtf8("nextBtn"));
        nextBtn->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"background-color: rgb(0, 170, 0);"));

        gridLayout_3->addWidget(nextBtn, 0, 1, 1, 1);


        verticalLayout->addLayout(gridLayout_3);


        horizontalLayout->addLayout(verticalLayout);


        gridLayout->addLayout(horizontalLayout, 0, 0, 1, 1);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setSpacing(6);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        ageFilter = new QLineEdit(UserGUI);
        ageFilter->setObjectName(QString::fromUtf8("ageFilter"));
        ageFilter->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_4->addWidget(ageFilter, 1, 1, 1, 1);

        breedFilter = new QLineEdit(UserGUI);
        breedFilter->setObjectName(QString::fromUtf8("breedFilter"));
        breedFilter->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));

        gridLayout_4->addWidget(breedFilter, 0, 1, 1, 1);

        label_6 = new QLabel(UserGUI);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_6->setAlignment(Qt::AlignCenter);

        gridLayout_4->addWidget(label_6, 0, 0, 1, 1);

        label_7 = new QLabel(UserGUI);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setStyleSheet(QString::fromUtf8("font: 12pt \"Century\";\n"
"color: rgb(0, 170, 0);"));
        label_7->setAlignment(Qt::AlignCenter);

        gridLayout_4->addWidget(label_7, 1, 0, 1, 1);


        gridLayout->addLayout(gridLayout_4, 1, 0, 1, 1);


        verticalLayout_3->addLayout(gridLayout);

        line = new QFrame(UserGUI);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout_3->addWidget(line);

        gridLayout_6 = new QGridLayout();
        gridLayout_6->setSpacing(6);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label_2 = new QLabel(UserGUI);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QFont font;
        font.setFamilies({QString::fromUtf8("Century")});
        font.setPointSize(12);
        label_2->setFont(font);
        label_2->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);"));
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(label_2);

        listWidget = new QListWidget(UserGUI);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));
        listWidget->setStyleSheet(QString::fromUtf8("color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        verticalLayout_2->addWidget(listWidget);


        gridLayout_6->addLayout(verticalLayout_2, 0, 0, 1, 1);

        gridLayout_5 = new QGridLayout();
        gridLayout_5->setSpacing(6);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        viewBtn = new QPushButton(UserGUI);
        viewBtn->setObjectName(QString::fromUtf8("viewBtn"));
        viewBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout_5->addWidget(viewBtn, 0, 0, 1, 1);

        openBtn = new QPushButton(UserGUI);
        openBtn->setObjectName(QString::fromUtf8("openBtn"));
        openBtn->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"Century\";"));

        gridLayout_5->addWidget(openBtn, 1, 0, 1, 1);


        gridLayout_6->addLayout(gridLayout_5, 0, 1, 1, 1);


        verticalLayout_3->addLayout(gridLayout_6);


        retranslateUi(UserGUI);

        QMetaObject::connectSlotsByName(UserGUI);
    } // setupUi

    void retranslateUi(QWidget *UserGUI)
    {
        UserGUI->setWindowTitle(QCoreApplication::translate("UserGUI", "UserGUI", nullptr));
        dogPhoto->setText(QString());
        label_3->setText(QCoreApplication::translate("UserGUI", "Breed:", nullptr));
        label->setText(QCoreApplication::translate("UserGUI", "Name:", nullptr));
        label_5->setText(QCoreApplication::translate("UserGUI", "URL:", nullptr));
        label_4->setText(QCoreApplication::translate("UserGUI", "Age:", nullptr));
        adoptBtn->setText(QCoreApplication::translate("UserGUI", "Adopt", nullptr));
        nextBtn->setText(QCoreApplication::translate("UserGUI", "Next", nullptr));
        label_6->setText(QCoreApplication::translate("UserGUI", "Breed filter", nullptr));
        label_7->setText(QCoreApplication::translate("UserGUI", "Age filter", nullptr));
        label_2->setText(QCoreApplication::translate("UserGUI", "Adoption List", nullptr));
        viewBtn->setText(QCoreApplication::translate("UserGUI", "View", nullptr));
        openBtn->setText(QCoreApplication::translate("UserGUI", "Open", nullptr));
    } // retranslateUi

};

namespace Ui {
    class UserGUI: public Ui_UserGUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_USERGUI_H
