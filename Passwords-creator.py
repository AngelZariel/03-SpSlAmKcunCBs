# {Variables initialization}
passwords = open('Passes.txt', 'w', encoding='UTF-8')
character_circle_1 = 0
character_circle_2 = 0
character_circle_3 = 0
character_circle_4 = 0
character_circle_5 = 0
character_circle_6 = 0
character_circle_7 = 0
character_circle_8 = 0
counter = 0
file_part = 0
password = []
letters = ["a", "b", "c",
           "d", "e", "f",
           "g", "h", "i",
           "j", "k", "l",
           "m", "n", "o",
           "p", "q", "r",
           "s", "t", "u",
           "v", "w", "x",
           "y", "z", "A",
           "B", "C", "D",
           "E", "F", "G",
           "H", "I", "G",
           "K", "L", "M",
           "n", "O", "P",
           "Q", "R", "S",
           "T", "U", "V",
           "W", "X", "Y",
           "Z", "1", "2",
           "3", "4", "5",
           "6", "7", "8",
           "9", "0", "@",
           "#", "*", "!"]

# {Main program circle}
while character_circle_1 < 65:
    # {Main form}
    example_password = letters[character_circle_1] \
                       + letters[character_circle_2] \
                       + letters[character_circle_3] \
                       + letters[character_circle_4] \
                       + letters[character_circle_5] \
                       + letters[character_circle_6] \
                       + letters[character_circle_7] \
                       + letters[character_circle_8] \
                       + '\n'
    passwords.writelines(example_password)
    character_circle_8 += 1
    counter += 0.5
    # -----------------------------------------------------------
    # {Creating new .txt file when generated 20mln combinations}
    if counter == 10000000:
        file_part += 1
        file_name = 'Password part ' + str(file_part) + '.txt'
        passwords.close()
        passwords = open(file_name, 'w', encoding='UTF-8')
        counter = 0
    # -----------------------------------------------------------
    if character_circle_8 == 65:
        character_circle_8 = 0
        character_circle_7 += 1
        if character_circle_7 == 65:
            character_circle_7 = 0
            character_circle_6 += 1
            if character_circle_6 == 65:
                character_circle_6 = 0
                character_circle_5 += 1
                if character_circle_5 == 65:
                    character_circle_5 = 0
                    character_circle_4 += 1
                    if character_circle_4 == 65:
                        character_circle_4 = 0
                        character_circle_3 += 1
                        if character_circle_3 == 65:
                            character_circle_3 = 0
                            character_circle_2 += 1
                            if character_circle_2 == 65:
                                character_circle_2 = 0
                                character_circle_1 += 1
                                if character_circle_1 == 65:
                                    passwords.close()
                                    break
# ------------------------------------------------------------
# By Dolor 23.04.2022
# https://github.com/AngelZariel/
# ------------------------------------------------------------
