import argparse
import cookie_class
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
    if args.date:
        return args.date
    print("Please enter a date, so that i may find the most active cookies")
    return False


def read_cookie_log(filename):
