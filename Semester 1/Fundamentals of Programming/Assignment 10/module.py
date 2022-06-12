class Module:
    """
    A class that implements an iterable data structure
    """
    def __init__(self):
        """
        Initialize the class
        """
        self.__data = dict()
        self.__keys = list()

    @staticmethod
    def sort(data, cmpFunction):
        """
        This function sorts a list using the shellSort algorithm
        shellSort is basically an insertion sort that allows exchanges of far elements and does not
        many movements one by one. It sorts and sub-array of length h and h decreases every time until 1
        :param data: the data to be sorted
        :param cmpFunction: the function used to compare two values
        :return: sorted data
        """
        newList = data[:]

        gap = len(newList) // 2

        while gap > 0:
            left = 0
            right = gap

            while right < len(newList):
                if cmpFunction(newList[left], newList[right]) is True:
                    newList[left], newList[right] = newList[left], newList[right]

                left += 1
                right += 1

                k = left
                while k - gap > -1:

                    if cmpFunction(newList[k - gap], newList[k]) is True:
                        newList[k - gap], newList[k] = newList[k], newList[k - gap]

                    k -= 1
            gap //= 2

        return newList

    @staticmethod
    def filter(data, filterFunction):
        """
        Filters the data
        :param data: the data to be filtered
        :param filterFunction: the acceptance function that decides if a value is filtered or not
        :return: the filtered data
        """
        filtered = []
        for value in data:
            if filterFunction(value) is True:
                filtered.append(value)

        return filtered

    def __setitem__(self, key, value):
        """
        Sets the item at the given key to the given value
        :param key: the index
        :param value: the value
        """
        if key in self.__keys:
            self.__data[key] = value
        else:
            self.__data[key] = value
            self.__keys.append(key)

    def __getitem__(self, item):
        """
        :param item: the given key
        :return: the item at the given key
        """
        return self.__data[item]

    def __delitem__(self, key):
        """
        Deletes an item at the given key
        :param key: the given key
        """
        del self.__data[key]
        for item in range(0, len(self.__keys)):
            if self.__keys[item] == key:
                self.__keys.pop(0)
                break

    def __next__(self):
        """
        :return: the next element during an iteration
        """
        if self.__iterator < len(self.__keys) - 1:
            self.__iterator += 1
            return self.__data[self.__keys[self.__iterator]]
        else:
            raise StopIteration

    def __iter__(self):
        """
        Initializes the iterator
        :return: the object to be iterated (self)
        """
        self.__iterator = -1
        return self

    def __len__(self):
        """
        :return: the length of the data
        """
        return len(self.__data)

    def __eq__(self, other):
        """
        :return: whether 2 sets of data are equal
        """
        return self.__data == other
    def __call__(self):
        """
        :return: the iterable data structure
        """
        return self.__data