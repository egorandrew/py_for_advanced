timur = input()
ruslan = input()
result = {
    "камень": {"камень", "ножницы"},
    "ножницы": {"ножницы", "бумага"},
    "бумага": {"бумага", "камень"}}

if ruslan == timur:
    print("ничья")
else:
    for key, value in result.items():
        if value == {timur, ruslan}:
            print("Тимур") if key == timur else print("Руслан")
