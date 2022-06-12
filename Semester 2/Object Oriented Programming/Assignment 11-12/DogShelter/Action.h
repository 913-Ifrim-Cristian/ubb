#pragma once
#include "Repository.h"
#include "AdoptionList.h"
#include "Dog.h"

class Action
{
public:
	virtual void executeUndo() = 0;
	virtual void executeRedo() = 0;
	virtual ~Action() {}
};

class ActionAdd : public Action {
	Dog addedSong;
	Repository& repo;
public:
	ActionAdd(Repository& r, Dog& s) : repo{ r }, addedSong{ s } {}
	void executeUndo() override;
	void executeRedo() override;
};

class ActionRemove : public Action {
	Dog deletedSong;
	Repository& repo;
public:
	ActionRemove(Repository& r, Dog& s) : repo{ r }, deletedSong{ s } {}
	void executeUndo() override;
	void executeRedo() override;
};

class ActionUpdate : public Action {
	Dog newSong, oldSong;
	Repository& repo;
public:
	ActionUpdate(Repository& r, Dog& updated, Dog& old) : repo{ r }, oldSong{ old }, newSong{ updated } {}
	void executeUndo() override;
	void executeRedo() override;
};

class ActionAdopt : public Action {
	Dog adoptedDog;
	AdoptionList* adoptList;
	Repository& repo;
public:
	ActionAdopt(AdoptionList* lst, Repository& repo, Dog& adopted) : adoptList{ lst }, repo{ repo }, adoptedDog{ adopted } {}
	void executeUndo() override;
	void executeRedo() override;
};

