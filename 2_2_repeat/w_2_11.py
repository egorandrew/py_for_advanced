word = input() + " запретил букву"
for i in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
    if i in word:
        print(word, i, sep=" ")
        word = word.replace(i, "")
        word = " ".join(word.split())
