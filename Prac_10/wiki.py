import wikipedia

def main():
    search_phrase = input('\nWhat do you want to search wikipedia for: ')
    while search_phrase != '':
        try:
            page = wikipedia.page(search_phrase)
            show_page(page)
        except wikipedia.DisambiguationError as e:
            disambig_handler(e)
        except wikipedia.PageError:
            print("Page doesn't seem to exist. Try something else")
        search_phrase = input('What do you want to search wikipedia for: ')


def disambig_handler(options):
    print('Why what??. Not sure what you meant.')
    print(options)


def show_page(page):
    print(page.title)
    print(page.url)
    print(page.summary)

main()
