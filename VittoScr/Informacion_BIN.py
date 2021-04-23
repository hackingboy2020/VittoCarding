import os, requests, json, sys
from time import sleep
from huepy import *

XDD = 19

API = "https://lookup.binlist.net/"

def Bin_Info():


    def banner():
        print("""\033[1;31m
                        :::.                      
                    .XXr;;;rrX7                   
                  iWa,        :@S                 
                 rM   .i;;i;;.  Mi                
                 @   aXi:,,,iZ  .M                
                i2  X.       i:  @i               
                a  ir   :r.   S  ,M               
               Xi  X.MM2. ,2MM8i  2Z              
              ;S  a;rXMMM @MMSiB.  Xr             
             ,8  2i.;:; : : ii;72   i,           V     V   I   T T T T T   T T T T T   O O O
             B .2      ,   ,     X.   ,           V   V    I       T           T      O     O
            0:.SX ;ai, 3   :: iS. 8i  i;           V V     I       T           T      O     O
           2X 3 rr.iXi,:rXX;,:r;i;iiX  2r           V      I       T           T       O O O
          iW X   :;,.3.. ..,.;i;;:  iX  M.        
          M X      .iiX::i::S7S,     X. Br        
          M ,       ;,XX7SXXX,,      S  M         
          S0        i :     : ..    S  Z2         
           @M:   .:i  ,:   :   ;;;::iiM0          
        :72XXBW88SXXi  :i..;X2SXXrSXrrS72Xi       
     :7ri:       r:i;r;,  ,07, ..:;      ,ii.     
     B                 ,;X2                 ri    
    .a                   X                  :2  
            
            \033[1;33mCreado por hackingboy2020
            
           \033[1;37mExtraer informacion de un bin \n""")

    
    def clean():

        if os.name == 'nt':

            os.system('cls')

        else:

            os.system('clear')

    def main():

        clean() 
        banner()
        
        try:
            
            BIN = input(" \033[1;31m()----> \033[1;37mEscribe el bin: \033[1;31m")
            clean(); banner()

            data = requests.get(API+BIN).json()
            sys.stdout.flush()

            print(info("\033[1;31mInformacion del BIN " +red(BIN + "\n")))
            sleep(0.3)
            print(good(red("----> Ciudad: " +yellow(data['country']['name']))))
            sleep(0.3)
            print(good(red("----> Esquema: " +yellow(data['scheme']))))
            sleep(0.3)
            print(good(red("----> Tipo: " +yellow(data['type']))))
            sleep(0.3)
            print(good(red("----> Marca: " +yellow(data['brand']))))
            sleep(0.3)
            print(good(red("----> Nombre del banco: " +yellow(data['bank']['name']))))
            sleep(0.3)
            print(good(red("----> Latitud: " +yellow(data['country']['latitude']))))
            sleep(0.3)
            print(good(red("----> Longitud: " +yellow(data['country']['longitude']))))
            sleep(0.3)
            print(good(red("----> Url del banco: " +yellow(data['bank']['url']))))
            sleep(0.3)
            print(good(red("----> Numero del banco: " +yellow(data['bank']['phone']))))
            sleep(0.3)
            print(good(red("----> Ciudad del banco: " +yellow(data['bank']['city'] + "\n"))))

            

        except:
            menu_vitto_5 = input("\033[1;37m()----> \033[1;31mQuieres volver al menu? Escribe si/no: \033[1;37m")

            if [ menu_vitto_5 == 'si' ]:
                os.system("cd .. && bash MenuVitto.sh")
            else:
                exit()


        

    main()


if XDD == 4:

    print(info(lightred(("An Error Ocurred..."))))

else:

    Bin_Info()

    