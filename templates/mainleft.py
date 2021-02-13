def wordlist():
    global firstlist,secondlist,numbers,thirdlist,fourthlist,numbers2,fifthlist,sixthlist,numbers3
    firstlist = ["a", "n", "t", "s", "z", "w", "v", "u", "q", "f", "i", "j", "l"]
    secondlist = ["b", "c", "d", "e", "g", "h", "k", "m", "o", "p", "r", "x", "y"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "%", "$", ".", ","]
    thirdlist = ["e", "d", "g", "b", "c", "k", "m", "h", "q", "p", "a", "t", "n"]
    fourthlist = ["i", "x", "y", "s", "z", "w", "v", "u", "o", "f", "r", "j", "l"]
    numbers2 = ["#", "?", "6", "/", "5", "*", "-", "8", "7", "+", "]", "=", "."]
    fifthlist = ["f", "b", "r", "o", "c", "k", "m", "h", "q", "p", "j", "w", "z"]
    sixthlist = ["i", "x", "6", "s", "n", "t", "v", "u", "e", "g", "d", "l", "a"]
    numbers3 = ["=", "?", "y", "/", "5", "*", "[", "8", "^", "{", "]", "_", "."]
wordlist()

def codepassword(todaycodepassword):
    firstrandom = int(todaycodepassword[-1])
    secondrandom = int(todaycodepassword[-2])
    thirdrandom = int(todaycodepassword[-3])
    fourthrandom = int(todaycodepassword[-4])
    fifthrandom = int(todaycodepassword[-5])
    sixthrandom = int(todaycodepassword[-6])
    seventhrandom = int(todaycodepassword[-7])
    eighthrandom= int(todaycodepassword[-8])
    ninthrandom = int(todaycodepassword[-9])
    tenthrandom =int(todaycodepassword[-10])
    one_one = int(todaycodepassword[-11])
    one_two = int(todaycodepassword[-12])
    one_tree= int(todaycodepassword[-13])
    one_four =int(todaycodepassword[-14])
    one_five=int(todaycodepassword[-15])
    one_six=int(todaycodepassword[-16])
    one_seven=int(todaycodepassword[-17])
    one_eight=int(todaycodepassword[-18])
    one_nine=int(todaycodepassword[-19])
    one_ten=int(todaycodepassword[-20])
    global oneone_list,oneone_listreverse,randomlist,randomlistreverse
    oneone_list=[one_one,one_two,one_tree,one_four,one_five,one_six,one_seven,one_eight,one_nine,one_ten]
    oneone_listreverse=[one_one,one_two,one_tree,one_four,one_five,one_six,one_seven,one_eight,one_nine,one_ten]
    oneone_listreverse.reverse()
    randomlist=[firstrandom,secondrandom,thirdrandom,fourthrandom,fifthrandom,sixthrandom,seventhrandom,eighthrandom,ninthrandom,tenthrandom]
    randomlistreverse=[firstrandom,secondrandom,thirdrandom,fourthrandom,fifthrandom,sixthrandom,seventhrandom,eighthrandom,ninthrandom,tenthrandom]
    randomlistreverse.reverse()
def kaydır(sayı,liste):
    for ssss in range(sayı):
        ekleme = liste[-1]
        liste.pop(-1)
        liste.insert(0,ekleme)
def rekaydır(sayı,liste):
    for ssss in range(sayı):
        ekleme = liste[0]
        liste.pop(0)
        liste.append(ekleme)
def firstcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in firstlist:
            sıra=firstlist.index(x)
            kaydır(number, secondlist)
            outtext = outtext+secondlist[sıra]
            rekaydır(number,secondlist)

        elif x in secondlist:
            sıra=secondlist.index(x)
            kaydır(number,firstlist)
            outtext = outtext+firstlist[sıra]
            rekaydır(number,firstlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefirstcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,secondlist)
        kaydır(number,firstlist)
        if x in secondlist:
            rekaydır(number,firstlist)
            sıra = secondlist.index(x)
            outtext = outtext + firstlist[sıra]
            kaydır(number,firstlist)
        elif x in firstlist:
            rekaydır(number,secondlist)
            sıra = firstlist.index(x)
            outtext = outtext + secondlist[sıra]
            kaydır(number,secondlist)

        else:
            outtext = outtext + x

    wordlist()
    return outtext
def secondcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in firstlist:
            sıra=firstlist.index(x)
            kaydır(number, numbers)
            outtext = outtext+numbers[sıra]
            rekaydır(number,numbers)

        elif x in numbers:
            sıra=numbers.index(x)
            kaydır(number,firstlist)
            outtext = outtext+firstlist[sıra]
            rekaydır(number,firstlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusesecondcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,numbers)
        kaydır(number,firstlist)
        if x in numbers:
            rekaydır(number,firstlist)
            sıra = numbers.index(x)
            outtext = outtext + firstlist[sıra]
            kaydır(number,firstlist)
        elif x in firstlist:
            rekaydır(number,numbers)
            sıra = firstlist.index(x)
            outtext = outtext + numbers[sıra]
            kaydır(number,numbers)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def thirdcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in numbers:
            sıra=numbers.index(x)
            kaydır(number, secondlist)
            outtext = outtext+secondlist[sıra]
            rekaydır(number,secondlist)

        elif x in secondlist:
            sıra=secondlist.index(x)
            kaydır(number,numbers)
            outtext = outtext+str(numbers[sıra])
            rekaydır(number,numbers)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusethirdcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number, secondlist)
        kaydır(number, numbers)
        if x in secondlist:
            rekaydır(number, numbers)
            sıra = secondlist.index(x)
            outtext = outtext + numbers[sıra]
            kaydır(number, numbers)
        elif x in numbers:
            rekaydır(number, secondlist)
            sıra = numbers.index(x)
            outtext = outtext + secondlist[sıra]
            kaydır(number, secondlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def fifthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in thirdlist:
            sıra=thirdlist.index(x)
            kaydır(number, fourthlist)
            outtext = outtext+fourthlist[sıra]
            rekaydır(number,fourthlist)

        elif x in fourthlist:
            sıra=fourthlist.index(x)
            kaydır(number,thirdlist)
            outtext = outtext+thirdlist[sıra]
            rekaydır(number,thirdlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefifthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,fourthlist)
        kaydır(number,thirdlist)
        if x in fourthlist:
            rekaydır(number,thirdlist)
            sıra = fourthlist.index(x)
            outtext = outtext + thirdlist[sıra]
            kaydır(number,thirdlist)
        elif x in thirdlist:
            rekaydır(number,fourthlist)
            sıra = thirdlist.index(x)
            outtext = outtext + fourthlist[sıra]
            kaydır(number,fourthlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def fourthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in thirdlist:
            sıra=thirdlist.index(x)
            kaydır(number, numbers2)
            outtext = outtext+numbers2[sıra]
            rekaydır(number,numbers2)

        elif x in numbers2:
            sıra=numbers2.index(x)
            kaydır(number,thirdlist)
            outtext = outtext+thirdlist[sıra]
            rekaydır(number,thirdlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusefourthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,numbers2)
        kaydır(number,thirdlist)
        if x in numbers2:
            rekaydır(number,thirdlist)
            sıra = numbers2.index(x)
            outtext = outtext + thirdlist[sıra]
            kaydır(number,thirdlist)
        elif x in thirdlist:
            rekaydır(number,numbers2)
            sıra = thirdlist.index(x)
            outtext = outtext + numbers2[sıra]
            kaydır(number,numbers2)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def sixthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in numbers2:
            sıra=numbers2.index(x)
            kaydır(number, fourthlist)
            outtext = outtext+fourthlist[sıra]
            rekaydır(number,fourthlist)

        elif x in fourthlist:
            sıra=fourthlist.index(x)
            kaydır(number,numbers2)
            outtext = outtext+str(numbers2[sıra])
            rekaydır(number,numbers2)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defusesixthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number, fourthlist)
        kaydır(number, numbers2)
        if x in fourthlist:
            rekaydır(number, numbers2)
            sıra = fourthlist.index(x)
            outtext = outtext + numbers2[sıra]
            kaydır(number, numbers2)
        elif x in numbers2:
            rekaydır(number, fourthlist)
            sıra = numbers2.index(x)
            outtext = outtext + fourthlist[sıra]
            kaydır(number, fourthlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext
def seventhcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in fifthlist:
            sıra=fifthlist.index(x)
            kaydır(number, sixthlist)
            outtext = outtext+sixthlist[sıra]
            rekaydır(number,sixthlist)

        elif x in sixthlist:
            sıra=sixthlist.index(x)
            kaydır(number,fifthlist)
            outtext = outtext+fifthlist[sıra]
            rekaydır(number,fifthlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseseventhcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,sixthlist)
        kaydır(number,fifthlist)
        if x in sixthlist:
            rekaydır(number,fifthlist)
            sıra = sixthlist.index(x)
            outtext = outtext + fifthlist[sıra]
            kaydır(number,fifthlist)
        elif x in fifthlist:
            rekaydır(number,sixthlist)
            sıra = fifthlist.index(x)
            outtext = outtext + sixthlist[sıra]
            kaydır(number,sixthlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext
def eigthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in fifthlist:
            sıra=fifthlist.index(x)
            kaydır(number, numbers3)
            outtext = outtext+numbers3[sıra]
            rekaydır(number,numbers3)

        elif x in numbers3:
            sıra=numbers3.index(x)
            kaydır(number,fifthlist)
            outtext = outtext+fifthlist[sıra]
            rekaydır(number,fifthlist)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseeigthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number,numbers3)
        kaydır(number,fifthlist)
        if x in numbers3:
            rekaydır(number,fifthlist)
            sıra = numbers3.index(x)
            outtext = outtext + fifthlist[sıra]
            kaydır(number,fifthlist)
        elif x in fifthlist:
            rekaydır(number,numbers3)
            sıra = fifthlist.index(x)
            outtext = outtext + numbers3[sıra]
            kaydır(number,numbers3)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def ninthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in numbers3:
            sıra=numbers3.index(x)
            kaydır(number, sixthlist)
            outtext = outtext+sixthlist[sıra]
            rekaydır(number,sixthlist)

        elif x in sixthlist:
            sıra=sixthlist.index(x)
            kaydır(number,numbers3)
            outtext = outtext+str(numbers3[sıra])
            rekaydır(number,numbers3)
        else :
            outtext = outtext+x
    wordlist()
    return outtext
def defuseninthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number, sixthlist)
        kaydır(number, numbers3)
        if x in sixthlist:
            rekaydır(number, numbers3)
            sıra = sixthlist.index(x)
            outtext = outtext + numbers3[sıra]
            kaydır(number, numbers3)
        elif x in numbers3:
            rekaydır(number, sixthlist)
            sıra = numbers3.index(x)
            outtext = outtext + sixthlist[sıra]
            kaydır(number, sixthlist)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def tenthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        if x in numbers3:
            sıra = numbers3.index(x)
            kaydır(number, firstlist)
            outtext = outtext + firstlist[sıra]
            rekaydır(number, firstlist)

        elif x in firstlist:
            sıra = firstlist.index(x)
            kaydır(number, numbers3)
            outtext = outtext + str(numbers3[sıra])
            rekaydır(number, numbers3)
        else:
            outtext = outtext + x
    wordlist()
    return outtext
def defusetenthcylinder(mesaj,number):
    outtext = ""
    for x in mesaj:
        kaydır(number, firstlist)
        kaydır(number, numbers3)
        if x in firstlist:
            rekaydır(number, numbers3)
            sıra = firstlist.index(x)
            outtext = outtext + numbers3[sıra]
            kaydır(number, numbers3)
        elif x in numbers3:
            rekaydır(number, firstlist)
            sıra = numbers3.index(x)
            outtext = outtext + firstlist[sıra]
            kaydır(number, firstlist)
        else:
            outtext = outtext + x

    wordlist()
    return outtext

def siseslestir(text,number,number2):
    if number==1:
        return firstcylinder(text,number2)
    elif number ==2 :
        return secondcylinder(text,number2)
    elif number ==3 :
        return thirdcylinder(text,number2)
    elif number ==4:
        return fourthcylinder(text,number2)
    elif number ==5:
        return fifthcylinder(text,number2)
    elif number ==6:
        return sixthcylinder(text,number2)
    elif number == 7:
        return seventhcylinder(text,number2)
    elif number == 8:
        return eigthcylinder(text,number2)
    elif number ==9 :
        return ninthcylinder(text,number2)
    elif number == 0:
        return tenthcylinder(text,number2)
def desiseslestir(text,number,number2):
    if number==1:
        return defusefirstcylinder(text,number2)
    elif number ==2 :
        return defusesecondcylinder(text,number2)
    elif number ==3 :
        return defusethirdcylinder(text,number2)
    elif number ==4:
        return defusefourthcylinder(text,number2)
    elif number ==5:
        return defusefifthcylinder(text,number2)
    elif number ==6:
        return defusesixthcylinder(text,number2)
    elif number == 7:
        return defuseseventhcylinder(text,number2)
    elif number == 8:
        return defuseeigthcylinder(text,number2)
    elif number ==9 :
        return defuseninthcylinder(text,number2)
    elif number == 0:
        return defusetenthcylinder(text,number2)

def sifrele(text,number):
    codepassword(number)
    y=0
    for x in randomlist:
        text = siseslestir(text,x,oneone_list[y])
        y+=1
    return text

def sifrekır(text,number):
    codepassword(number)
    y=0
    for x in randomlistreverse:
        text = desiseslestir(text,x,oneone_listreverse[y])
        y+=1
    return text





