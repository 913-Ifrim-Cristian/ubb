from src.errors.settingsErrors import SettingsError


class Settings:
    def __init__(self):

        self.__fileName = "settings.properties"

        self.__settingsDict = {
            "repository": self.repoType,
            "books": self.booksFile,
            "clients": self.clientsFile,
            "rentals": self.rentalsFile,
            "ui": self.uiType
        }

        self.__repoType = ""
        self.__booksFile = ""
        self.__clientsFile = ""
        self.__rentalsFile = ""
        self.__uiType = ""

        self._loadSettings()



    def _loadSettings(self):

        f = open(self.__fileName, "rt")

        for line in f.readlines():
            setting, value = line.split(sep='=', maxsplit=1)
            setting = setting.strip()
            value = value.strip()

            if setting not in self.__settingsDict:
                raise SettingsError("Incorrect settings file!")

            self.__settingsDict[setting](value)

        f.close()

    def repo(self):
        return self.__repoType

    def books(self):
        return self.__booksFile

    def clients(self):
        return self.__clientsFile

    def rentals(self):
        return self.__rentalsFile

    def ui(self):
        return self.__uiType

    def repoType(self, value):
        self.__repoType = value

    def booksFile(self, value):
        self.__booksFile = value

    def clientsFile(self, value):
        self.__clientsFile = value

    def rentalsFile(self, value):
        self.__rentalsFile = value

    def uiType(self, value):
        self.__uiType = value


