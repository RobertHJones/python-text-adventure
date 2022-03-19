import time # to be able to add a pause

# user answers
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
yes_no = ["yes", "no"]


# take in the player's name
username = input('You look up from the empty glass to see the bartender scowling at you. "What did you say your name was again?" he growls \n')
print('"' + '...' + username + '"' + " you mutter bitterly \n")
# intro section
print('"Oh yeah? Well ' + username + ' my friend" (the sarcasm in his voice is palpable), "I was just wondering if you have the cash to actually pay for all those drinks?')
def intro():
    answer = input('"Do you have the cash?" (Y/N) \n')
    if answer in yes:
        option_pay()
    elif answer in no:
        option_nopay()
    else:
        print('"What was that boy? Am I gonna have to whoop your ass?"')
        intro()

# story branches        

def option_pay():
    print("The bartender gives you a vacant stare as you hand over the last of your meagre supply of cash. You ease yourself off the bar stool and stagger drunkenly to the exit. As you leave the dingy bar, the sun stings your squinting eyes and you realise that it's still early in the afternoon. Your thoughts unwillingly turn towards the events of last week and sighing heavily you feel an invisible weight being placed on top your shoulders. You barely hear the screeching tyres, and then everything fades to darkness...")
    time.sleep(5)
    answer = ""
    turn = ""
    while answer not in yes:
        answer = input('Open your eyes? (Y/N) \n')
        if answer in yes:
           print("You cautiously open your eyes and find yourself lying in a bed in what appears to be a hospital ward. As your sight returns the sounds in the room also come back into focus, and you become aware of the stifled groans of an old man in the bed next to you. You turn your head to look at him, but as you try to move you feel a shooting pain through your entire body.")
           turn = input("Turn your head anyway? (Y/N) \n")
           if turn in yes:
               option_hospescape()
           else:
               print("You are content to lie still in the bed. However this means the end of your adventure for now as you convalesce. Goodbye " + username + ". (GAME OVER)")
               quit()
        else:
            print("You allow yourself to rest for a few more moments")
            time.sleep(2)
    option_pay()   


def option_nopay():
    print('"Bad"')
    option_nopay()
intro()                
