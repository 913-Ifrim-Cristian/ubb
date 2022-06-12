#include "AdoptionListView.h"

AdoptionListView::AdoptionListView(QAbstractItemModel* model, QWidget *parent)
	: QWidget(parent)
{
	ui.setupUi(this);
	ui.tableView->setModel(model);
}

AdoptionListView::~AdoptionListView()
{
}
