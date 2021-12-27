import functions


class args:
    def __init__(self, date):
        self.date = date


def test_get_search_date():
    """To test when a given date is successfully given"""

    arg = args('2018-12-09')
    assert functions.get_search_date(arg) == '2018-12-09'


def test_no_search_date_given():
    """If no date is given in the arguments, the function should return false"""
    arg = args("")
    assert functions.get_search_date(arg) == False
