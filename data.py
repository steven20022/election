def read_data(file_name):
    data = open(file_name)
    result = []
    data.readline()
    for row in data.readlines():
        row = row.split(',')
        result.append(tuple([row[0], int(row[1]), row[2].strip()]))
    data.close()
    return result


def state(elem):
    return elem[0]


def votes(elem):
    return elem[1]


def lean(elem):
    return elem[2]


def format_State(file_name):
    results = read_data(file_name)
    results.sort(key=state)
    return results


def format_Vote(file_name):
    results = read_data(file_name)
    results.sort(key=votes)
    return results


def format_Lean(file_name):
    results = read_data(file_name)
    results.sort(key=lean)
    return results


def list_Democratic(file_name):
    results = format_Lean(file_name)
    democratic = []
    for i in range(0, len(results)):
        if results[i].__contains__('B'):
            democratic.append(results[i])
    return democratic


def list_Republican(file_name):
    results = format_Lean(file_name)
    republican = []
    for i in range(0, len(results)):
        if results[i].__contains__('R'):
            republican.append(results[i])
    return republican


def list_Swing(file_name):
    results = format_Lean(file_name)
    swing = []
    for i in range(0, len(results)):
        if results[i].__contains__('P'):
            swing.append(results[i])
    return swing


def Blue_Votes(file_name):
    data = list_Democratic(file_name)
    votes = 0
    for i in data:
        votes += int(i[1])
    return votes


def Red_Votes(file_name):
    data = list_Republican(file_name)
    votes = 0
    for i in data:
        votes += int(i[1])
    return votes


def Swing_Votes(file_name):
    data = list_Swing(file_name)
    votes = 0
    for i in data:
        votes += int(i[1])
    return votes


swing = Swing_Votes("data.txt")
red = Red_Votes("data.txt")
blue = Blue_Votes("data.txt")


def Move_States(file_name, state, color1, color2):
    s = list_Swing(file_name)

    global swing, red, blue

    if color1 == "swing":

        if color2 == "swing":
            for i in s:
                if i[0] == state:
                    swing -= i[1]
                    swing += i[1]

        if color2 == "red":
            for i in s:
                if i[0] == state:
                    swing -= i[1]
                    red += i[1]

        if color2 == "blue":
            for i in s:
                if i[0] == state:
                    swing -= i[1]
                    blue += i[1]

    if color1 == "blue":

        if color2 == "swing":
            for i in s:
                if i[0] == state:
                    blue -= i[1]
                    swing += i[1]

        if color2 == "red":
            for i in s:
                if i[0] == state:
                    blue -= i[1]
                    red += i[1]

        if color2 == "blue":
            for i in s:
                if i[0] == state:
                    blue -= i[1]
                    blue += i[1]

    if color1 == "red":

        if color2 == "swing":
            for i in s:
                if i[0] == state:
                    red -= i[1]
                    swing += i[1]

        if color2 == "red":
            for i in s:
                if i[0] == state:
                    red -= i[1]
                    red += i[1]

        if color2 == "blue":
            for i in s:
                if i[0] == state:
                    red -= i[1]
                    blue += i[1]

