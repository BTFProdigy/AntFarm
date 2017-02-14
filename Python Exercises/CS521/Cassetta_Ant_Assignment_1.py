from random import randint
from time import sleep

nouns = ['CAT', 'DOG', 'FISH', 'PANGOLIN']
verbs = ['RAN','CUT','BOOGIE','SPUN', 'WIGGLE','WOBBLE' ]
adj = ['VERACIOUS','SLIMY','COURAGEOUS', 'WHIMPY', 'DEBONAIR', 'MYSTERIOUS', 'DARK']
sentences = ['The _n_ quickly _v_ up the stairs, it looked very _a_!',
             'While the little _n_ was _v_ she was amazed to find a _a_ turtle!',
             'The _a_ _n_ was practicing _v_ so hard they fell over!']
master = [nouns, verbs, adj, sentences]
madlibs = []

play_again = 'y'
#Encapsulate the whole program into while playagain == 'y':

while play_again == 'y' or play_again == 'yes':

    plyr_num = input('Please give me a number between 0 and 7: ')
    plyr_num = int(float(plyr_num))

    while plyr_num < 0 or plyr_num > 7:
        if plyr_num <0:
            try_again = input("To small! The number must be a positive integer between 0 - 7. Please try again: ")
            plyr_num = int(float(try_again))
        elif plyr_num > 7:
            try_again = input("To big! The number must be a positive integer between 0 - 7. Please try again: ")
            plyr_num = int(float(try_again))

    print("\nGreat! Let's use: " + str(plyr_num))

    if plyr_num > len(nouns)-1:
        rand_noun = randint((plyr_num % 2), len(nouns)- 1)
    else:
        rand_noun = randint(plyr_num, len(nouns)-1)

    if plyr_num > len(verbs)-1:
        rand_verb = randint(plyr_num % 2, len(verbs)-1)
    else:
        rand_verb = randint(plyr_num, len(verbs)-1)

    if plyr_num > len(adj)-1:
        rand_adj = randint(plyr_num % 2, len(adj)-1)
    else:
        rand_adj = randint(plyr_num, len(adj)-1)

    if plyr_num > len(sentences)-1:
        rand_sentence = randint(plyr_num % 2, len(sentences)-1)
    else:
        rand_sentence = randint(plyr_num, len(sentences)-1)

    #print(rand_noun, rand_verb, rand_adj, rand_sentence)
    print('Generating your sentence...')
    sleep(0.75)
    new_madlib = sentences[rand_sentence].replace('_n_', nouns[rand_noun]).replace('_v_', verbs[rand_verb]).replace('_a_', adj[rand_adj])
    print('\n' + new_madlib)

    if new_madlib in madlibs:
        print("\nWe already have that one. This mad lib will not be stored. Try again!")
    else:
        print("\nOh, that's a new arrangement! We will save this one.\n")
        madlibs.append(str(new_madlib))

    for item in madlibs:
        print(item)

    print("\nDo you want to play again? ('y' or 'n')")
    play_again = input().lower()