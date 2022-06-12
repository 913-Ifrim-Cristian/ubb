class SettingsError(Exception):
    def __init__(self, message = "Invalid settings!"):
        self.__message = message
        super().__init__(self.__message)