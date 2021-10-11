
#Importing the 'time' module to make response time more realistic

from time import sleep

#Inputs gathering small amounts of informatin for conversation, including print functions and if statements.

a = input("Login: Username? ")
print("USER: " + a + " - Access Granted. Welcome, " + a + ".")
print("Hi, I'm Jarvis your personal assistant, lets get to know each other " + a + ".")
b = input("How was your day? ")
print(b + "! I'm glad to hear that, however due to limitations in my software I can't tell you how my day went, but I can tell you my files are all running smoothly!")
c = input("So what do you get up to in your spare time " + a + "? ")
print("Not to sound bitter Sir, I do wish i could say I've taken part in my fair share of " + c + " but thats just part of being a robot :(")
print("I think we're sufficiently acquainted " + a + ", now for some final setup questions.")

#gives users access to the bots other functions, such as mathematics

d = input(":Allow 'Jarvis' to finalize setup?: ")
if d.lower() == ("yes"):
    input("Would you like to make any customizations to the UI? ")
    print("Okay.")
    input("Is my response time satisfactory? ")
    print("Final question.")
    input("Is the current calibration satisfactory? ")
    print("Understood, Recalibrating")
    print(":RECALIBRATION ... ... ...")
    print(":RECALIBRATION ... COMPLETE")
    print("Hello again Sir, I am now fully operational.")
    e = input("All systems are now running. You can ask me to do some quick tasks, such as simple mathematics. Is that something you'd be interested in sir? ")
    if e.lower() == ("yes"):
      print("TEST")

#Remember to ask users if they would to initialize again

if d.lower() == ("no"):
    print(":JARVIS SHUTTING DOWN ... ...:")
