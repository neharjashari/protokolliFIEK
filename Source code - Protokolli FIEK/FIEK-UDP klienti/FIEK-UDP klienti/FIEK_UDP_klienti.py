from socket import *

print('============================================')
print('Programi: FIEK-UDP klienti')
print('============================================')

serverName = 'localhost'
serverPort = 11000

# krijohet socketi i klientit, ku parametri i pare tregon familjen e ip adresave
# kurse parametri i dyte tregon se tipi i socketit eshte UDP socket
s = socket(AF_INET, SOCK_DGRAM)

print("Jeni lidhur ne serverin ",serverName," ne portin ",serverPort)
print("========================================================================================================================================\n")

# MENYJA e programit 
print("""Jeni te lidhur me serverin!

       Cilat nga keto metoda deshironi ti perdorni: 
               
       1.IPADDR                        - Percakton dhe kthen IP adresen e klientit
               
       2.PORTNR                        - Percakton dhe kthen portin e klientit
               
       3.ZANORE {hapesire} teksti      - Merr si parameter nje tekst dhe kthen numrin e zanoreve ne ate tekst
               
       4.PRINTO {hapesire} teksti      - Merr si parameter nje tekst dhe kthen fjaline e shtypur dhe te formatuar 
                                         nga hapesirat e teperta
               
       5.HOST                          - Kerkon emrin e hostit dhe e kthen ate
               
       6.TIME                          - Kthen kohen aktuale ne server
               
       7.LOJA                          - Kthen vargun e 20 numrave "random" te rangut [1,99]
               
       8.FIBONACCI {hapesire} numri    - Gjen numrin Fibonacci si rezultat i parametrit te dhene
               
       9.KONVERTO {hapesire} opcioni {hapesire} vlera    - Kthen si rezultat konvertimin e parametrit hyres sipas ketyre opcioneve: 
                                                            CelsiusToKelvin, CelsiusToFahrenheit, KelvinToFahrenheit
                                                            KelvinToCelsius, FahrenheitToCelsius, FahrenheitToKelvin
                                                            PoundToKilogram, KilogramToPound.
               
       10.QUADRATIC {hapesire} vleraA {hapesire} vleraB {hapesire} vleraC  
                                
                                       - Merr si parameter vlerat e ekuacionit kuadratik (a, b, c) dhe kthen 
                                         zgjidhjet e atij ekuacioni
               
       11.ROLLTHEDICE                  - Kthen dy vlera "random" te dy zareve te gjuajtura

               
               Sheno EXIT per te dalur nga programi!
========================================================================================================================================              
               """)


while 1:
    try:
        kerkesa = input('Shkruaj emrin e metodes dhe argumentin perkates: ')
        if kerkesa!="" and kerkesa.upper()!="EXIT":
            # dergojme kerkesen ne server duke e percaktuar adresen e cakut
            s.sendto(str(kerkesa).encode(), (serverName, serverPort))
        else:
            break
        # pranohet pergjigja nga serveri
        data, serverAddress = s.recvfrom(128)
        print('Te dhenat e pranuara nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------------\n")
    except Exception as e:
        print(str(e))
        break

s.close()   # mbyllet lidhja
