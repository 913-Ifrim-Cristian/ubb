#include "Action.h"

void ActionAdd::executeUndo()
{
	this->repo.remove(addedSong.getName());
}

void ActionAdd::executeRedo()
{
	this->repo.add(addedSong);
}

void ActionRemove::executeUndo()
{
	this->repo.add(deletedSong);
}

void ActionRemove::executeRedo()
{
	this->repo.remove(deletedSong.getName());
}

void ActionUpdate::executeUndo()
{
	this->repo.remove(newSong.getName());
	this->repo.add(oldSong);
}

void ActionUpdate::executeRedo()
{
	this->repo.remove(oldSong.getName());
	this->repo.add(newSong);
}

void ActionAdopt::executeUndo()
{
	adoptList->remove(adoptedDog);
	repo.add(adoptedDog);
}

void ActionAdopt::executeRedo()
{
	repo.remove(adoptedDog.getName());
	adoptList->adopt(adoptedDog);
}
