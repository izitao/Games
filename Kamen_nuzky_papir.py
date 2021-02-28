import random

symbols = ["kamen", "nuzky", "papir"]
exit_tags = ['quit', 'q', 'STOP', 'stop', 'exit', 'no', 'No']

pc_points = 0
user_points = 0

rounds = 0
active = True

while active:
    active_2 = True

    while rounds <=0:s
        try:
            rounds = input('Pocet kol: ')
            if rounds in exit_tags:
                active_2 = False
                active = False
                break
            else:
                rounds = int(rounds)
        except ValueError:
            print('Pocet kol musi byt alespon 1.')
            rounds = 0

    actual_round = 0

    while active_2 and actual_round < rounds :
        print(f'\n{actual_round+1}.kolo')
        pc_choice = random.randint(0, len(symbols) - 1)
        user_choice = -1
        while user_choice == -1:
            user_choice = input('Zadej symbol ("1=kamen", "2=nuzky", "3=papir"): ')
            try:
                if user_choice in exit_tags:
                    active_2 = False
                    active = False
                    break
                else:
                    user_choice = int(user_choice) - 1
            except ValueError:
                print('Byl zadan neplatny symbol.')
                user_choice = -1

        if active_2 and (user_choice - pc_choice == -1 or user_choice - pc_choice == 2):
            print('Vyhral jsi!\n')
            user_points += 1
            actual_round += 1
        elif active_2 and (user_choice - pc_choice == 1 or user_choice - pc_choice == -2):
            print('Prohral jsi!\n')
            pc_points += 1
            actual_round += 1
        elif active_2 and (user_choice - pc_choice == 0):
            print('Remiza\n')
            actual_round += 1

        if active_2:
            print(f'Uzivatel hral: {symbols[user_choice].upper()}, souper hral: {symbols[pc_choice].upper()}.')
            print(f'Body uzivetele: {user_points}, body soupere: {pc_points}.')

    if user_points > pc_points and active_2:
        print('Vyhral jsi!\n')
    elif user_points < pc_points and active_2:
        print('Prohral jsi!\n')
    elif user_points == pc_points and active_2:
        print('Remiza!\n')

    if active_2:
        new_game = input('Nova hra? ')
        if new_game in exit_tags:
            active = False
        else:
            actual_round = 0
            rounds = 0
            pc_points = 0
            user_points = 0


