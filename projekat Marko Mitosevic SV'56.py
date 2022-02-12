#projekat Marko Mitosevic SV'56
import datetime
from turtle import back
from typing import OrderedDict
path = "users.txt"
path1= "apartments.txt"
path2= "equipment.txt"
path3= "reservations.txt"
path4= "blocked.txt"
def login():
    unos=input("Dobrodosli! Da li vec imate korisnicki nalog?(Da/Ne)").lower().strip()
    while unos[0] != "d" or unos[0] !="n":
        if unos[0]== "d":#postojeci korisnik
            print("login: ")
            isUser=False
            isPas=False
            while isUser==False:
                user=input("Unesite vase korisnicko ime: ")
                isUser=checkUser(user)
                if isUser==True:
                    while isPas==False:
                        pas =input("Unesite vasu lozniku: ")
                        isPas=checkPas(user,pas)
                        if isPas==True:
                            print("Uspesna login! Dobrodosli nazad ", user, "!")
                            return user
                        print("Uneli ste pogresnu lozinku za dati nalog!")
                print("Dati korisnik ne postoji!")
        elif unos[0]== "n":
            print("Za koriscenje aplikacije poptrebno je da registrujete nalog!")
            unos=""
            unos=input("Da li zelite da se registrujete?(Da/Ne)").lower().strip()
            while unos[0] != "d" or unos[0] !="n":
                unos = input("Pogresan unos! Molimo vas da unesete Da ili Ne").lower().strip()
                if unos[0]== "d":
                    user=register()
                    return user
                else:
                    exit()
        unos = input("Pogresan unos! Molimo vas da unesete Da ili Ne").lower().strip()


def checkUser(user):
    with open(path,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("|")
            if user == line[0]:
                return True
    return False

def checkPas(user,pas):
    with open(path,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("|")
            if user == line[0]:
                if pas== line[1]:
                    return True
                else:
                    return False
    return False

def register():
    isUser = True
    while isUser == True:
        user=input("Unesite korisnicko ime(ovo cete koristiti prilikom buduce prijave): ")
        isUser=checkUser(user)
        if isUser==False:
            pas=input("Unesite lozinku: ")
            ime=input("Unesite vas ime: ")
            prezime=input("Unesite vas prezime: ")
            pol=input("Unesite vas pol: ")
            tel=input("Unesite vas kontakt telefon: ")
            mail=input("Unesite vas email(primer:nesto@domen): ")
            with open(path,"w",encoding ="utf-8") as file:
                korisnik="{}|{}|{}|{}|{}|{}|{}|gost\n".format(user,pas,ime,prezime,pol,tel,mail)
                file.write(korisnik)
                return user

        else:
            print("Dato korisnicko ime je vec u upotrebi!")

def checkRole(user):
    with open(path,encoding ="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.split("|")
                if user == line[0]:
                    if line[7].strip()=="admin":
                        return 2
                    elif line[7].strip()=="domacin":
                        return 1
                    else:
                        return 0

def menu(role,user):
    if role==0: #admin
        menuAdmin(role,user)
    elif role==1:#domacin
        menuLandlord(role,user)
    else:#gost
        menuGuest(role,user)

def menuAdmin(role,user):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9,10,11,12]
    while inp not in validinput:
        print("="*100)
        print("1. Pregled aktivnih apartmana")
        print("2. Pretraga apartmana")
        print("3. Visekriterijumska pretraga apartmana")
        print("4. Prikaz 10 najpopularnijih gradova")
        print("5. Pretraga rezervacija")
        print("6. Registracija novih domacina")
        print("7. Kreiranje dodatne opreme")
        print("8. Brisanje dodatne opreme")
        print("9. Blokiranje korisnika")
        print("10. Izvestavanje")
        print("11. Odjava")
        print("12. Izlaz")
        print("="*100)
        try:
            inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
            if inp in validinput:
                break
            else:
                print("Unesite validnu opciju!")
        except:
            print("Unesite validnu opciju!")
    if inp==1:
        listApart(role,user)
    elif inp==2:
        searchApart(role,user)
    elif inp==3:
        multiSearchApart(role,user)
    elif inp==4:
        mostPop(role,user)
    elif inp==5:
        searchRes(user)
    elif inp==6:
        newLandLord(user)
    elif inp==7:
        newEquip(user)
    elif inp==8:
        delEquip(user)
    elif inp==9:
        blockUser(user)
    elif inp==10:
        analitics(user)
    elif inp==11:
        newLogin()
    elif inp==12:
        exit()

def menuLandlord(role,user):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9,10,11]
    while inp not in validinput:
        print("="*100)
        print("1. Pregled aktivnih apartmana")
        print("2. Pretraga apartmana")
        print("3. Visekriterijumska pretraga apartmana")
        print("4. Prikaz 10 najpopularnijih gradova")
        print("5. Dodavanje novog apartmana")
        print("6. Izmena postojeceg apartmana")
        print("7. Brisanje apartmana")
        print("8. Pregled rezervacija")
        print("9. Potvrda ili odbijanje rezervacija")
        print("10. Odjava")
        print("11. Izlaz")
        print("="*100)
        try:
            inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
            if inp in validinput:
                break
            else:
                print("Unesite validnu opciju!")
        except:
            print("Unesite validnu opciju!")
    if inp==1:
        listApart(role,user)
    elif inp==2:
        searchApart(role,user)
    elif inp==3:
        multiSearchApart(role,user)
    elif inp==4:
        mostPop(role,user)
    elif inp==5:
        newApart(user,user)
    elif inp==6:
        editApart(user)
    elif inp==7:
        delApart(user)
    elif inp==8:
        listResL(user)
    elif inp==9:
        approveRes(user)
    elif inp==10:
        newLogin()
    elif inp==11:
        exit()

def menuGuest(role,user):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9]
    while inp not in validinput:
        print("="*100)
        print("1. Pregled aktivnih apartmana")
        print("2. Pretraga apartmana")
        print("3. Visekriterijumska pretraga apartmana")
        print("4. Prikaz 10 najpopularnijih gradova")
        print("5. Rezervisanje apartmana")
        print("6. Pregled rezervacija")
        print("7. Ponistavanje rezervacija")
        print("8. Odjava")
        print("9. Izlaz")
        print("="*100)
        try:
            inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
            if inp in validinput:
                break
            else:
                print("Unesite validnu opciju!")
        except:
            print("Unesite validnu opciju!")
    if inp==1:
        listApart(role,user)
    elif inp==2:
        searchApart(role,user)
    elif inp==3:
        multiSearchApart(role,user)
    elif inp==4:
        mostPop(role,user)
    elif inp==5:
        resApart(user)
    elif inp==6:
        listRes(user)
    elif inp==7:
        delRes(user)
    elif inp==8:
        newLogin()
    elif inp==9:
        exit()

def listApart(role,user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                begdate=line[5].split(",")
                enddate=line[6].split(",")
                display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                display=display.strip()
                print(display)
        print(150*"=")
        backToMenu(role,user)
 
def displayHeader():
    print(150*"=")
    print("Sifra | Tip     | Br Soba | Br gostiju | Adresa"+ 43*" "+ "|  Dospupnost apartmana  | Domacin    | Dnevna cena | Dodatni materijal")

def backToMenu(role,user):
    unos=" "
    while unos[0] != "d" or unos[0] != "n":
        unos=input("Da li zelite da se vratite u meni?(Da/Ne)\n").lower().strip()
        if unos[0]== "d":
            menu(role,user)
        elif unos[0]=="n":
            exit()
        print("Pogresan unos! Molimo vas da unesete Da ili Ne:")
        
def searchApart(role,user):
    unos = -1
    while unos not in [1,2,3,4]:
        searchMenu()
        unos=eval(input(""))
        if unos in [1,2,3,4]:
            if unos==1:
                searchCity()
            elif unos==2:
                searchDate()
            elif unos==3:
                searchNum()
            else:
                searchPrice()
            break
        print("Pogresan unos, molim vas unesite validan broj!")
    backToMenu(role,user)

def searchCity():
    unos=input("Unesite grad ili deo imena grada za pretragu:").lower()
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                if unos in line[4].lower():
                    begdate=line[5].split(",")
                    enddate=line[6].split(",")
                    display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                    display=display.strip()
                    print(display)
        print(150*"=")
        

def searchMenu():
    print("Unesite broj ispred kriterijuma po kojem zelite da pretrazite apartmane: ")
    print("1. Pretrazivanje po mestu")
    print("2. Pretrazivanje po vremenskoj dostupnosti")
    print("3. Pretrazivanje po broju osoba")
    print("4. Pretrazivanje po ceni")

def searchNum():
    unos=-1
    unos1=-1
    while unos<0:
        unos=eval(input("Unesite granicu za broj gostiju:\n"))
        if unos>0:
            while unos1 not in [1,2,3,4]:
                menuNum()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        numUpper(unos,equal,3)
                    elif unos1 in [3,4]:
                        numLower(unos,equal,3)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        print("Molimo Vas unesite broj veci od nule!")
    
def searchPrice():
    unos=-1
    unos1=-1
    while unos<0:
        unos=eval(input("Unesite granicu za cenu:\n"))
        if unos>0:
            while unos1 not in [1,2,3,4]:
                menuPrice()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        numUpper(unos,equal,8)
                    elif unos1 in [3,4]:
                        numLower(unos,equal,8)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        print("Molimo Vas unesite broj veci od nule!")

def menuNum():
    print("Unesite broj ispred zelenje opcije pretrage")
    print("1. Pretraga apartmana za broj gostiju veci od datog")
    print("2. Pretraga apartmana za broj gostiju veci ili jednak od datog")
    print("3. Pretraga apartmana za broj gostiju manji od datog")
    print("4. Pretraga apartmana za broj gostiju manji ili jednak od datog")

def menuPrice():
    print("Unesite broj ispred zelenje opcije pretrage")
    print("1. Pretraga apartmana sa cenom vecom od date")
    print("2. Pretraga apartmana sa cenom vecom ili jednak od date")
    print("3. Pretraga apartmana sa cenom manjom od date")
    print("4. Pretraga apartmana sa cenom manjom ili jednakom od date")

def numUpper(unos,equal,i):
    if equal==True:    
        unos+=1
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                if unos<int(line[i]):
                    begdate=line[5].split(",")
                    enddate=line[6].split(",")
                    display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                    display=display.strip()
                    print(display)
        print(150*"=")


def numLower(unos,equal,i):
    if equal==True:    
        unos-=1
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                if unos>int(line[i]):
                    begdate=line[5].split(",")
                    enddate=line[6].split(",")
                    display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                    display=display.strip()
                    print(display)
        print(150*"=")

def multiSearchApart(role,user):
    unos = -1
    stop = False
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
    while stop == False:    
        while unos not in [1,2,3,4]:
            searchMenu()
            unos=eval(input(""))
            if unos in [1,2,3,4]:
                if unos==1:
                    lines=searchCityM(lines)
                elif unos==2:
                    lines=searchDateM(lines)
                elif unos==3:
                    lines=searchNumM(lines)
                else:
                    lines=searchPriceM(lines)
                break
            print("Pogresan unos, molim vas unesite validan broj!")
        unos=input("Da li zelite da postavite jos kriterijuma za pretragu?(Da/Ne)").lower().strip()
        while unos[0] != "d" or unos[0] !="n":
            if unos[0]=="d":
                break
            elif unos[0]=="n":
                stop=True
                break
            print("Molimo vas unesite da ili ne!")
    backToMenu(role,user)

def searchCityM(lines):
    unos=input("Unesite grad ili deo imena grada za pretragu:").lower()
    tmpline=[]
    for line in lines:
        line = line.split("|")
        if line[9]=="aktivan":
            if unos in line[4].lower():
                tmpline=tmpline.append(line)
    return tmpline

def searchNumM(lines):
    unos=-1
    unos1=-1
    while unos<0:
        unos=eval(input("Unesite granicu za broj gostiju:\n"))
        if unos>0:
            while unos1 not in [1,2,3,4]:
                menuNum()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        numUpperM(unos,equal,3,lines)
                    elif unos1 in [3,4]:
                        numLowerM(unos,equal,3,lines)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        print("Molimo Vas unesite broj veci od nule!")

def searchPriceM(lines):
    unos=-1
    unos1=-1
    while unos<0:
        unos=eval(input("Unesite granicu za cenu:\n"))
        if unos>0:
            while unos1 not in [1,2,3,4]:
                menuPrice()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        numUpperM(unos,equal,8,lines)
                    elif unos1 in [3,4]:
                        numLowerM(unos,equal,8,lines)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        print("Molimo Vas unesite broj veci od nule!")


def numUpperM(unos,equal,i,lines):
    if equal==True:    
        unos+=1
    templist=[]
    for line in lines:
        line = str(line).split("|")
        if line[9]=="aktivan":
            if unos<int(line[i]):
                templist=templist.append(line)
    return templist

def numLowerM(unos,equal,i,lines):
    if equal==True:    
        unos-=1
    templist=[]
    for line in lines:
        line = str(line).split("|")
        if line[9]=="aktivan":
            if unos>int(line[i]):
                templist=templist.append(line)
    return templist

def searchDate():
    isDate=False
    unos1=-1
    while isDate==False:
        unos=input("Unesite datum po kojem zelite da pretrazite  apartmane u formatu dan.mesec.godina:\n")
        try:
            unos=unos.split(".")
            date=datetime.date(int(unos[2]),int(unos[1]),int(unos[0]))
            isDate=True
            while unos1 not in [1,2,3,4]:
                dateMenu()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        dateUpper(date,equal,5)
                    elif unos1 in [3,4]:
                        dateLower(date,equal,6)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        except:
            print("Molimo Vas unesite validan datum!")

def dateMenu():
    print("Unesite broj ispred kriterijuma po kojem zelite da pretrazite apartmane")
    print("1. Pretraga apartmana za datum veci od datog")
    print("2. Pretraga apartmana za datum veci ili jednak od datog")
    print("3. Pretraga apartmana za datum manji od datog")
    print("4. Pretraga apartmana za datum manji ili jednak od datog")

def dateUpper(date,equal,i):
    if equal==True:    
        date=date+datetime.timedelta(days=1)
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                datum=line[i].split(".")
                adate=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
                if date<adate:
                    begdate=line[5].split(",")
                    enddate=line[6].split(",")
                    display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                    display=display.strip()
                    print(display)
        print(150*"=")

def dateLower(date,equal,i):
    if equal==True:    
        date=date+datetime.timedelta(days=-1)
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                dat=line[i].split(",")
                datum=dat[len(dat)-1].split(".")
                adate=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
                if date>adate:
                    begdate=line[5].split(",")
                    enddate=line[6].split(",")
                    display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                    display=display.strip()
                    print(display)
        print(150*"=")

def searchDateM(lines):
    isDate=False
    unos1=-1
    while isDate==False:
        unos=input("Unesite datum po kojem zelite da pretrazite  apartmane u formatu dan.mesec.godina:\n")
        try:
            unos=unos.split(".")
            date=datetime.date(int(unos[2]),int(unos[1]),int(unos[0]))
            isDate=True
            while unos1 not in [1,2,3,4]:
                dateMenu()
                unos1=eval(input(""))
                if unos1 in [1,2,3,4]:
                    
                    if unos1 in [2,4]:
                        equal=True
                    elif unos1 in [1,3]:
                        equal=False
                    if unos1 in [1,2]:
                        dateUpperM(date,equal,5,lines)
                    elif unos1 in [3,4]:
                        dateLowerM(date,equal,6,lines)
                    
                    break
                print("Pogresan unos,molimo Vas da unesete validnu opciju!")
            break
        except:
            print("Molimo Vas unesite validan datum!")

def dateUpperM(date,equal,i,lines):
    if equal==True:    
        date=date+datetime.timedelta(days=1)
    templist=[]
    for line in lines:
        line = str(line).split("|")
        datum=line[i].split(".")
        adate=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
        if line[9]=="aktivan":
            if date<adate:
                templist=templist.append(line)
    return templist

def dateLowerM(date,equal,i,lines):
    if equal==True:    
        date=date+datetime.timedelta(days=-1)
    templist=[]
    for line in lines:
        line = str(line).split("|")
        datum=line[i].split(".")
        adate=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
        if line[9]=="aktivan":
            if date>adate:
                templist=templist.append(line)
    return templist

def delEquip(user):
    unos=""
    pas=""
    good=False
    goodp=False

    while good==False:
        unos=input("Unesite ime dodatne opreme: ")
        good=checkEquip(unos)
        if good==True:
            while goodp==False:
                pas=input("Unesite sifru za datu dodatnu opremu: ")
                goodp=checkEquipPas(unos,pas)
                if goodp==True:
                    goodp=checkEquipRes(unos)
                    if goodp==False:
                        with open(path2,"r+",encoding ="utf-8") as file:
                            newfile=file.read()
                        str=pas + "|" + unos + "\n"
                        newfile=newfile.replace(str, "")
                        with open(path2,"w",encoding ="utf-8") as file:

                            file.write(newfile)
                        print("Dodatna oprema " + unos + " je uspesno obrisana.")
                        break
                    else:
                        print("Data dodatna oprema je u upotrebi u apartmanima!")
                        delEquip()
                print("Data sifra i dodatna oprema se ne poklapaju!")
        if good==True:
            break
        print("Dato ime dodatne opreme ne postoji!")      
    backToMenu(0,user)     

def checkEquipRes(user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line=line.split("|")
            equip=line[10].split(",")
            for i in equip:
                if user==i.strip():
                    return True


def newEquip(user):
    unos=""
    pas=""
    good=True
    goodp=True

    while good==True:
        unos=input("Unesite ime dodatne opreme: ")
        good=checkEquip(unos)
        if good==False:
            while goodp==True:
                pas=input("Unesite sifru za datu dodatnu opremu\n(u obliku dvocifrenog broja,ako je broj jednocifren ispred brojs napisite nulu): ")
                goodp=checkEquipPas(unos,pas)
                if goodp==False:
                    with open(path2,"r+",encoding ="utf-8") as file:
                        newfile=file.read()
                    str=pas + "|" + unos + "\n\n"
                    newline=newfile.rfind("\n")
                    newfile=newfile[:newline]+str
                    with open(path2,"w",encoding ="utf-8") as file:

                        file.write(newfile)
                    print("Dodatna oprema " + unos + " je uspesno dodata")
                    break
                print("Data sifra je vec u upotrebi!")
        if good==False:
            break
        print("Dato ime dodatne opreme je vec u upotrebii!")      
    backToMenu(0,user)


def checkEquip(unos):
    with open(path2,"r+",encoding ="utf-8") as file:
        
        lines=file.readlines()
        for line in lines:
            line = line.split("|")
            if "\n"== line[0]:
                break
            if unos == line[1].strip():
                return True

        return False  

def checkEquipS(unos):
    with open(path2,"r+",encoding ="utf-8") as file:
        
        lines=file.readlines()
        for line in lines:
            line = line.split("|")
            if "\n"== line[0]:
                break
            if unos == line[0].strip():
                return True

        return False  

def checkEquipPas(user,pas):
    with open(path2,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("|")
            if "\n"== line[0]:
                break
            if user == line[1].strip():
                if pas== line[0]:
                    return True
                else:
                    return False
    return False  

def newLandLord(us):
    isUser = True
    while isUser == True:
        user=input("Unesite korisnicko ime domacina: ")
        isUser=checkUser(user)
        if isUser==False:
            pas=input("Unesite lozinku: ")
            ime=input("Unesite ime domacina: ")
            prezime=input("Unesite prezime domacina: ")
            pol=input("Unesite pol domacina: ")
            tel=input("Unesite kontakt telefon domacina: ")
            mail=input("Unesite mail domacina(primer:nesto@domen): ")
            with open(path,"w",encoding ="utf-8") as file:
                korisnik="{}|{}|{}|{}|{}|{}|{}|domacin\n".format(user,pas,ime,prezime,pol,tel,mail)
                file.write(korisnik)
                #return user

        else:
            print("Dato korisnicko ime je vec u upotrebi!")
    backToMenu(0,us)

def newApart(user):
    with open(path1,encoding ="utf-8") as file:
        readlines=file.readlines()
        for line in readlines:
            line = line.split("|")
            if line[0]!="\n" and line[0]!="":
                tmp=line[0]
        sifra=int(tmp)+1
        tip=input("Unesite tip apartmana: ")
        brsoba=-1
        while brsoba <0:
            try:
                brsoba=int(eval(input("Unesite broj soba: ")))
                break
            except:
                print("Unesite prirodan broj!")
        brgost=-1
        while brgost <0:
            try:
                brgost=int(eval(input("Unesite broj gostiju: ")))
                break
            except:
                print("Unesite prirodan broj!")
        lok=input("Unesite lokaciju apartmana: ")
        begdate=input("Unesite pocetan datum termina: ")#poprsvi unos ovde\
        enddate=input("Unesite zavrsana datum terima: ")
        cena=-1
        while cena <0:
            try:
                cena=eval(input("Unesite cenu po noci u evrima: "))
                break
            except:
                print("Unesite validnu cenu!")
        listEquip()
        unos=""
        equip=""
        while unos.lower() != "x":
            unos=input("Unesite sifru dodatne opreme koju imate u apartmanu(za prestanak unos unesite x): ")
            isEquip=checkEquipS(unos)
            if isEquip==False:
                print("Data sifra nije povezana ni sa jednom dodatnom opremom!")
                continue
            equip=equip+unos+","
    with open(path2,"r+",encoding ="utf-8") as file:
        newfile=file.read()
    str=sifra + "|" + tip + "|" + f'{brsoba}' + "|" + f'{brgost}' + "|" + lok + "|" + begdate + "|" + enddate + "|" + user + "|" + f'{cena}' + "|" +"neaktivan" + "|" + equip + "\n\n"
    newline=newfile.rfind("\n")
    newfile=newfile[:newline]+str
    with open(path2,"w",encoding ="utf-8") as file:

        file.write(newfile)
    print("Dodatna oprema " + unos + " je uspesno dodata")
    backToMenu(0,user)

def listEquip():
    with open(path2,encoding ="utf-8") as file:
        print(120*"=")
        print("Sifra | Dodatna oprema")
        print(120*"=")
        lines=file.readlines()
        for line in lines:
            if line == "\n":
                break
            line=line.split("|")
            print(line[0]+"    | "+line[1].strip())
        print(120*"=")
    

def blockUser(user):
    isUser=False
    while isUser==False:
        user=input("Unesite korisnicko ime korisnika koga zelite blokirati: ")
        isUser=checkUser(user)
        if isUser==True:
            break
        print("Dato korisnicko ime nije u upotrebi!")
    with open(path,encoding ="utf-8") as file:
        lines = file.readlines()
        i=0
        for line in lines:
            line = line.split("|")
            if user == line[0]:
                korisnik=lines[i]
            i=i+1
    with open(path,encoding ="utf-8") as file:
        users=file.read()
        users=users.replace(korisnik,"")

    with open(path4,encoding ="utf-8") as file:
        
        newfile=file.read()
        str=user + "\n\n"
        newline=newfile.rfind("\n")
        newfile=newfile[:newline]+str
    with open(path2,"w",encoding ="utf-8") as file:

        file.write(newfile)
    print("Dati korisnik je uspesno blokiran")


    backToMenu(0,user)

def delApart(user):
    listApartL(user)
    isPas=False
    while isPas==False:
        sifra=input("Unesite sifru apartmana kojeg zelite da obrisete: ")
        isPas=checkPsp(sifra,user)
        if isPas==True:
            break
        else:
            print("Data sifra nije u upotrebi!")
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        i=0
        for line in lines:
            line = line.split("|")
            if user == line[0]:
                apartman=lines[i]
            i=i+1
    with open(path1,encoding ="utf-8") as file:
        users=file.read()
        users=users.replace(apartman,"")
    print("Apartman je uspesno obrisan!")
    backToMenu(1,user)

def checkPsp(pas,user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("|")
            if pas == line[0]:
                if user==line[7]:
                    return True
    return False

def listApartL(user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            if line=="\n":
                break
            line = line.split("|")
            if line[7]==user:
                begdate=line[5].split(",")
                enddate=line[6].split(",")
                display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                display=display.strip()
                print(display)
        print(150*"=")

def checkPspA(pas):
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
            try:
                line=line.split("|")
                if line[9]=="aktivan":
                    if line[0]==pas:
                        return True
            except:
                return False
        return False

def getDates(sif):
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
                line=line.split("|")
                if line[0]==sif:
                    beg=line[5].split(",")
                    end=line[6].split(",")
                    i=0
                    print("Broj | Pocetak     | Kraj     ")
                    for date in beg:
                        print("{:2d}.  | {:11s} | {:11s} ".format((i+1),date,end[i]))
                        i+=1
                return i  ,beg,end
                        

def resApart(user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        displayHeader()
        for line in lines:
            display=""
            line = line.split("|")
            if line[9]=="aktivan":
                begdate=line[5].split(",")
                enddate=line[6].split(",")
                display="{:6s}|{:9s}| {:8s}| {:11s}| {:49s}| {:11s}-{:11s}| {:11s}| {:12s}| {:49s}".format(line[0],line[1],line[2],line[3],line[4],begdate[0],enddate[0],line[7],line[8],line[10].rstrip())
                display=display.strip()
                print(display)
        print(150*"=")
    ok=False
    while ok==False:
        sif=input("Unesite sifru apartmana kojeg zelite da rezervisete: ")
        ok=checkPspA(sif)
        if ok==True:
            break
        else:
            print("Ne postoji aktivan apartman sa datom sifrom! Molimo vas unesite validnu sifru apartmana.")
    i,beg,end=getDates(sif)
    num=-1
    while num>i+1 or num<0:
        try:
            num=eval(input("Unesite broj ispred termina koji zelite da rezervisete: "))
            if num<i+1 and num>0:
                num=num-1
                poc=beg[num].split(".")
                pocetak=datetime.date(int(poc[2]),int(poc[1]),int(poc[0]))
                krj=end[num].split(".")
                kraj=datetime.date(int(krj[2]),int(krj[1]),int(krj[0]))
                isDate=False
                while isDate==False:
                    begg=input("Unesite pocetni datum rezervacije u formatu dan.mesec.godina: ")
                    pdan=begg
                    begg=begg.split(".")
                    try:
                        begdate=datetime.date(int(begg[2]),int(begg[1]),int(begg[0]))
                        if begdate<pocetak or begdate>kraj:
                            print("Datum mora biti unutar termina!")
                            continue
                        else:
                            isDate=True
                            break
                    except:
                        print("Unesite validan datum!")

                valid=False
                while valid==False:
                    daynum=eval(input("Unesite broj dana koji zelite da rezervsite u terminu: "))
                    if daynum>0:
                        try:
                            enddate=begdate+datetime.timedelta(days=daynum)
                            if enddate>kraj:
                                print("Unesite validan broj dana za dati termin!")
                                continue
                            else:
                                valid=True
                                break
                        except:
                            print("Unesite validan broj dana!")
                brgost=getGuestNum(sif)
                unos="o"
                while unos[0] != "d" or unos[0] !="n":
                    unos=input("Da li rezerviste apartman za sebe?(Da/Ne)").lower().strip()
                    if unos[0]== "d":
                        glist=user
                        b=1
                        break
                    elif unos[0]=="n":
                        b=0
                        glist=""
                        break
                    print("Molimo vas odgovorite sa da ili ne!")
                while b<brgost:
                    guest=input("Unesite ime i prezime " + f'{b+1}'  + ". gosta(ako ste vec uneli sve goste unesite x): ")
                    if guest.lower()=="x":
                        break
                    if b==0:
                        glist=guest
                    else:
                        glist=glist + "," + guest
                    b=b+1
                cenaDan=getPrice(sif)
                cena=cenaDan*daynum
                with open(path3,encoding ="utf-8") as file:
                    newfile=file.read()
                    newline=newfile.rfind("\n")
                    sifra=newfile.count("\n")
                    str=sif + "|"  + pdan + "|" + f'{cena}' + "|" + glist + "|" + "kreirana" + "|" + f'{sifra}' + "\n\n"
                    newfile=newfile[:newline]+str
                with open(path3,"w",encoding ="utf-8") as file:

                    file.write(newfile)
                print("Rezervacija je uspesno kreirana!")
                backToMenu(2,user)
            else:
                print("Unesite validan broj!")
        except:
            print("Unesite validan broj!")


def getGuestNum(pas):
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
                line=line.split("|")
                if line[9]=="aktivan":
                    if line[0]==pas:
                        return int(line[3])

def getPrice(pas):
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
                line=line.split("|")
                if line[9]=="aktivan":
                    if line[0]==pas:
                        return float(line[8])

def searchRes(user):
    unos=""
    while unos not in [1,2,3]:
        menuRes()
        try:
            unos=eval(input(""))
            if unos in [1,2,3]:
                if unos==1:
                    searchResS()
                elif unos==2:
                    searchResA()
                elif unos==3:
                    searchResU()
                break
        except:
            print("Pogresan unos, molim vas unesite validan broj!")
        print("Pogresan unos, molim vas unesite validan broj!")
    backToMenu(0,user)

def searchResS():
    print("1. Pretraga prihvacenih rezervacija\n2.Pretraga odbijenih rezervacija")
    opt=""
    while opt not in [1,2]:
        try:
            opt=eval(input("Unesite broj ispred kriterijuma po kojem zelite da vrsite pretragu"))
            if opt not in [1,2]:
                print("Molimo vas unesite validnu opciju!")
        except:
            print("Molimo vas unesite validnu opciju!")
    if opt==1:
        listStatus("prihvaćena")
    else:
        listStatus("odbijena")

def listStatus(status):
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti ")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[5].strip()==status:
                print("{:2s}    | {:11s} | {:7s} | {:6s} | {:70s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4]))

def searchResA():
    adress=input("Unesite adresu po kojoj zelite da se vrsi pretraga: ").strip().lower()
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
    sifre=[" "]
    for line in lines:
        if line=="\n":
            break
        line = line.split("|")
        if line[9]=="aktivan":
            if adress in line[4].lower():
                sifre.append(line[0])
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[0] in sifre:
                print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))

def searchResU():
    isUser=False
    isLandlord=False
    while isUser==False or isLandlord==False:
        user=input("Unesite korisnicko ime domacina:")
        isUser=checkUser(user)
        if isUser==True:
            if checkRole(user)==1:
                isLandlord=True
                break
            else:
                print("Uneti korisnik nije domacin!")
                continue
        else:
            print("Unesite validno korisnicko ime domacina!")
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
    sifre=[" "]
    for line in lines:
        if line=="\n":
            break
        line = line.split("|")
        if line[9]=="aktivan":
            if user==line[7]:
                sifre.append(line[0])
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[0] in sifre:
                print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))


def menuRes():
    print("Unesite broj ispred kriterijuma po kojem zelite da pretrazite rezervacije: ")
    print("1. Pretraga rezervacija po statusu")
    print("2. Pretraga rezervacija po adresi")
    print("3. Pretraga rezervacija po korisnickom imenu domacina")
    
def listRes(user):
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            gost=lin[4].split(",")
            if gost[0]==user:
                print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))
    backToMenu(2,user)


def listResL(user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        sifre=[" "]
        for line in lines:
            if line=="\n":
                break
            line = line.split("|")
            if line[9]=="aktivan":
                if user==line[7]:
                    sifre.append(line[0])
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[0] in sifre:
                if lin[5]=="kreirana":
                    print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))
    backToMenu(1,user)

def delRes(user):
    isResPas=False
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            gost=lin[4].split(",")
            if gost[0]==user:
                print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))
    while isResPas==False:
        sif=input("Unesite sifru rezervacije koju zelite da obrisete: ")
        isResPas=checkResPas(sif,user)
        if isResPas==True:
            break
        else:
            print("Data sifra nije u upotrebi sa vasom rezervacijom, molimo vas unesite validnu sifru!")
            continue
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[5].strip()=="prihvaćena":
                resetTermin(lin[1],lin[2],lin[0])
        i=0
        for line in lines:
            line = line.split("|")
            if user == line[0]:
                res=lines[i]
                break
            i=i+1
    with open(path3,encoding ="utf-8") as file:
        reserv=file.read()
        newfile=reserv.replace(res,"")
    with open(path3,"w",encoding ="utf-8") as file:
        file.write(newfile)


    backToMenu(2,user)

def resetTermin(beglist,days,sif):
    beg=beglist.split(".")
    begdate=datetime.date(int(beg[2]),int(beg[1]),int(beg[0]))
    begdate= begdate + datetime.timedelta(-1)
    enddate=begdate+datetime.timedelta(days+2)
    pocetak=str(begdate.day)+"."+str(begdate.month)+"."+str(begdate.year)
    kraj=str(enddate.day)+"."+str(enddate.month)+"."+str(enddate.year)
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
            lin=line.split("|")
            if lin[0]==sif:
                poc=lin[5].split(",")
                krj=lin[6].split(",")
                for date in poc:
                    if date == kraj:
                        poc=poc.remove(date)
                lin[5]=",".join(poc)
                for date in krj:
                    if date == pocetak:
                        krj = krj.remove(date)
                lin[6]=",".join(krj)
                oldline=line
                newline="|".join(lin)
    with open(path1,encoding ="utf-8") as file:
        oldfile=file.read()
        newfile=oldfile.replace(oldline,newline)            
    with open(path1,"w",encoding ="utf-8") as file:
        file.write(newfile)

def checkResPas(sif,user):
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[6].strip()==sif:
                gost=lin[4].split(",")
                if gost[0]==user:
                    return True
        return False

def approveRes(user):#odbijene!!
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        sifre=[" "]
        for line in lines:
            if line=="\n":
                break
            line = line.split("|")
            if line[9]=="aktivan":
                if user==line[7]:
                    sifre.append(line[0])
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        validPas=[]
        print("Sifra |  Datum      | Br Dana | Cena   | Gosti " + 45*" " + "| Status")
        for line in lines:
            if line=="\n":
                break
            lin=line.split("|")
            if lin[0] in sifre:
                if lin[5]=="kreirana":
                    validPas.append(lin[6].strip())
                    print("{:2s}    | {:11s} | {:7s} | {:6s} | {:50s} | {:20s}".format(lin[6].strip(),lin[1],lin[2],lin[3],lin[4],lin[5]))
    sif="-1"
    while sif not in validPas:
        sif=input("Unesite sifru rezervaciju koju zelite da potvrdite/odbijete: ")
        if sif in validPas:
            break
        else:
            print("Unesite validnu sifru!")
    
    inp="3"
    while inp[0] != "1" and inp[0]!= "2":
        print("1. Potvrda rezervacije")
        print("2. Odbijanje rezervacije")
        inp=input("Unesite broj ispred opcije koju zelite da uradite: ")
        if inp[0]=="1":
            approved=True
            break
        elif inp[0]=="2":
            approved=False
            break
        else:
            print("Molimo vas unesite validnu opciju!")
    
    if approved==True:
        with open(path3,encoding ="utf-8") as file:
            lines=file.readlines()
            for line in lines:
                if line=="\n":
                    break
                line=line.split("|")
                if line[6].strip()==sif:
                    pas=line[0]
                    bg=line[1].split(".")
                    begt=datetime.date(int(bg[2]),int(bg[1]),int(bg[0]))
                    newbeg=begt+datetime.timedelta(-1)
                    endt=begt+datetime.timedelta(float(line[2]))
                    newend=endt+datetime.timedelta(1)
        with open(path1,encoding ="utf-8") as file:
            lines=file.readlines()
            for line in lines:
                lin=line.split("|")
                if lin[0]==pas:
                    beg=lin[5].split(",")
                    end=lin[6].split(",")
                    i=0
                    for termin in beg:
                        t=termin.split(".")
                        bt=datetime.date(int(t[2]),int(t[1]),int(t[0]))
                        if bt>begt or termin==beg[len(beg)-1]:
                            novit=str(newend.day)+"."+str(newend.month)+"."+str(newend.year)
                            poslednjip=end[len(beg)-1].split(".")
                            poslednjipdatum=datetime.date(int(poslednjip[2]),int(poslednjip[1]),int(poslednjip[0]))
                            if newend>=poslednjipdatum:
                                newbt=",".join(beg)
                            elif i==0:
                                posle=",".join(beg[1:])
                                if posle!="":
                                    newbt=beg[0]+"," + novit+","+posle
                                else:
                                    newbt=beg[0]+"," + novit
                            elif beg[i:]==[]:
                                pre=",".join(beg[0:i])
                                if newbeg>=poslednjipdatum:
                                    newet=beg
                                elif pre !="":
                                    newbt=pre+","+novit + "," + beg[i]
                                else:
                                    newbt=novit + "," + beg[i]
                            else:
                                pre=",".join(beg[0:i])
                                posle=",".join(beg[i:])
                                newbt=pre+","+novit+","+posle
                            novite=str(newbeg.day)+"."+str(newbeg.month)+"."+str(newbeg.year)
                            poslednji=end[len(end)-1].split(".")
                            poslednjidatum=datetime.date(int(poslednji[2]),int(poslednji[1]),int(poslednji[0]))
                            if newend>=poslednjidatum:
                                pree=",".join(end[0:i])
                                newet=pree+","+novite
                                break
                            elif end[0:i-1]==[]:
                                poslee=",".join(end[i-1:])
                                if poslee!="":
                                    newet=novite+","+poslee
                                    break
                                else:
                                    newet=novite
                                    break
                            elif end[i-1:]==[]:
                                pree=",".join(end[0:i-1])
                                poslednji=end[len(end)-1].split(".")
                                poslednjidatum=datetime.date(int(poslednji[2]),int(poslednji[1]),int(poslednji[0]))
                                if newend>=poslednjidatum:
                                    newet=pree+","+novite
                                    break
                                elif pree!="":
                                    newet=pree+","+novite + "," + end[len(end)-1]
                                    break
                                else:
                                    newet=novite + "," + end[len(end)-1]
                                    break
                                
                            else:
                                pree=",".join(end[0:i-1])
                                poslee=",".join(end[i-1:])
                                newet=pree+","+novite+","+poslee
                                break
                        i=i+1
                    pocetni=newbt.split(",")
                    krajnji=newet.split(",")
                    try:#za brisanje jednodnevnih datuma
                        for j in range(len(pocetni)):
                            if pocetni[j]==krajnji[j]:
                                newbt=",".join(pocetni[0:j])+",".join(pocetni[j+1:])
                                newet=",".join(krajnji[0:j])+",".join(krajnji[j+1:])
                                pocetni.remove(pocetni[j])
                                krajnji.remove(krajnji[j])
                    except:
                        pass #zbog removea da stane na kraju niza datuma
                    lin[5]=newbt
                    lin[6]=newet
                    newline="|".join(lin)
        for i in range(len(lines)):
            if lines[i].split("|")[0]==pas:
                lines[i]=newline
        newfile="".join(lines)
        with open(path1,"w",encoding ="utf-8") as file:
            file.write(newfile)
        with open(path3,encoding ="utf-8") as file:
            lines=file.readlines()
            for i in range(len(lines)):
                tmpline=lines[i].split("|")
                if tmpline==["\n"]:
                    break
                elif tmpline[6].strip()==sif:
                    tmpline[5]="prihvaćena"
                    lines[i]="|".join(tmpline)
            newfile="".join(lines)
        with open(path3,"w",encoding ="utf-8") as file:
            file.write(newfile)
    else:
        with open(path3,encoding ="utf-8") as file:
            lines=file.readlines()
            for i in range(len(lines)):
                tmpline=lines[i].split("|")
                if tmpline==["\n"]:
                    break
                elif tmpline[6].strip()==sif:
                    tmpline[5]="odbijena"
                    lines[i]="|".join(tmpline)
            newfile="".join(lines)
        with open(path3,"w",encoding ="utf-8") as file:
            file.write(newfile)

    backToMenu(1,user)

def editApart(user):
    listApartL(user)
    with open(path1,"r+",encoding ="utf-8") as file:
        isPas = False
        while isPas==False:
            sif=input("Unesite sifru apartmana za kojeg zelite da promenite podatke: ")
            isPas=checkPsp(sif,user)
            if isPas==True:
                break
            else:
                print("Unesite validnu sifru apartmana!")
        lines=file.readlines()
        j=0
        for line in lines:
            lin=line.split("|")
            if lin[0]==sif:
                inp=""
                while inp=="":
                    print("Trenutni tip apartmana je " +lin[1]+ ",ako zelite da ga promenite upisite novi tip, a ako zelite da ostane isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        lin[1]=inp
                inp=""
                while inp=="":
                    print("Trenutni broj soba je " +lin[2]+ ",ako zelite da ga promenite upisite novi broj, a ako zelite da ostane isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        lin[2]=inp
                inp=""
                while inp=="":
                    print("Trenutni maksimalni broj gostiju je " +lin[3]+ ",ako zelite da ga promenite upisite novi broj, a ako zelite da ostane isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        lin[3]=inp
                inp=""
                while inp=="":
                    print("Trenutna adresa je " +lin[4]+ ",ako zelite da je promenite upisite novu adresu, a ako zelite da ostane ista unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        lin[4]=inp
                inp=""
                while inp=="":
                    print("Trenutni poceci termina su redom " +lin[5]+ ",ako zelite da ih promenite upisite nove u istoj formi, a ako zelite da ostanu isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        dat=inp.split(",")
                        for datum in dat:
                            try:
                                datum=datum.split(".")
                                date=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
                            
                                
                            except:
                                print("Unesite datume u validnoj formi!")
                                inp=""
                                continue
                        lin[5]=inp
                inp=""   
                while inp=="":
                    print("Trenutni krajevi termina su redom " +lin[6]+ ",ako zelite da ih promenite upisite nove u istoj formi, a ako zelite da ostanu isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        dat=inp.split(",")
                        for datum in dat:
                            try:
                                datum=datum.split(".")
                                date=datetime.date(int(datum[2]),int(datum[1]),int(datum[0]))
                            
                                
                            except:
                                print("Unesite datume u validnoj formi!")
                                inp=""
                                continue
                        lin[6]=inp   
                inp=""
                while inp=="":
                    print("Trenutni cena po danu je " +lin[8]+ ",ako zelite da je promenite upisite novi broj, a ako zelite da ostane isti unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        lin[8]=inp
                inp=""
                while inp=="":
                    print("Trenutno stanje apartmana je " +lin[9]+ ",ako zelite da ga promenite upisite novo stanje, a ako zelite da ostane isto unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp.lower()=="aktivan" or inp.lower()=="neaktivan":
                        lin[9]=inp
                    else:
                        print("Status moze biti samo aktivan ili neaktivan, unesite validan status! ")
                        inp=""
                inp=""
                while inp=="":
                    print("Trenutna dodatna oprema u apartmanu je " +lin[10].strip()+ ",ako zelite da je promenite upisite novu listu dodante opreme sa zarezom izmedju oprema, a ako zelite da ostane ista unesite x: ")
                    inp=input("")
                    if inp[0].lower()=="x":
                        break
                    elif inp!="":
                        equip=inp.split(",")
                        for item in equip:
                            isEquip=checkEquip(item)
                            if isEquip==False:
                                print("Molimo vas unesite validnu dodatnu opremu!")
                                inp=""
                                continue
                        lin[10]=inp
                break
            else:
                j=j+1
        newfile="".join(lines[:j])+"|".join(lin)+"".join(lines[j+1:])
    with open(path1,"w",encoding ="utf-8") as file:
        file.write(newfile)   
    backToMenu(1,user)

def mostPop(role,user):
    lista=[]
    cities=[]
    dict={}
    with open(path3,encoding ="utf-8") as file:
        lines=file.readlines()
        for line in lines:
            if line == "\n":
                break
            line=line.split("|")
            lista.append(line[0])
    with open(path1,encoding ="utf-8") as file:
        lines=file.readlines()
        for  item in lista:
            for line in lines:
                if line == "\n":
                    break
                line=line.split("|")
                if line[0]==item:
                    city=line[4].split(",")
                    cities.append(city[1])
    for city in cities:
        if city in dict:
            dict[city]+=1
        else:
            dict[city]=1
    sortedValues=sorted(dict.values(),reverse=True)
    sortedDict={}

    for value in sortedValues:
        for key in dict.keys():
            if dict[key] == value:
                sortedDict[key]=dict[key]
    print("Grad " + 20*" "+"| Broj rezervacija")
    i=0
    for key,value in sortedDict.items():
        print("{:25s}|{:10d}".format(key, value))
        i+=1
        if i > 10:
            break
    
    backToMenu(role,user)


def newLogin():
    user=login()
    role=checkRole(user)
    menu(role,user)    

if __name__ == "__main__":
    #newLogin()
    mostPop(1,"savob")
    
    
