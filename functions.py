import argparse
from cookie_class import cookie

# This function reads and parses cli-commands, returns namespace about a cookie filename and possibly a date


def get_args() -> object:
    parser = argparse.ArgumentParser(
        description="Enter a cookie log file and a date to search for all cookies of that date")
    parser.add_argument("filename",
                        help="The filename of the cookie log file")
    parser.add_argument("-d", help="date/timestamp in UTC")
    args = parser.parse_args()
    return args


# This function takes in a namespace object, and returns a cookie log filename


def get_cookie_filename(args: object) -> str:
    return args.filename

# This function takes in namespace object and returns a date to search for cookie, if no date was provided let the user know


def get_search_date(args: object) -> str:
    if args.d:
        return args.d
    print("Please enter a date, so that i may find the most active cookies")
    return ""

# This function takes in a cookie log filename, opens that file,
# and returns an array of cookie objects


def read_cookie_log(filename):
    cookieLog = open(filename, 'r')
    # skip first line of cvs file, which would say cookie,timestamp
    next(cookieLog)
    arryOfCookies = []
    for grabLine in cookieLog:
        splitLine = grabLine.split(',')
        cookieId = splitLine[0]
        cookieTimeStampList = splitLine[1].split('T')
        date = cookieTimeStampList[0]
        time = cookieTimeStampList[1].rstrip('\n')
        newCookie = cookie(cookieId, date, time)
        arryOfCookies.append(newCookie)
    cookieLog.close()
    return arryOfCookies


"""This function takes in a date and an array of cookies, then returns a 
new array of cookie ids whos dates match the date parameter"""


def get_all_cookies_for_selected_date(date, cookieArray):
    newArry = []
    for cookie in cookieArray:
        if cookie.date == date:
            newArry.append(cookie.id)
    return newArry


"""This function sorts an array of cookie ids from most commonly occuring to 
least commonly occuring, also gets rid of duplicates"""


def sort_most_active(cookieArry):
    res = sorted(cookieArry, key=cookieArry.count, reverse=True)
    # now take sorted list and remove duplicates
    noDups = []
    [noDups.append(cookieId) for cookieId in res if cookieId not in noDups]
    return noDups
