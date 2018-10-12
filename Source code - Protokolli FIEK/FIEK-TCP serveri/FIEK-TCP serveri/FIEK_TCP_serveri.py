from socket import *
import random
import datetime
import sys
import threading
import cmath

print('============================================')
print('Programi: FIEK-TCP serveri')
print('============================================')

# Ndahet porti 11000 per socketin e serverit:
serverPort = 11000

# krijohet socketi i serverit, sipas TCP protokollit:
serverSocket = socket(AF_INET, SOCK_STREAM)

# asociojme portin e serverit me socketin e krijuar:
serverSocket.bind(('',serverPort))


print('Serveri startoi ne localhost me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(serverPort)) 

# pasiqe te krijohet socketi i serverit te TCP protokolli presim per nje klient te lidhet me server:
serverSocket.listen(5)
 
print('Serveri eshte i gatshem te pranoj kerkesa...')


# METODAT: 
def IPADDR(address):
    return str(address[0])

def PORTNR(address):
    return str(address[1])

def ZANORE(teksti):
    numriZanoreve = 0
    zanoret = "aeiouyëAEIOUYË"
    for i in range(1, len(teksti)):
        if teksti[i] in zanoret:
            numriZanoreve +=1
    return str(numriZanoreve)

def PRINTO(teksti):
    teksti = str(teksti).strip()
    return teksti

def HOST():
    try:
        hosti = socket.gethostname()
        pergjigja = "Emri i hostit eshte: " + hosti
        return str(pergjigja)
    except:
        pergjigja = "Emri i hostit nuk mund te percaktohet!"
        return str(pergjigja)


def TIME():
    return str(datetime.datetime.now())

def LOJA():
    listaNumrave = []
    for i in range(20):
        listaNumrave.append(random.randint(1,99))
    listaNumrave.sort()
    return str(listaNumrave)

def FIBONACCI(vlera):
    numri = 1
    numripr = 0
    numriDhene = 0
    numriDhene = int(vlera)
    for i in range(numriDhene-1):
        numri = numri + numripr
        numripr = numri - numripr
    return str(numri)

def KONVERTO(tipi,vlera):
    vleraKonvertuar = 0
    vlera = float(vlera)

    if tipi=="CELSIUSTOKELVIN":
        return str(vlera+273.15)
    elif tipi=="CELSIUSTOFAHRENHEIT":
        return str((vlera*9.0/5.0)+32)
    elif tipi=="KELVINTOFAHRENHEIT":
        return str((9.0*(vlera-273.15)/5.0)+32)
    elif tipi=="KELVINTOCELSIUS":
        return str(vlera-273.15)
    elif tipi=="FAHRENHEITTOCELSIUS":
        return str(5.0*(vlera-32)/9.0)
    elif tipi=="FAHRENHEITTOKELVIN":
        return str(5.0*(vlera-32)/9.0+273.15)
    elif tipi=="POUNDTOKILOGRAM":
        return str(vlera*0.45359237)
    elif tipi=="KILOGRAMTOPOUND":
        return str(vlera/0.45359237)
    else:
        return "Error - Keni bere ndonje gabim gjate shenimit!"

def QUADRATIC(a, b, c):
    d = (b**2) - (4*a*c)
    x1 = (-b - cmath.sqrt(d))/(2*a)
    x2 = (-b + cmath.sqrt(d))/(2*a)
    pergjigja = str("Zgjidhjet e ekuacionit kuadratik jane: x1 = {:.2f} dhe x2 = {:.2f}").format(x1,x2)
    return pergjigja

def ROLLTHEDICE():
    min = 1
    max = 6
    kubi1 = str(random.randint(min, max))
    kubi2 = str(random.randint(min, max))
    pergjigja = str("Rolling the dice...        Vlerat e qelluara jane:   " + kubi1 + " dhe " + kubi2)
    return pergjigja

# te gjitha te dhenat qe dergohen te klienti kjo metode i printon edhe te serveri
def ShtypTeDhenat(teDhenat):
    print("\n----------------------------------------------------------------------------------------------")
    print("Te dhenat e derguara te klienti =>  ", teDhenat)
    return



# funksioni ku shfaqet klienti i ri ne server, ky funksion thirret tek threading
def klienti_i_ri(connectionSocket,addr):
    
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper()!="EXIT" and str(kerkesa.decode())!="":
            # pranimi i kerkeses nga klienti
            kerkesa = connectionSocket.recv(128)

            # dekodimi i kerkeses
            kerkesaStr = str(kerkesa.decode()).strip()

            # behet ndarja e kerkeses sipas hapesirave dhe ruhet ne njw Array
            kerkesaArray = kerkesaStr.split(' ')

            # kerkesa e derguar nga klienti kthehet se pari ne upperCase:
            kerkesaArray[0] = kerkesaArray[0].upper()

            # metoda IPADDR
            if kerkesaArray[0]=="IPADDR":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("IP adresa juaj eshte: "+IPADDR(addr)).encode())
                    ShtypTeDhenat(("IP adresa e klientit: "+IPADDR(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda PORTNR
            elif kerkesaArray[0]=="PORTNR":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Numri i portit tuaj eshte: "+PORTNR(addr)).encode())
                    ShtypTeDhenat(("Numri i portit te klientit eshte: "+PORTNR(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda ZANORE
            elif kerkesaArray[0]=="ZANORE":
                if len(kerkesaArray) == 2:
                    rezultati = "Numri i zanoreve ne fjalen e dhene eshte: " + ZANORE(kerkesaArray[1])
                    connectionSocket.send(rezultati.encode())
                    ShtypTeDhenat(rezultati)
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda PRINTO
            elif kerkesaArray[0]=="PRINTO":
                kerkesaStr2 = (str(kerkesaStr)).replace("PRINTO","")
                connectionSocket.send(("Fjalia e printuar: " + PRINTO(kerkesaStr2)).encode())
                ShtypTeDhenat(("Fjalia e printuar: " + PRINTO(kerkesaStr2)))
            # metoda HOST
            elif kerkesaArray[0]=="HOST":
                if len(kerkesaArray) == 1:
                    if HOST()=="Emri i hostit nuk mund te percaktohet!":
                        connectionSocket.send(("Emri i hostit nuk mund te percaktohet!").encode())
                        ShtypTeDhenat("Emri i hostit nuk mund te percaktohet!")
                    else:
                        connectionSocket.send(("Emri i klientit eshte: "+HOST()).encode())
                        ShtypTeDhenat(("Emri i klientit eshte: "+HOST()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda TIME
            elif kerkesaArray[0]=="TIME":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Koha e tanishme eshte: " + TIME()).encode())
                    ShtypTeDhenat(("Koha e tanishme eshte: " + TIME()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda LOJA
            elif kerkesaArray[0]=="LOJA":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Rezultati nga loja: " + LOJA()).encode())
                    ShtypTeDhenat(("Rezultati nga loja: " + LOJA()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda FIBONACCI
            elif kerkesaArray[0]=="FIBONACCI":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)==1 or len(kerkesaArray)>2:
                    connectionSocket.send(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode())
                    ShtypTeDhenat("ERROR")
                else:
                    connectionSocket.send(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])).encode())
                    ShtypTeDhenat(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])))
            # metoda KONVERTO
            elif kerkesaArray[0]=="KONVERTO":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                    connectionSocket.send(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode())
                    ShtypTeDhenat("ERROR")
                else:
                    konvertimi = str(kerkesaArray[1]).lower().split("to")
                    pergjigja = kerkesaArray[2] + " " + str(konvertimi[0]) + " jane te barabarte me " + KONVERTO(str(kerkesaArray[1]).upper(),kerkesaArray[2]) + " " + str(konvertimi[1])
                    connectionSocket.send(str(pergjigja).encode())
                    ShtypTeDhenat(pergjigja)
            # metoda shtese QUADRATIC - shkruan si parametra vlerat a,b,c te ekuacionti kuadratik dhe kthen zgjidhjet e tij.
            elif kerkesaArray[0]=="QUADRATIC":
                if len(kerkesaArray) == 4:
                    connectionSocket.send(str(QUADRATIC(kerkesa[1], kerkesa[2], kerkesa[3])).encode())
                    ShtypTeDhenat(str(QUADRATIC(kerkesa[1], kerkesa[2], kerkesa[3])))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda shtese ROLLTHEDICE - kthen vlerat e dy kubeve te gjuajtura.
            elif kerkesaArray[0]=="ROLLTHEDICE":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(str(ROLLTHEDICE()).encode())
                    ShtypTeDhenat(str(ROLLTHEDICE()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # nqs. nuk shkruhet asnjera nga metodat e percaktuara
            else:
                connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                ShtypTeDhenat("ERROR!")

            

        # kur largohet klienti mbyllet lidhja me te, por serveri ende pret per lidhje me klient te tjere
        connectionSocket.close()
    except Exception as e:
        print("\nERROR: ")
        print(str(e))
        connectionSocket.close()
    


# pranimi i kerkesave te njepasnjeshme nga klientet
while 1:
    # ky rresht ben qe serveri te "degjoj" per kerkesa nga klienti permes lidhjes TCP
    connectionSocket, addr = serverSocket.accept()
    print('Klienti me IP adrese %s dhe me numrin e portit %s eshte lidhur me server' %(addr))

    # krijimi i nje procesi te ri (threadi te ri), me lidhjen e nje klienti te ri
    threading._start_new_thread(klienti_i_ri,(connectionSocket,addr)) 