



def print_menu():
    print("""
    [1] - vypis polozky
    [2] - vyhledej polozku
    [3] - pridej polozku
    [4] - smaz polozky
    [5] - nahrad' polozku
    [6] - konec
        """)

def search_item(db):
    item_n = input("Zadej jmeno kterou chces najit: ")

    for item_n in db:
        if item_n["name"] == name:
            return True
    return False
def add_item(db):
    name = input("Zadej jmeno knizky: ")
    author = input("Zadej jmeno authora: ")

    db.append({"name":name, "author": author})

def print_items(db):
    print("Aktualni seznam knizek")
    for item in db:
        print(f"jmeno:{item['name']}, author: {item['author']}")
    print("-------------------------")
    print()


def del_item():
   name = input("Zadej nazev knihy jakou chces smazat: ")




def replace_item():
    name = input("Zadej nazev knihy jakou chces updatnout autora: ")
    # vylepseni o ruznej update, name, author...

    update_index = None
    for i in range (len(db)):
        if db[i]["name"] == name:
            update_index = i
        if update_index is None:
            print("kniha se nenasla")
            return False
    author = input("Zadej authora knihy jakou chces updatnout: ")


def get_input():
    return int(input("Zadej volbu: "))
def run():
    db = [{"name": "hamlet", "author": "shakespeare"},
          {"name": "harry potter", "author": "jk rowling"}]
    #ukazka
    db2 = {"adam": 198,
           "tom": 206}
    print("Vitej v programu")

    while True:
        print_menu()
        user_choice = get_input()

        if user_choice == 1:
            print_items(db)

        elif user_choice == 2:
            add_item(db)

        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            pass
        elif user_choice == 6:
            pass

        else:
            print("Zadal jsi neplatnou volbu")

run()

print ("added changes")

print("nnnn")