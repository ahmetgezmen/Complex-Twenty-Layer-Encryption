import datetime
from templates import mainleft, mainright, textedit

print("""
****************
Wellcome to CTLE
****************
""")
def clear():
    print(50*"\n")
datetimenow = datetime.datetime.now()
day = datetimenow.day
month = datetimenow.month
year = datetimenow.year
global todaycodepassword
len_control = "false"
while len_control == "false":
    try:
        toDayCode = int(input("""
        The code entered must be a number.

        The code must have 17 digits.

        Please enter the code >>> """))
        clear()
        todaycodepassword = str((day + month + year) * toDayCode)
        if len(todaycodepassword) >= 20:
            len_control = "true"
        else:
            print("Try again...")
    except:
        clear()
        toDayCode = int(input("""
        The code entered must be a number.

        The code must have 17 digits.

        Please enter the code >>> """))
        clear()
        todaycodepassword = str((day + month + year) * toDayCode)
        if len(todaycodepassword) >= 20:
            len_control = "true"
        else:
            print("Try again...")

activity = "true"
while activity == "true":
    action_control = "true"
    while action_control == "true":
        action = input("""
        Select Action
    [1]>>> Encrypt
    [2]>>> Defuse
    [q]>>> Quit 
        >>>""")
        clear()
        if action == "1" or action == "2" or action == "q":
            action_control = "false"
        else:
            action_control = "true"
    if action == "1":
        ana_mesaj = input("Please enter the message >>>")
        textList = textedit.separate(ana_mesaj)
        outputleft = mainleft.sifrele(textList[0], todaycodepassword)
        outputright = mainright.sifrele(textList[1], todaycodepassword)
        output=outputleft+outputright
        print("""
        Encrypt >>>
        {}
        """.format(output))
        devam = input("Please enter the continue...")
        clear()
    elif action == "2":
        ana_mesaj = input("Please enter the encrypt >>>")
        textList = textedit.separate(ana_mesaj)
        outputleft = mainleft.sifrekır(textList[0], todaycodepassword)
        outputright = mainright.sifrekır(textList[1], todaycodepassword)
        output = outputleft + outputright
        print("""
        Defuse >>>
        {}
        """.format(output))
        devam = input("Please enter the continue...")
        clear()
    elif action == "q":
        activity = "false"
        print("""
        ****************
        Thanks for using
        ****************
        """)