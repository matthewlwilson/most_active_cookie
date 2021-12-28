import functions
from cookie_class import cookie


class args:
    def __init__(self, date):
        self.date = date


filename = "test_cookie_data.csv"


def test_get_search_date():
    """To test when a given date is successfully given"""

    arg = args('2018-12-09')
    assert functions.get_search_date(arg) == '2018-12-09'


def test_get_search_date_no_date():
    """If no date is given in the arguments, the function should return false"""
    arg = args("")
    assert functions.get_search_date(arg) == ""


def test_read_cookie_log_open_file():
    """This test will check to make sure the given filename opens"""
    cookieLog = open(filename, 'r')
    assert cookieLog.closed == False


def test_read_cookie_log():
    """Test to make sure this function returns an array of cookie objects"""
    res = functions.read_cookie_log(filename)
    cookie1 = cookie("AtY0laUfhglK3lC7", "2018-12-09", "14:19:00+00:00")
    cookie2 = cookie("SAZuXPGUrfbcn5UA", "2018-12-09", "10:13:00+00:00")
    cookie3 = cookie("5UAVanZf6UtGyKVS", "2018-12-09", "07:25:00+00:00")
    cookie4 = cookie("AtY0laUfhglK3lC7", "2018-12-09", "06:19:00+00:00")
    cookie5 = cookie("SAZuXPGUrfbcn5UA", "2018-12-08", "22:03:00+00:00")
    cookie6 = cookie("4sMM2LxV07bPJzwf", "2018-12-08", "21:30:00+00:00")
    cookie7 = cookie("fbcn5UAVanZf6UtG", "2018-12-08", "09:30:00+00:00")
    cookie8 = cookie("4sMM2LxV07bPJzwf", "2018-12-07", "23:30:00+00:00")

    expectedArry = [cookie1, cookie2, cookie3,
                    cookie4, cookie5, cookie6, cookie7, cookie8]
    i = 0
    for ele in res:
        # test that cookie ids are correctly stored
        assert ele.id == expectedArry[i].id
        # test that cookie dates are correctly stored
        assert ele.date == expectedArry[i].date
        # test that cookie times are correctly stored
        assert ele.time == expectedArry[i].time
        i += 1


def test_get_all_cookies_for_selected_date():
    """Test to make sure this func returns a new list of cookie ids whos date match the selected date"""

    expectedArry = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA",
                    "5UAVanZf6UtGyKVS", "AtY0laUfhglK3lC7"]

    cookieArry = functions.read_cookie_log(filename)
    date = "2018-12-09"
    res = functions.get_all_cookies_for_selected_date(date, cookieArry)

    i = 0
    for ele in res:
        assert ele == expectedArry[i]
        i += 1


def test_sort_most_active_cookie():
    """Test to make sure an array is returned that is correctly sorted by most active"""
    fakeCookieArry = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA",
                      "5UAVanZf6UtGyKVS", "AtY0laUfhglK3lC7"]
    expectedOutcome = ["AtY0laUfhglK3lC7",
                       "SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS"]
    assert functions.sort_most_active(fakeCookieArry) == expectedOutcome
