timur = input()
ruslan = input()
result = {
    "камень": {"ножницы", "ящерица"},
    "ножницы": {"ящерица", "бумага"},
    "бумага": {"Спок", "камень"},
    "ящерица": {"бумага", "Спок"},
    "Спок": {"ножницы", "камень"}}

if ruslan == timur:
    print("ничья")
else:
    print("Тимур") if ruslan in result[timur] else print("Руслан")
