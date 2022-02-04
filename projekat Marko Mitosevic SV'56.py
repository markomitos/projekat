#projekat Marko Mitosevic SV'56
import datetime
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
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
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
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
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
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
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
                for part in line:
                    if part==line[9]:
                        continue
                    if part==line[8]:
                        display=display+"\t"
                    display = display +"\t"+ part
                print(display)
        print(150*"=")
        backToMenu(role,user)

def displayHeader():
    print(150*"=")
    print("\tSifra\tTip\tBroj Soba|Broj gostiju\tAdresa\t\t\t\t\tDospupnost apartmana\t\tDomacin\t\tDnevni zajam\tDodaci")

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
                    for part in line:
                        if part==line[8]:
                            display=display+"\t"
                        if part==line[9]:
                            continue
                        display = display +"\t"+ part
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
                    for part in line:
                        if part==line[9]:
                            continue
                        if part==line[8]:
                            display=display+"\t"
                        display = display +"\t"+ part
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
                    for part in line:
                        if part==line[9]:
                            continue
                        if part==line[8]:
                            display=display+"\t"
                        display = display +"\t"+ part
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
                    for part in line:
                        if part==line[9]:
                            continue
                        if part==line[8]:
                            display=display+"\t"
                        display = display +"\t"+ part
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
                    for part in line:
                        if part==line[9]:
                            continue
                        if part==line[8]:
                            display=display+"\t"
                        display = display +"\t"+ part
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
            display=""
            line = line.split("|")
            if line[7]==user:
                for part in line:
                    if part==line[9]:
                        continue
                    if part==line[8]:
                        display=display+"\t"
                    display = display +"\t"+ part
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
                for part in line:
                    if part==line[9]:
                        continue
                    if part==line[8]:
                        display=display+"\t"
                    display = display +"\t"+ part
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
        listStatus("prihvacena")
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


def newLogin():
    user=login()
    role=checkRole(user)
    menu(role,user)    

if __name__ == "__main__":
    #newLogin()
    listResL("savob")
    
        
    
