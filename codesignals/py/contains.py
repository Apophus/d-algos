class MovingTotal:
    def __init__(self,numbers):
        self.numbers = [numbers]


    list_ = []
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        _list = self.list_
        for number in numbers:
            self.list_.append(number)
        return _list

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        res = False
        sums = []
        numbers = self.append()
        for index, number in enumerate(numbers):

            if index > len(numbers) - 2:
                break
            else:
                sums.append(sum(numbers[index:index+3]))

        if total in sums:
            res = True

        return res


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))