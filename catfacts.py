import os

def catFactsTest(text,username,USERNAME):
        turingquestions = ["are you a bot?","are u a bot?","r u a bot?","are u a bot?","are you really a bot?", "are you a human?","r u a human?", "are you human?","are u a human?","are u human?","are you really human?","are you actually a human?"]
        catfacts = ["Thanks for signing up for Cat Facts! You now will receive fun daily facts about CATS! >o<","Cats use their tails for balance and have nearly 30 individual bones in them! <To cancel Daily Cat Facts, reply \'cancel\'>","Would you like to receive a Cat Fact every hour? <reply \'Tyxt33358dggyf\' to cancel>","Command not recognized. You have a <year> subscription to Cat Facts and will receive fun <hourly> updates!","In ancient Egypt killing a cat was a crime punishable by death. Thanks for choosing Cat Facts!","Command not recognized. Please answer the following to confirm you\'re human:\n Your favorite animal is the (blank)","INCORRECT. Your favorite animal is the cat. You will continue to receive Cat Facts every <hour>.","Welcome to Cat Facts!\nDid you knowthat the first cat show was held in 1871 at the Crystal Palace in London? Mee-wow!","Thanks for using Cat Facts! Remember, for every tweet you\'ll receive an instant Cat Fact. To cancel reply \'chryutfgh57\'","<Command not recognized.>\nDid you know there are about 100 distinct breeds of domestic cat? Plenty of furry love!","Cats bury their feces to cover their trails from predators. <To cancel Cat Facts reply dghdfnhddhtd5666443hgfdfdfdfuutregjb654","You want to cancel?\nPlease answer the following to confirm you\'re human:\nYour favorite animal is the (blank)"]
        catfact = "nope"
        catstate = "nope"
        text = text.lower()
        text = text.replace(USERNAME,"")
        for question in turingquestions:
                if question in text:
                        catstate = 0 # Signup and greeting
                        with open(username + '.txt', 'w') as f: # create new file
                                catfact = catfacts[catstate]
                                f.write("0\n")
                        f.close()
        if os.path.isfile(username + '.txt') and catstate !=0:
                with open(username + '.txt', 'r+') as f: # check existing state
                        catstate = f.read().splitlines()
                        if int(catstate[0]) < 11:
                                if int(catstate[0]) == 5: # capture favorite animal
                                        catstate = "6\n" + text
                                        f.seek(0)
                                        f.write(str(catstate))
                                        catfact = catfacts[6]
                                else:
                                        catstate = (int(catstate[0]) + 1)
                                        f.seek(0)
                                        f.write(str(catstate) + "\n")
                                        catfact = catfacts[catstate]
                        elif int(catstate[0]) == 11:
                                if "cat" in text:
                                        catfact = "INCORRECT. You said your favorite animal is the <" + str(catstate[1]) + ">. You will continue to receive <hourly> cat facts."
                                        catstate = 12
                                        f.seek(0)
                                        f.write(str(catstate))
                                        f.close()
                                else:
                                        catfact = "INCORRECT. Your favorite animal is the cat. You will continue to receive <hourly> cat facts."
                                        catstate = 12
                                        f.seek(0)
                                        f.write(str(catstate))
                                        f.close()
                        elif int(catstate[0]) == 12:
                                catfact = "Thanks for using catfacts! You have successfully unsubscribed!\nhttps://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was"
                                os.remove(username + '.txt')
                f.close()
        return catfact
