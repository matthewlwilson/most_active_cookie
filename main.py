import functions


def main():
    arg = functions.get_args()
    filename = functions.get_cookie_filename(arg)
    DateToSearch = functions.get_search_date(arg)
    functions.read_cookie_log(filename)


if __name__ == '__main__':
    main()
