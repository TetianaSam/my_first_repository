



def print_menu():
    print("""
    [1] - vypis polozky
    [1] - vyhledej polozku
    [1] - pridej polozku
    [1] - smaz polozky
    [1] - nahrad' polozky
    [1] - konec
        """)

def search_item():
    pass
def add_item():
    pass
def print_items():
    pass
def del_item():
    pass
def replace_item():
    pass
def get_input():



def run():
    db = [{"name": "hamlet", "author": "shakespeare"},
          {"name": "harry potter", "author": "jk rowling"}]
    #ukazka
    db2 = {"adam": 198,
           "tom": 206}
    print("Vitej v programu")

    while True:
        print_menu()
        user_choise = get_input()

        if user_choise == 1:
            pass
        elif user_choise == 2:
            pass
        elif user_choise == 3:
            pass
        elif user_choise == 4:
            pass
        elif user_choise == 5:
            pass
        elif user_choise == 6:
            pass

        else:
            print("Zadal jsi neplatnou volbu")

run()
