def my_args_handler(*args):
    max_args = len(args)
    strg = ""
    compteur = 1

    for i in args:
        if compteur < max_args:
            strg += i + ','
        else:
            strg += i
        compteur += 1

    return strg
