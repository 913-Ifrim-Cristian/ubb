import unittest
from src.domain.taxi import Taxi
from src.repository.repository import Repo, RepoError
from src.services.taxiService import TaxiService

class TaxiServiceTests(unittest.TestCase):

    def setUp(self) -> None:
        self._repo = Repo()
        self._service = TaxiService(self._repo, 6)

    def tearDown(self) -> None:
        pass

    def test_add_ride(self):
        self.assertEqual(len(self._repo), 6)

        taxi = self._service.add_ride(15, 16, 20, 26)
        self.assertEqual(self._repo[taxi].x, 20)
        self.assertEqual(self._repo[taxi].y, 26)
        self.assertEqual(self._repo[taxi].fare, 15)

        taxi = self._service.add_ride(50, 25, 90, 70)
        self.assertEqual(self._repo[taxi].x, 90)
        self.assertEqual(self._repo[taxi].y, 70)
        self.assertEqual(self._repo[taxi].fare, 100)

