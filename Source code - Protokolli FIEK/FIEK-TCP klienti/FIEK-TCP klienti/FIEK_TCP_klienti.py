from socket import *
import sys

print('============================================')
print('Programi: FIEK-TCP klienti')
print('============================================')

# i percaktohet klientit hosti: localhost dhe porti: 11000
serverName = 'localhost'
serverPort = 11000

# krijimi i socketit te klientit,
# ku parametri i dyte i socketit tregon se kemi te bejme me nje TCP socket:
s = socket(AF_INET, SOCK_STREAM)

# te protokolli TCP ne menyre qe te komunikojne klienti dhe serveri se pari duhet te vendoset nje lidhje nepermjet tyre: 
s.connect((serverName,serverPort))

kerkesa = "sample"

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
            # behet enkodimi i kerkeses dhe dergimi tek TCP serveri
            s.sendall(str(kerkesa).encode())
        else:
            break
        # ketu behet pranimi i pergjigjes nga serveri dhe dekodimi i saj
        # madhesia me e madhe qe mund tw mirret eshte 128 byte
        data = s.recv(128)
        print('Te dhenat e pranuara nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------------\n")
    except Exception as e:
        print(str(e))
        break
    
s.close()   # mbyllet lidhja