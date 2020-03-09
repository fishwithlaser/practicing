# Assumptions, data are come in as integers, and the min value is smaller than the max

class RangeManager():
    """Stores range-data and allows addition (add) subtraction (delete) and retrieving (get)"""

    def __init__(self):
        self.data = []
        self._smaller_tuple = [] # TODO delete me

        # 'lower case' methods are idiomatic in python, but instructions use caps. Allows either
        self.Add = self.add
        self.Delete = self.delete
        self.Get = self.get

    def __str__(self):
        return f'data: {self.data}'

    def add(self, start, end):
        """Inserts a range into the data and merges other ranges if necessary."""

        _tuple = (start, end)
        if _tuple not in self.data:
            self.data.append(_tuple)
            self.data.sort()
            sort_index = self.data.index(_tuple)
            if sort_index != 0:
                self._smaller_tuple = self.data[sort_index - 1]
                if self._smaller_tuple[1] >= self.data[sort_index][0]:
                    self._smaller_merge(sort_index)
                    sort_index += -1
            self._bigger_merge(sort_index)

    def delete(self, start, end):
        """Removes ranges that intersect with the given range."""

        _tuple = (start, end)
        self.data.append(_tuple)
        self.data.sort()
        sort_index = self.data.index(_tuple)
        if sort_index != 0:
            self._smaller_remove(sort_index)
        self._bigger_remove(sort_index)
        self.data.pop(sort_index)

    def get(self, start, end):
        """Returns an array of ranges within the given range."""
        _tuple = (start, end)
        self.data.append(_tuple)
        self.data.sort()
        sort_index = self.data.index(_tuple)
        get_list = []
        if sort_index != 0:
            # special case: (given range and data has the same input, but given has higher second value)
            # for example: TODO
            if self.data[sort_index-1][0] == self.data[sort_index][0]:
                get_list.append(self.data[sort_index-1])
        get_list = self._bigger_get(sort_index, get_list)
        return get_list

    def _smaller_remove(self, sort_index):
        if self.data[sort_index - 1][1] > self.data[sort_index][1]:
            self.data.append((self.data[sort_index][1], self.data[sort_index - 1][1]))
        if self.data[sort_index-1][1] > self.data[sort_index][0]:
            # reduces the range of the smaller tuple
            self.data[sort_index-1] = (self.data[sort_index-1][0], self.data[sort_index][0])
        self.data.sort()

    def _smaller_merge(self, sort_index):
        if self._smaller_tuple[1] >= self.data[sort_index][1]:
            self.data.pop(sort_index)
        # extend the range of the lower-tuple
        elif self._smaller_tuple[1] < self.data[sort_index][1]:
            self.data[sort_index-1] = (self.data[sort_index-1][0], self.data[sort_index][1])
            self.data.pop(sort_index)
        else:
            raise AssertionError("Shouldn't get here")

    def _bigger_merge(self, sort_index):
        while sort_index != len(self.data) - 1:
            if self.data[sort_index][1] < self.data[sort_index+1][0]:
                break
            # picks the higher entry of the input tuple and the tuple above
            if self.data[sort_index][1] > self.data[sort_index+1][1]:
                higher_entry = self.data[sort_index][1]
            else:
                higher_entry = self.data[sort_index+1][1]
            # extends the range of the higher-tuple
            self.data[sort_index] = (self.data[sort_index][0], higher_entry)
            self.data.pop(sort_index + 1)

    def _bigger_remove(self, sort_index):
        while sort_index != len(self.data) - 1:
            if self.data[sort_index][1] > self.data[sort_index+1][1]:
                self.data.pop(sort_index+1)
                continue
            # take the bigger of the numbers
            if self.data[sort_index][1] >= self.data[sort_index+1][0]:
                starting_int = self.data[sort_index][1]
            else:
                starting_int = self.data[sort_index+1][0]
            if starting_int == self.data[sort_index+1][1]:
                self.data.pop(sort_index + 1)
                continue
            # reduces the range of the higher-tuple
            self.data[sort_index + 1] = (starting_int, self.data[sort_index+1][1])
            break

    def _bigger_get(self, sort_index, get_list):
        iteration_index = sort_index + 1
        while sort_index != len(self.data) - 1:
            if self.data[sort_index][1] > self.data[iteration_index][1]:
                get_list.append(self.data[iteration_index])
                if iteration_index < len(self.data)-1:
                    iteration_index += 1
                    continue
                else:
                    break
            if self.data[sort_index][1] > self.data[iteration_index][0]:
                get_list.append((self.data[iteration_index][0], self.data[sort_index][1]))
            break
        self.data.pop(sort_index)
        return get_list


if __name__ == "__main__":
    test_manager = RangeManager()

    ####  TEST  CASES  ####
    #_____ ADDITION ______#
    test_manager.data = [(1, 2)]
    test_manager.Add(3, 5)
    assert test_manager.data == [(1, 2), (3, 5)]

    test_manager.data = [(1, 6)]
    test_manager.Add(3, 5)
    assert test_manager.data == [(1, 6)]

    test_manager.data = [(1, 4)]
    test_manager.Add(3, 5)
    assert test_manager.data == [(1, 5)]

    # SPECIAL CASE: Recursive merge addition
    test_manager.data = [(5, 10), (15, 20), (20, 25), (30, 35), (50, 55), (100, 101)]
    test_manager.Add(0, 50)
    assert test_manager.data == [(0, 55), (100, 101)]

    print('SUCCESS - 2A (addition problems)')

    #_____ DELETION ______#
    test_manager.data = [(1, 6)]
    test_manager.Delete(-3, -1)
    assert test_manager.data == [(1, 6)]

    test_manager.data = [(1, 6)]
    test_manager.Delete(-1, 10)
    assert test_manager.data == []

    test_manager.data = [(1, 6)]
    test_manager.Delete(4, 10)
    assert test_manager.data == [(1, 4)]

    # SPECIAL CASE 1: Truncation
    test_manager.data = [(0, 100)]
    test_manager.Delete(50, 60)
    assert test_manager.data == [(0, 50), (60, 100)]

    # SPECIAL CASE 2: unique indexing
    test_manager.data = [(0, 100)]
    test_manager.Delete(50, 51)
    assert test_manager.data == [(0, 50), (51, 100)]

    print('SUCCESS - 2B (deletion problems)')

    #_____ Getting ______#
    test_manager.data = [(1, 3), (5, 7)]
    ans = test_manager.get(4, 5)
    assert ans == []

    test_manager.data = [(1, 3), (5, 6)]
    ans = test_manager.get(4, 6)
    assert ans == [(5, 6)]

    test_manager.data = [(1, 3), (5, 6)]
    ans = test_manager.get(4, 6)
    assert ans == [(5, 6)]

    # SPECIAL CASE 2: tuple entry indexed after target entry
    test_manager.data = [(0, 5)]
    ans = test_manager.Get(0, 10)
    assert ans == [(0, 5)]

    # SPECIAL CASE 2: complex get
    test_manager.data = [(0, 5), (10, 11), (1000, 2000)]
    ans = test_manager.Get(0, 1050)
    assert ans == [(0, 5), (10, 11), (1000, 1050)]

    print('SUCCESS - 2C (get problems)')

