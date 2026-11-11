from builtins import KeyError

while True:
    try:
        import random

        moves = ['камень', 'ножницы', 'бумага']
        bot = random.choice(moves)
        player = input("Ваш ход: ")
        print("Компьютер:", bot)
        wins = {"камень": "ножницы",
                "ножницы": "бумага",
                "бумага": "камень"}
        if player == bot:
            print("Ничья")
        elif wins[player] == bot:
            print("Ты победил")
        else:
            print("Вы проиграли")
    except KeyError:
        print("Неверный текст")