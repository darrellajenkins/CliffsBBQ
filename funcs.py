
clr = "\033[39m\033[0m"
bold = "\033[1m"
blk = "\033[30m"
italic = "\033[3m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"


def my_datetime():
    import time
    my_date = time.strftime('%A, %B %d, %Y')
    my_time = time.strftime('%I:%M:%S %p')
    return my_date, my_time


def display_time():
    while True:
        t = my_datetime()
        print(f'{t[0]} {t[1]}', end='\r')


def search():
    import webbrowser
    query_again = input("Input your query: ")
    webbrowser.open("https://duckduckgo.com/search?q=" + query_again)