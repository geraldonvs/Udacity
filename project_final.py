# this is my mab libs code

phrase = "You can define functions to provide the required functionality. Here are simple rules to define a function in Python. Function blocks begin with the keyword _1_ followed by the function _2_ and parentheses ( ). Any _3_ parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses. The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return _4_."

busca = ["_1_","_2_","_3_","_4_"]                                   #questions
respostas = ["def", "name", "inputs", "nome"]               #answers


listphrase = phrase.split()

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    print "In this game you will have 5x chances to get 4 questions right"
    print "So here is the phrase you for you to answer the 4 questions:"
    print ml_string
    ml_string = ml_string.split()
    i=0
    lifes = 5

    for word in ml_string:

        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("What`s the answer for: " + replacement + " ")
            while user_input != respostas[i]:
                lifes -= 1
                if lifes == 0:
                    return
                user_input = raw_input("try again, what`s the answer for: " + replacement + " ")

            word = word.replace(replacement, user_input)
            replaced.append(word)
            i +=1

        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(phrase, busca)

