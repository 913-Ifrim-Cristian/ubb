import unittest
from src.domain.book import Book
from src.repository.repository import Repo
from src.errors.repoErrors import RepoError


class RepoErrors(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repo()
    def tearDown(self) -> None:
        pass

    def test_emptyRepo(self):
        testDict = {}
        self.assertEqual(self._repo(), testDict)
        self.assertEqual(len(self._repo), 0)

    def test_addEntity(self):
        newEntity = Book(0, "Ion Creanga", "Amintiri din Copilarie")
        self._repo.add(newEntity)

        self.assertEqual(len(self._repo), 1)
        self.assertEqual(self._repo[0], newEntity)

        with self.assertRaises(RepoError):
            self._repo.add(Book(0, "Ion Creanga", "Amintiri din Copilarie"))

    def test_callMethods(self):
        newEntity = Book(0, "Ion Creanga", "Amintiri din Copilarie")
        self._repo.add(newEntity)
        self.assertEqual(self._repo[0], newEntity)

        self._repo[0] = Book(0, "Figuri geometrice", "Bilosu")
        self.assertEqual(self._repo[0], Book(0, "Figuri geometrice", "Bilosu"))

        with self.assertRaises(RepoError):
            x = self._repo[1]

    def test_getList(self):
        newList = list(self._repo.getList())
        self.assertEqual(newList, [])

        self._repo.add(Book(0, "Ion Creanga", "Amintiri din Copilarie"))

        newList = list(self._repo.getList())
        self.assertEqual(newList, [Book(0, "Ion Creanga", "Amintiri din Copilarie")])

        self._repo.add(Book(1, "Ion Creanga", "Amintiri din Copilarie"))
        newList = list(self._repo.getList())
        self.assertEqual(newList, [Book(0, "Ion Creanga", "Amintiri din Copilarie"), Book(1, "Ion Creanga", "Amintiri din Copilarie")])

    def test_delItem(self):
        self._repo.add(Book(1, "Bla Bla", "Da da"))
        self._repo.add(Book(0, "Nane", "BBYMM"))
        self._repo.add(Book(2, "Florin Salam", "Dragostea"))

        del self._repo[1]

        self.assertEqual(len(self._repo), 2)

        with self.assertRaises(RepoError):
            x = self._repo[1]

        with self.assertRaises(RepoError):
            self._repo[1] = Book(1, "of of", "fo fo")


    def test_entireRepo(self):
        testDict = {}
        self.assertEqual(self._repo(), testDict)
        self.assertEqual(len(self._repo), 0)

        newEntity = Book(0, "Ion Creanga", "Amintiri din Copilarie")
        self._repo.add(newEntity)

        self.assertEqual(len(self._repo), 1)
        self.assertEqual(self._repo[0], newEntity)

        with self.assertRaises(RepoError):
            self._repo.add(Book(0, "Ion Creanga", "Amintiri din Copilarie"))

        newEntity = Book(1, "Ion Creanga", "Amintiri din Copilarie")
        self._repo.add(newEntity)
        self.assertEqual(self._repo[1], newEntity)

        self._repo[0] = Book(0, "Figuri geometrice", "Bilosu")
        self.assertEqual(self._repo[0], Book(0, "Figuri geometrice", "Bilosu"))

        with self.assertRaises(RepoError):
            x = self._repo[2]

        newList = list(self._repo.getList())
        self.assertEqual(newList, [Book(0, "Figuri geometrice", "Bilosu"), Book(1, "Ion Creanga", "Amintiri din Copilarie")])

        del self._repo[1]

        self.assertEqual(len(self._repo), 1)

        with self.assertRaises(RepoError):
            x = self._repo[1]

        with self.assertRaises(RepoError):
            self._repo[1] = Book(1, "of of", "fo fo")


if __name__ == '__main__':
    unittest.main()
