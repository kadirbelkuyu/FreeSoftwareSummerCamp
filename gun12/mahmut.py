def kabuk(function):
    def wrapper(*args, **kwargs):
        print("girdiler: ", args)
        new_args = (14,)
        sonuc = function(*new_args, **kwargs)
        print("Gerçek sonuç: ", sonuc)
        return 0

    return wrapper()
