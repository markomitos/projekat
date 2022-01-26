#projekat Marko Mitosevic SV'56

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
                    if line[7]=="admin":
                        return 2
                    elif line[7]=="domacin":
                        return 1
                    else:
                        return 0

def menu(role,user):
    if role==0: #admin
        menuAdmin(role)
    elif role==1:#domacin
        menuLandlord(role,user)
    else:#gost
        menuGuest(role)

def menuAdmin(role):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9,10,11,12]
    while inp not in validinput:
        print("="*150)
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
        print("="*150)
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
        print("Unesite validnu opciju!")
    if inp==1:
        listApart(role)
    elif inp==2:
        searchApart(role)
    elif inp==3:
        multiSearchApart(role)
    elif inp==4:
        mostPop(role)
    elif inp==5:
        searchRes(role)
    elif inp==6:
        newLandLord()
    elif inp==7:
        newEquip()
    elif inp==8:
        delEquip()
    elif inp==9:
        blockUser()
    elif inp==10:
        analitics()
    elif inp==11:
        login()
    elif inp==12:
        exit()

def menuLandlord(role,user):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9,10,11]
    while inp not in validinput:
        print("="*150)
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
        print("="*150)
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
        print("Unesite validnu opciju!")
    if inp==1:
        listApart(role)
    elif inp==2:
        searchApart(role)
    elif inp==3:
        multiSearchApart(role)
    elif inp==4:
        mostPop(role)
    elif inp==5:
        newApart(user)
    elif inp==6:
        editApart(user)
    elif inp==7:
        delApart(user)
    elif inp==8:
        listRes(user)
    elif inp==9:
        approveRes(user)
    elif inp==10:
        login()
    elif inp==11:
        exit()

def menuGuest(role):
    inp=0
    validinput=[1,2,3,4,5,6,7,8,9]
    while inp not in validinput:
        print("="*150)
        print("1. Pregled aktivnih apartmana")
        print("2. Pretraga apartmana")
        print("3. Visekriterijumska pretraga apartmana")
        print("4. Prikaz 10 najpopularnijih gradova")
        print("5. Rezervisanje apartmana")
        print("6. Pregled rezervacija")
        print("7. Ponistavanje rezervacija")
        print("8. Odjava")
        print("9. Izlaz")
        print("="*150)
        inp = eval(input("Unesite broj ispred opcije koju zelite da odaberete: \n"))
        if inp in validinput:
            break
        print("Unesite validnu opciju!")
    if inp==1:
        listApart(role)
    elif inp==2:
        searchApart(role)
    elif inp==3:
        multiSearchApart(role)
    elif inp==4:
        mostPop(role)
    elif inp==5:
        resApart()
    elif inp==6:
        listRes()
    elif inp==7:
        delRes()
    elif inp==8:
        login()
    elif inp==9:
        exit()

def listApart(role):
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
        backToMenu(role)

def displayHeader():
    print(150*"=")
    print("\tSifra\tTip\tBroj Soba|Broj gostiju\tAdresa\t\t\t\t\tDospupnost apartmana\t\tDomacin\t\tDnevni zajam\tDodaci")

def backToMenu(role):
    unos=" "
    while unos[0] != "d" or unos[0] != "n":
        unos=input("Da li zelite da se vratite u meni?(Da/Ne)\n").lower().strip()
        if unos[0]== "d":
            menu(role)
        elif unos[0]=="n":
            exit()
        print("Pogresan unos! Molimo vas da unesete Da ili Ne:")
        
def searchApart(role):
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
    backToMenu(role)

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

def multiSearchApart(role):
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
        unos=input("Da li zelite da postavite jos kriterijuma zaz pretragu?(Da/Ne)").lower().strip()
        while unos[0] != "d" or unos[0] !="n":
            if unos[0]=="d":
                break
            elif unos[0]=="n":
                stop=True
                break
            print("Molimo vas unesite da ili ne!")
            
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
        line = line.split("|")
        if line[9]=="aktivan":
            if unos<int(line[i]):
                templist=templist.append(line)

def numLowerM(unos,equal,i,lines):
    if equal==True:    
        unos-=1
    templist=[]
    for line in lines:
        line = line.split("|")
        if line[9]=="aktivan":
            if unos>int(line[i]):
                templist=templist.append(line)




def delEquip():
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
    backToMenu(0)     

def checkEquipRes(user):
    with open(path1,encoding ="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line=line.split("|")
            equip=line[10].split(",")
            for i in equip:
                if user==i.strip():
                    return True


def newEquip():
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
    backToMenu(0)


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

def newLandLord():
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
                return user

        else:
            print("Dato korisnicko ime je vec u upotrebi!")

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


def blockUser():
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
    print("Dati korisnik je uspesno obrisan")


    backToMenu(2)

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
        

if __name__ == "__main__":
    #user=login()
    #role=checkRole(user)
    #menu(role,user)
    listApart("savob")
    
