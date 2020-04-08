def display_all(x):
    lKeys = list(x.keys())
    lValue = list(x.values())
    cpt = 0

    for i in lValue:
        str_type = str(type(i))
        str_type = str_type.replace("<class '", "")
        str_type = str_type.replace("'>", "")
        print(lKeys[cpt] + "->(" + str_type + ": " + str(i) + ")")
        cpt += 1


display_all({"a": 1, "b": 2})
