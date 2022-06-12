from src.repository.repository import Repo, RepoError
from src.domain.book import Book

def repositoryTests():

    repo = Repo()

    assert repo() == {}

    repo.add(Book(1, "Vali Vijelie", "Sot si amant"))
    assert repo()[1].ID == 1
    assert repo()[1].author == "Vali Vijelie"
    assert repo()[1].title == "Sot si amant"

    try:
        repo.add(Book(1, "Vali Vijelie", "Nu suntem la fel"))
        assert False
    except RepoError as re:
        assert str(re) == "Entity(ID: 1) is already in repo."

    del repo[1]
    assert repo() == {}

    try:
        del repo[1]
        assert False
    except RepoError as re:
        assert str(re) == "The entity with ID: 1 is not in repo."

    repo.add(Book(1, "Bla Bla", "Da da"))
    repo.add(Book(0, "Nane", "BBYMM"))
    repo.add(Book(2, "Florin Salam", "Dragostea"))

    assert repo[2].ID == 2
    assert repo[2].author == "Florin Salam"
    assert repo[2].title == "Dragostea"

    assert repo[1].ID == 1
    assert repo[1].author == "Bla Bla"
    assert repo[1].title == "Da da"

    repo[1] = Book(1, "Lemn", "Cioata")

    assert repo[1].ID == 1
    assert repo[1].author == "Lemn"
    assert repo[1].title == "Cioata"


repositoryTests()

