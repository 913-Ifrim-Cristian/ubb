#pragma once

#include <QWidget>
#include "ui_AdoptionListView.h"

class AdoptionListView : public QWidget
{
	Q_OBJECT

public:
	AdoptionListView(QAbstractItemModel* model, QWidget *parent = Q_NULLPTR);
	~AdoptionListView();

private:
	Ui::AdoptionListView ui;
};
