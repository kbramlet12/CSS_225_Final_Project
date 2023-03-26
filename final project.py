def print_notebook_display(notebook_entries):
    if(not notebook_entries):
        print("(----------------------------------)")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print(" |                                |")
        print("(----------------------------------)")
    else:
        print("----------------------------------")
        for entry in notebook_entries:
            print(f"{entry}")
        print("----------------------------------")


def game_opening():
    print("*Police Sirens* 'Hello Dispatch?, We're going to need a coroner and some backup.. Looks like a homicide.. I see lacerations on the victim and signs of a struggle.. ")
    print("I can also see shoe prints leading into the woods, our suspect may still be out there on foot.. We have a couple of witnesses here who say they've caught a glimpse of ")
    print("who the perpetrator is but one of them seems to be rather shaken up by the experience.. Get here as fast as possible over and out.\n")


def character_creation():
    print("*You step out of a police cruiser and begin walking towards the scene of the crime, a younger man in uniform approaches you as you come near*")
    return input("What's your name detective?: (Last name preferred) ")


def game_commence(name):
    print(f"\nWell Detective {name}, I'm going to give you a brief rundown of the situation and then I'm going to let you take point. We've got a homicide that occurred here not too long ago.")
    print("We haven't narrowed down the exact timeline of events so that still needs to be established. Furthermore, while it looks like a sharp object was used on the victim we haven't been able to locate the murder weapon.")
    print("We discovered some shoe prints next to the victim and it looks like they lead into the forest down there. But I wouldn't go down there by yourself, especially if he's still running around in there.\n")
    print("(At certain points in the game, you will be prompted with a list of responses that you can give to certain characters. Indicate which response to select by entering the number associated with each)")
    reply = input(
        "1). Shouldn't we have officers in the woods looking for the killer right now?\n2). Where should I start with my investigation?\n")
    while(reply != "1" and reply != "2"):
        reply = input(
            "'Say again? I didn't quite catch that..' (For this response, please select either 1 or 2):\n")
    if(reply == "1"):
        print("\n*The officer gives a look of impatience, a look that could be interpretted as either 'I wish I wasn't stationed here.' or 'Damn city folk.'*")
        print("'Small town, small budget.'")
        reply = input("1). Really?\n2). Understood\n")
        while(reply != "1" and reply != "2"):
            break
        while(reply == "1"):
            print("\n'Really..'")
            reply = input("1). Really?\n2). Understood\n")
    print("\nI would suggest getting a better look at the body, we've only glanced at it superficially so there may still be something that we haven't discovered about it yet.")
    print("You can also talk to the two witnesses up on the hill just 15 meters that way. One of them seems to be experiencing shock from the event so handle with caution.")
    print("Finally.. There is the woods.. But I wouldn't go in there without backup and I'll tell you right now it's not going to be me.\n")
    reply = input("1). You won't even go into the woods to help investigate let alone potentially apprehend a suspect? Are you even a cop?\n2.) (Start Investigation).\n")
    while(reply != "1" and reply != "2"):
        print(
            f"'Sorry, haven some trouble hearing you there detective {name}. Say again?")
    if(reply == "1"):
        print(
            f"\n*His gaze remains on the forest in the distance with a neutral expression* 'Tell you what Detective {name}, when you return to the city and convince them to increase ")
        print("the budget for police funding for our rural town of Salem, I'll follow you everywhere. Even into the goddamn sewer.'")
        print("*You can tell that the officer wishes he wasn't stationed here.. He didn't have a choice*\n")


def investigation(name):
    notebook_entries = []
    inspected_body = False
    gained_follower = 0
    survived_woods = False
    alive = True
    print(
        f"\n(The investigation portion will now commence Detective {name}, choose from the following selection where you want to go.)")
    choice = input(
        "1). Inspect the body\n2). Question witnesses\n3). Enter the woods\n")
    while(choice != "1" and choice != "2" and choice != "3"):
        print("(Please choose from either 1-3)")
        choice = input(
            "1). Inspect the body\n2). Question witnesses\n3). Enter the woods\n")
    while True:
        if(not alive):
            print(
                "*Darkness overtakes you.. Nothing but darkness.. This is the end of your investigation..*")
            print("Game Over")
            break
        elif(choice == "1"):
            if(not inspected_body):
                inspected_body = inspect_body(notebook_entries)
            else:
                print("*You feel there's nothing more to gain from inspecting the body*")
        elif(choice == "2"):
            if(not gained_follower):
                gained_follower = question_witnesses(name, notebook_entries)
            else:
                print(
                    "*You feel you've bothered the witnesses with enough questions for one night.*")
        elif(choice == "3"):
            if(not survived_woods):
                survived_woods = enter_woods(
                    gained_follower, name, notebook_entries)
                alive = survived_woods
                if(not alive):
                    continue
            else:
                print(
                    "\n*You decide that you may have missed something and decide to go looking on your own this time*")
                print("*You trace the footprints into the forest, deeper and deeper..*")
                print("*Deeper and deeper....*")
                print("*Deeper and deeper............*")
                print("*Deeper and deeper.........................*")
                alive = False
                continue
        elif(choice == "4" and (inspected_body or gained_follower or survived_woods)):
            print_notebook_display(notebook_entries)
        elif(choice == "5" and (inspected_body or gained_follower or survived_woods)):
            print("\n*You believe you have enough information to make an accurate guess as to who was the murderer of this crime.*")
            who_done_it = input(
                f"*Well Detective {name}, who do you think committed the crime?*\n")
            if(who_done_it.lower() == "johnson" and survived_woods):
                print(
                    "\n*You pull out the shiny object from your overcoat knowing full-well what it really is*")
                print(
                    "*You walk up to officer Johnson, the man who greeted you when you first got here*\n")
                input(
                    "1). Is this your badge officer?\n2). Looks like you'll be going away for a long time.\n")
                print("\n*The officer doesn't respond and remains as still as stone, even as you slap the handcuffs on him and drive him away in your cruiser.*")
                print(f"*Congratulations Detective {name}, You Win!")
                break
            else:
                print("\n*You guess a name, but that's all it is. Just a guess*")
                print(
                    "*Without any leads or any solid evidence you're at a loss as to what to do.*")
                print("*You realize there's nothing you can do to help solve the murder of the young woman. Whatever happened tonight will forever remain a mystery.*")
                print("*Game Over*")
                break
        else:
            print("(Please choose from either 1-5)")
            choice = input(
                "1). Inspect the body\n2). Question witnesses\n3). Enter the woods\n4). Display Notebook\n5). Conclude Investigation\n")
        choice = input(
            "1). Inspect the body\n2). Question witnesses\n3). Enter the woods\n4). Display Notebook\n5). Conclude Investigation\n")


def inspect_body(notebook_entries):
    finish_inspection = False
    additional_features = [False, False, False]
    check_pockets = False
    inspect_blood_spatter = False
    check_ground = False
    print("\nYou walk up to the body of the victim. Features become more apparent and you can already decipher several facts: Adult, Black hair, Female.")
    print("The color of the skin is pale, no signs of decomposition just yet. This homicide is very recent, you can't help but wonder just how recent..")
    print("You notice blood spatter drops accross the body, on the shirt and jeans.")
    print("you produce a face mask to keep from coughing or sneezing on the blood. It could still be valuable during lab analysis.")
    print("You also begin putting on a pair of gloves. You're ready for further inspection.\n")
    choice = input(
        "1). Inspect for additional features\n2). Check pockets\n3). Inspect blood spatter pattern\n4). Check ground near the victim\n5). Display Notebook\n")
    while(choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"):
        print("(Please choose 1-5)\n")
        choice = input(
            "1). Inspect for additional features\n2). Check pockets\n3). Inspect blood spatter pattern\n4). Check ground near the victim\n5). Display Notebook\n")
    while(finish_inspection != True):
        if(choice == "1"):
            if(additional_features[0] != True):
                print(
                    "\nThe body seems to be about 5'6, body weight could be estimated to be 90 to 120lbs\n")
                additional_features[0] = True
            elif(additional_features[1] != True):
                print("\nThe jeans of the victim are not blue, they're more of a darker color. You can make out the white lettering on the black shirt.")
                print("It reads: 'Asking Alexandria'\n")
                additional_features[1] = True
            elif(additional_features[2] != True):
                print(
                    "\nYou look closer at the victim's hands. Black nail polish, but something else sticks out to you.")
                print(
                    "You notice bruising and brackish colors on the knuckles. The victim fought back while she was being attacked.")
                print("Signs of a struggle.\n")
                additional_features[2] = True
                notebook_entries.append(
                    "Victim has brusing on the knuckles showing signs of struggle.")
            else:
                print(
                    "\nIt seems there are no more additional features to be gleemed from the victim.\n")
        elif(choice == "2"):
            if(check_pockets != True):
                print("\nWith your gloves you check the pockets of the victim. You pull out a wallet that contains a driver's license. The picture on the license shows a smiling face")
                print("full of color and blonde hair. The image sharply contrasts with the dead body before you. The name on the license displays 'Miranda Douglass', DOB: 07-12-98.")
                print("Her age was 23.\n")
                check_pockets = True
            else:
                print("\nThere's nothing else of interest inside the pockets.\n")
        elif(choice == "3"):
            if(inspect_blood_spatter != True):
                print("\nAfter inspection of the blood spatter on the victim's clothing, you notice that these are droplets.. If the victim had lacerations suggesting a sharp object ")
                print("then why would there be additional droplets on the victim's body? You would expect streak patterns, indicating a sweeping motion of the blade, not droplets.")
                print(
                    "You don't want to assume anything, not without an official analysis, but this may not be the victim's blood.\n")
                notebook_entries.append(
                    "Abnormal blood spatter pattern found on victim may not belong to the victim.")
                inspect_blood_spatter = True
            else:
                print("\nThe blood spatter remains the same. Droplets, not streaks.\n")
        elif(choice == "4"):
            if(check_ground != True):
                print("\nThe ground surrounding the victim seems to be soaked in crimson mixed with the brown of the soil, creating a dark brackish color.")
                print("You also notice the shoe prints near the victim. Judging from the sole, you could say the shoe size was 10.5, the average size for a male\n")
                notebook_entries.append(
                    "Shoe prints on the ground near victim indicate possibility of male gender.")
                check_ground = True
            else:
                print(
                    "\nDoesn't look like there is anything else of interest lying on the ground.\n")
        elif(choice == "5"):
            print_notebook_display(notebook_entries)
        choice = input(
            "1). Inspect for additional features\n2). Check pockets\n3). Inspect blood spatter pattern\n4). Check ground near the victim\n5). Display Notebook\n6). Finish Inspection\n")
        while(choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6"):
            print("(Please choose 1-6)\n")
            choice = input(
                "1). Inspect for additional features\n2). Check pockets\n3). Inspect blood spatter pattern\n4). Check ground near the victim\n5). Display Notebook\n6). Finish Inspection\n")
        if(choice == "6"):
            print(
                "\nYou step away from the body and begin evaluating your other options.")
            finish_inspection = True
    return True


def question_witnesses(name, notebook_entries):
    witness_will_follow = False
    print("\nYou approach the two witnesses, both are female, young adults. One avoids eye contact and shakes with little tremors, the other looks directly at you as you come forward.")
    print(
        f"You introduce yourself as detective {name} and the young woman who seems the most intact begins to speak: ")
    print("'We aren't going to answer anymore questions, I've already told the officer down there everything we know. We're going to file a complaint to the Salem Police Department.")
    print("If they can't even catch an active criminal hiding out in the woods then what are they good for anyway?'")
    print("*The more anxious young woman nervously glances at the officer down the hill when the other mentioned already telling him what happened previously*\n")
    response = input("1). I'm not an officer from Salem, I'm a detective from Selensky county and I just want to help.\n2). *Motion to the anxious witness* Excuse me miss, is something wrong?\n")
    while True:
        if(witness_will_follow):
            if(witness_will_follow == 1):
                return 1
            else:
                return False
        elif(response == "1"):
            witness_will_follow = question_witnesses_segment(
                name, notebook_entries)
        elif(response == "2"):
            print("\n*The more anxious witness looks away from you quickly and whimpers a little before the other steps in for her.*")
            print(
                "'If you're going to question someone then question me, she's been through enough already.'\n")
            response = input(
                "1). *Continue attempting to question the anxious witness*\n2). Understood, Well I'm a detective from Selensky county so I'm not affected by SPD bureaucracy.\n")
            if(response == "1"):
                print("\n*The anxious witness flinches at your aggressive attempts to question her, it begins to look more like an interrogation. The companion begins to look increasingly angry until she finally speaks up.*")
                print("'That's enough detective! We won't be harassed anymore tonight by the Salem Police! If you want more information you can speak to our attornies!")
                print(
                    "*They've shut down on you. There's nothing more to say here. With that, you back away from the witnesses.*")
                return False
            elif(response == "2"):
                witness_will_follow = question_witnesses_segment(
                    name, notebook_entries)
            else:
                print(
                    "\n*The confident witness looks visibly fed up* 'Look you can talk to our attornies, we're done talking!")
                print(
                    "*There's nothing more to gain here, you step away from the witnesses.*\n")
                return False
        else:
            print("\n*The witness looks at you strangely, it seems she didn't quite understand what you were trying to say*\n")
            response = input(
                "1). I'm not an officer from Salem, I'm a detective from Selensky county and I just want to help.\n2). *Motion to the anxious witness* Excuse me miss, is something wrong?\n")


def question_witnesses_segment(name, notebook_entries):
    response = question_witnesses_good_response()
    outcome = question_witnesses_continued_conversation(
        response, name)
    if(outcome == True):
        return -1
    else:
        witness_will_follow = question_witnesses_commence(
            outcome, notebook_entries)
        return witness_will_follow


def question_witnesses_good_response():
    print("\n*The woman breathes a sigh of relief* 'Thank god. In that case I'll do my best to help out, but only on one condition.'")
    print("*She begins to look serious as her friend continues to avoid any type of contact in contrast*. 'I'm going with you into the woods if that's where you're planning on going.")
    print("Take me with you and we'll look for any leads and even catch the guy if we run into him.'\n")
    response = input("1). No way, we can't have civilians putting their lives at risk if a murderer is on the loose.\n2). Very well, if I go into the forest you'll be coming with me.\n")
    return response


def question_witnesses_continued_conversation(response, name):
    while True:
        if(response == "1"):
            print(
                f"\n*A scowl appears accross the young woman's face as she begins to glare at you* 'Then good luck with your investigation detective {name}, if you need any information from us")
            print("you can talk to our attornies.' *The anxious companion next to her glances up for a quick brief moment before quickly looking back at the ground, you could swear you heard a silent")
            print("sad voice saying 'no'. With that, you back away from the witnesses*\n")
            return True
        elif(response == "2"):
            print("\n*A look of determination begins to form on her face, she's ready to help out any way she can.* 'Alright, ask me anything.'\n")
            response = input(
                "1). I heard from the other officer that you've caught a glimpse of the killer, can you describe any details?\n2). What time did you see the culprit?\n3). *Try questioning the other witness*\n4). Display Notebook\n")
            return response
        else:
            print(
                "\n*A look of impatience crosses the woman's face as she waits for a response*\n")
            response = input(
                "1). No way, we can't have civilians putting their lives at risk if a murderer is on the loose.\n2). Very well, if I go into the forest you'll be coming with me.\n")


def question_witnesses_commence(outcome, notebook_entries):
    blue_coat = False
    time_of_death = False
    saw_face = False
    while True:
        if(outcome == "1"):
            if(not blue_coat):
                print("\n'I remember seeing a someone in a blue coat I think.. There was something shiny that caught my eye.. I think it was on their coat.'\n")
                blue_coat = True
                notebook_entries.append(
                    "Witness account: I remember seeing someone in a blue coat, allegedly there was something shiny on their coat")
            else:
                print(
                    "\n'He was wearing a blue coat with something shiny on it.. That's all I remember.'\n")
        elif(outcome == "2"):
            if(not time_of_death):
                print("\n'It was at 7:00 PM, we just came back from work at 'Good Eats Diner'. That was when we heard someone screaming and I rushed over.'")
                print("*7:00 PM was just a little over 2 hours ago*\n")
                time_of_death = True
                notebook_entries.append(
                    "The murder took place 2 hours ago, very recently.")
            else:
                print("\n'It was 7:00 PM.. I'm sure of it..'\n")
        elif(outcome == "3"):
            if(not saw_face):
                print("\n*Very cautiously you turn towards the other witness. With a gentleness in your voice, you ask if she saw anything suspicious around the time of the murder.*")
                print("*She's still shaking, but it has lessened a bit, she begins opening her mouth slowly.. And she says something that you've heard too many times in your career..")
                print("Something that still makes the skin on your back crawl..*")
                print("'I saw his face..'")
                print(
                    "*After saying that she shuts down again.. There's nothing more to ask her*\n")
                saw_face = True
                notebook_entries.append(
                    "2nd Witness account: I saw his face. This confirms the perpetrator's gender was male.")
            else:
                print(
                    "\n*You got what you needed. You decide it would be better to give her some space*\n")
        elif(outcome == "4"):
            print_notebook_display(notebook_entries)
        elif(outcome == "5" and (blue_coat or time_of_death or saw_face)):
            print("\n'And remember.' *The witness with confidence looks directly at you* 'When you go into the woods, you take me with you.' *She turns to her companion and continues consoling her*")
            print("*And with that taken care of, you step away from the witnesses.. Before leaving however.. You take one last glance at the shaken young woman*")
            print("*You could've sworn you saw her take a sudden glance at something in the distance before looking back towards the ground. Her face looking incredibly pale*")
            print("*If you had to guess, she was glancing somewhere down the hill*\n")
            return True
        else:
            print("\n*You almost say something but you begin coughing. Probably for the best since you were at a loss for words anyway*\n")
        outcome = input("1). I heard from the other officer that you've caught a glimpse of the killer, can you describe any details?\n2). What time did you see the culprit?\n3). *Try questioning the other witness*\n4). Display Notebook\n5). End questioning\n")


def enter_woods(gained_follower, name, notebook_entries):
    while True:
        if(gained_follower == 1):
            print(gained_follower)
            print("\n*The witness you questioned previously begins coming down the hill towards you as you near the opening of the woods*")
            print("*She tells you briefly that she sent her friend home and that she couldn't take being questioned much more.. Understandably you don't press the issue*")
            print("*However, the officer that greeted you as you came onto the scene is making his way towards the both of you now.. It seems he's not very happy with the current circumstances*")
            print(
                f"*The officer begins to speak* 'Excuse me detective {name}, but what do you think you're doing with the witness?'")
            print("*Before you have a chance to respond the witness already has a retort at the ready* 'I know my rights officer! If I'm not being detained then you can back off!'")
            print("*The officer looks stunned for a second before regaining his composure. He continues the confrontation in a low, threatening voice* 'You still have questions that need to be answered about the crime that took place.")
            print("If you're unwilling to answer them then it doesn't paint you in a very good light you see..' *She responds to the threat with tenacity* 'I plead the 5th!")
            print(
                "If you want anymore answers you can talk to my attorney! Now am I being detained???'")
            print("*The officer, motionless.. Begins to glare at the young woman.. The look on his face becoming more and more intense as the moment passes*\n")
            response = input("1). Is there a problem here officer?\n2). ...\n")
            if(response == "1"):
                protect_follower(name, notebook_entries)
                return True
            else:
                print("\n*The officer begins to say something in a eerie, quiet voice* 'Actually, I think you will be detained.. For assaulting an officer of the law..'")
                print("*He motions to a spot on his face that you didn't see clearly before, due to the veil of nightime that surrounds all of you. But now you see it clear as day with his assistance*")
                print(
                    "*Scabbing and bruise marks show themseleves on his face with his helpful indication*")
                print(
                    "*The young woman looks to you with shock, her face is pleading with you to do something*\n")
                response = input(
                    "1). (Pull Rank) Don't worry, she'll be coming with me.\n2). ...\n")
                if(response == "1"):
                    protect_follower(name, notebook_entries)
                    return True
                else:
                    print("\n*Without saying a word the officer begins to put handcuffs on the witness. A look of betrayal is plastered on her face as she's escorted off the premises and into a nearby police cruiser*")
                    print(
                        "*You decide it wasn't worth the trouble of getting involved with the Salem Police Department and continue on into the woods*")
                    gained_follower = 0
        else:
            print("\n*You enter the woods.. You can't help but feel something is very wrong here.. You venture further in following the footsteps on the ground*")
            print("*The footprints are spaced out further as you follow them.. The perpetrator started running at some point*")
            print("*It seems like some time has passed.. The woods continue winding and the trees continue popping into view from every direction.. Yet you continue following the trail..*")
            print(
                "*You finally near the end of what seemed to be a seemingly infinite amount of footprints*")
            print("*You notice something shiny on the ground.. You bend over to get a better look.. You begin reading the letters on the object*")
            print("*It says 'Off'")
            return False


def protect_follower(name, notebook_entries):
    print("\n*The officer looks at you and seems ready to go off, but catches himself before saying something that could be detrimental to his career*")
    print(
        f"'Very well detective {name}, y'all have fun in the forest.. Try not to get stabbed to death with a pocket knife..'")
    print("*After the menacing warning, he steps away from the both of you and you continue your investigation into the forest*")
    print("*You follow the footsteps into the forest along with the witness.. You notice that as you continue walking the footsteps become more spread out..*")
    print("*The perpetrator started running at some point.*")
    print("*You reach the end of the trail and happen upon something particularly shiny on the ground.. You begin bending over to look at what seems to be lettering on the object..*")
    print("*It says 'Off' but scuff marks make it hard to read the rest.. There seems to be one final word on the shiny object before you tuck it away into your overcoat*")
    print("*The name reads 'Johnson'*")
    notebook_entries.append(
        "Found what appears to be a shiny object. It says 'Off' on top and the name just below it says 'Johnson'")
    print("*The witness looks to you for any indication of what you might think.. You merely nod your head to her.. and begin trekking out of the woods and back to the crime scene.*\n")


def main():
    name = ""
    game_opening()
    name = character_creation()
    game_commence(name)
    investigation(name)


main()
