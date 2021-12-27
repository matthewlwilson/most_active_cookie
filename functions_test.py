import functions


def test_get_search_date():
    """To test when a given date is successfully given"""
    class args:
        def __init__(self, date):
            self.date = date
    arg = args('2018-12-09')
    assert functions.get_search_date(arg) == '2018-12-09'
