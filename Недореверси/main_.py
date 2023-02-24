from board_position import BoardPosition


n = input("Ведите число больше 1, оно будет строить поле с задаными вами сторонами: ").strip()
if n.isdigit() and int(n) > 1:
    word = input("ваша цель закрасить все поля своим цветом, "

                 "тогда игра закончится, цвет вы должны выбрать между собой,"
                 " вы готовы начать игру? Напишите ДА ").upper()
    if word == "ДА":
        BoardPosition(int(n), int(n))
    else:
        while word != "ДА":
            if word != "ДА":
                word = input("А сейчас вы готовы ?").upper()
            if word == "ДА":
                BoardPosition(int(n), int(n))
else:
    print("Неправильный формат ввода")
