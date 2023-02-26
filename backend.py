ABSOLUTE_PATH = "/home/robert/pyCourse/newWebApp/items.txt"


def getItems():
    try:
        with open(ABSOLUTE_PATH, 'r') as file:
            items = [item.rstrip() for item in file]
    except:
        with open(ABSOLUTE_PATH, 'w') as file:
            items = []
    return items

def writeItems(items):
    with open(ABSOLUTE_PATH, 'w') as file:
        file.write('\n'.join(items))

