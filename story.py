import time # to be able to add a pause

# user answers
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]
yes_no = ["yes", "no"]


# take in the player's name
username = input('You look up from the empty glass to see the bartender scowling at you. "What did you say your name was again?" he growls \n')
print('"' + '...' + username + '"' + " you mutter bitterly \n")
# intro section
print('"Oh yeah? Well ' + username + ' my friend" (the sarcasm in his voice is palpable), "I was just wondering if you have the cash to actually pay for all those drinks?')
def intro():
    answer = input(" 'Do you have the cash?' (Y/N) \n")
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
    time.sleep(4)
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
    
def option_hospescape():
    print("As you look over at the emaciated, almost corpse-like frame of the old man, his gaze turns to meet yours. One glance at his milky eyeballs tells you that this man is blind, and yet as you face him a grating cackle emerges from his toothless mouth. 'Hey boy', he wheezes, 'when you fall asleep I'm gonna gut you.' He reaches under his pillow and pulls out a rusty scalpel. 'Stole this from a doctor when they took my sight away, I did'.")
    print("He lets out another unpleasant laugh as you turn away from him uneasily.")
    answer = input("Later on that evening you find yourself growing sleepy, but the old man's words echo inside your head. Allow yourself to fall asleep? (Y/N) \n")
    if answer in no:
        option_escape()
    elif answer in yes:
        print("You can't believe that the crazy blind old man could actually harm you and you close your eyes wearily. Moments later you feel a sharp pain shooting through your chest - you look up to see the old man bending over you with his scalpel. You just have time to meet his dead eyes before he pierces your throat. I'm afraid he killed you " + username + ". (GAME OVER)")
        quit()

def option_escape():
    print("Wary of the guileless sincerity you sensed from the deranged old man, you try to force yourself from the hospital bed.")
    print("As your legs touch the floor, they crumple on impact and you unceremoniously collapse in a heap. Your body is wracked by excruitiating agony, but you recall the old man and his scalpel, and force yourself to your feet.")
    answer = input("You manage to reach the window and find it slightly ajar. Pushing it open further, you see a long drop down to the ground below. Do you A - try to climb out the window? B - Go back to get your bedsheets to tie it up and use it to climb down? Or C - try to find another way to escape?")
    if answer in answer_A:
        print("You carefully lower yourself out of the open window, making sure to play your feet on the ledge below. Unfortunately your legs buckle and you fall to your doom. Goodbye " + username + ". (GAME OVER)")
    elif answer in answer_B:
        print("You turn around and creep back to your bed, gather up the bedsheets and tie them together. Attaching one end securely to the window handle you begin to make your descent.")
def option_nopay():
    print("The bartender is silent for a few moments, before exploding with rage. 'Are you serious?' he yells in your face, his deranged bloodshot eyes rolling back into his head. 'Right, that's it - Marge, call the boys!' he turns and shouts through an open doorway behind him. A short globular woman with a weary expression waddles out of this door. 'What boys?' she asks the bartender (who is presumably her husband). He immediately rounds on her 'Goddammit Marge, we've been over this!' he starts... ")
    answer = input("Do you A - Use the distraction to quietly sneak out, B - Smash the bartender over the head with a nearby bottle? Or C - Wait patiently for him to finish his argument. (A/B/C) \n")
    if answer in answer_A:
        print("escape!")
    option_nopay()
intro()                
