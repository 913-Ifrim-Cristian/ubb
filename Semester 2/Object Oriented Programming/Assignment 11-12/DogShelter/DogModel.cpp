#include "DogModel.h"
#include <qcolor.h>
#include <qbrush.h>

DogsModel::DogsModel(AdoptionList* repo) : repo{ repo }
{
}

int DogsModel::rowCount(const QModelIndex& parent) const
{
	return repo->get().size();
}

int DogsModel::columnCount(const QModelIndex& parent) const
{
	return 3;
}

QVariant DogsModel::data(const QModelIndex& index, int role) const
{
	int row = index.row();
	int column = index.column();

	Dog s = repo->operator[](row);
	if (role == Qt::DisplayRole) {
		switch (column) {
		case 0:
			return QString::fromStdString(s.getName());
		case 1:
			return QString::fromStdString(s.getBreed());
		case 2:
			return QString::number(s.getAge());
		}
	}
	else if (role == Qt::BackgroundRole) {
		if (row & 1)
			return QBrush(QColor(72, 72, 72));
	}
	return QVariant();
}

QVariant DogsModel::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (orientation == Qt::Horizontal && role == Qt::DisplayRole)
		switch (section) {
		case 0:
			return QString("Name");
		case 1:
			return QString("Breed");
		case 2:
			return QString("Age");
		default:
			break;
		}
	return QVariant();
}

