import datetime
from templates import mainleft, mainright, textedit

print("""
****************
Welcome to CTLE
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
    toDayCode = input("""
            The code entered must be a number.

            The code must have 17 digits.

            Please enter the code >>> """)
    clear()
    try:
        if toDayCode==int(toDayCode):
            toDayCode = int(toDayCode)
    except:
        continue
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
        inputText = input("Please enter the message >>>")
        textList = textedit.separate(inputText)
        outputleft = mainleft.encrypt(textList[0], todaycodepassword)
        outputright = mainright.encrypt(textList[1], todaycodepassword)
        output=outputleft+outputright
        print("""
        Encrypt >>>
        {}
        """.format(output))
        devam = input("Please enter the continue...")
        clear()
    elif action == "2":
        inputText = input("Please enter the encrypt >>>")
        textList = textedit.separate(inputText)
        outputleft = mainleft.defuse(textList[0], todaycodepassword)
        outputright = mainright.defuse(textList[1], todaycodepassword)
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
