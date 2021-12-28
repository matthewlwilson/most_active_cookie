import functions


def main():
    arg = functions.get_args()
    filename = functions.get_cookie_filename(arg)
    dateToSearch = functions.get_search_date(arg)
    arryOfCookies = functions.read_cookie_log(filename)
    newArry = functions.get_all_cookies_for_selected_date(
        dateToSearch, arryOfCookies)
    mostActiveCookies = functions.sort_most_active(newArry)
    functions.display_most_active(mostActiveCookies)


if __name__ == '__main__':
    main()
