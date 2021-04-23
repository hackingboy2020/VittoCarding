#!/usr/bin/env python3

import os, time, sys, datetime
from random import randint
from huepy import *

XD = 18

def cc_gen(bin):

    cc = ""

    if len(bin) != 16:

        while len(bin) != 16:
            bin += 'x'

    else:
        pass

    if len(bin) == 16:

        for x in range(15):

            if bin[x] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                cc += bin[x]
                continue

            elif bin[x] in ('x'):
                cc += str(randint(0,9))

            else:
                print(bad(f"Formato invalido: {bin}"))
                sys.exit()


        for i in range(10):
            check_cc = cc
            check_cc += str(i)

            if ValidCC(check_cc):
                cc = check_cc
                break
            else:
                check_cc = cc

    else:
        print(bad(f"Formato Invalido: {bin}"))

    return(cc)

def ValidCC(card_number): 
    
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )


def dategen(month, year):

    if month == 'rnd' and year == 'rnd':
        now = datetime.datetime.now()
        month = int(randint(1, 12))
        current_year = str(now.year)
        year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))

        if month < 10:
            month = '0'+str(month)
        
        else:
            month = str(month)

        date = month + "|" + year
        return date

    elif month == 'rnd' and year != 'rnd':
        now = datetime.datetime.now()
        month = int(randint(1,12))

        if month < 10:
            month = '0'+str(month)
        
        else:
            month = str(month)

        date = month + "|" + year
        return date

    elif month != 'rnd' and year == 'rnd':
        now = datetime.datetime.now()
        current_year = str(now.year)
        year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
        date = month + "|" + year
        return date

    elif month != 'rnd' and year != 'rnd':
        date = month + "|" + year
        return date

def ccvgen(cvv):
        
    if cvv == 'rnd':

        ccv = ""
        num = randint(10,999)

        if num < 100:

            ccv = "0" + str(num)
        
        else:
            ccv = str(num)

        return(ccv)

    else:
        return(cvv)

def clean():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('clear')

def banner():
    print("""\033[1;37m
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
            0:.SX ;ai, 7   :: iS. 8i  i;           V V     I       T           T      O     O
           2X 7 rr.iXi,:rXX;,:r;i;iiX  2r           V      I       T           T       O O O
          iW X   :;,.7.. ..,.;i;;:  iX  M.        
          M X      .iiX::i::S7S,     X. Br        
          M ,       ;,XX7SXXX,,      S  M         
          S0        i :     : ..    S  Z2         
           @M:   .:i  ,:   :   ;;;::iiM0          
        :72XXBW88SXXi  :i..;X2SXXrSXrrS72Xi       
     :7ri:       r:i;r;,  ,07, ..:;      ,ii.     
     B                 ,;X2                 ri    
    .a                   X                  :2  
                                
            \033[1;33mCreado por hackingboy2020
                
                \033[1;31mGenerador de CC \n""")
print( )
def main():
    
    clean()
    banner()

    print( )
    try:

        seses = int(input("\033[1;37m()----> \033[1;31mCantidad de cc :  "))
        counter = 0

        BIN = input("\033[1;31m()----> \033[1;37mEscribe el BIN: ")
        MONTH = input("Mes [MM / RND] > ").lower()
        YEAR = input("Año [YY / RND] > ").lower()
        CVV = input("CVV [CVV / RND] > ").lower()

        month = MONTH
        year = YEAR

        clean()
        banner()
        
        while counter != seses:
            print(good(cc_gen(BIN) + "|" + dategen(month, year) + "|" + ccvgen(CVV)))
            counter +=1

    except:
        print(bad(yellow("Error")))
        sys.exit()

if XD == 2:
    print(info(lightred(("Error"))))
    
else:
    main()

print( )
menu_vitto_2 = input("\033[1;37m()----> \033[1;31mQuieres volver al menu? Escribe si/no: \033[1;37m")

if [ menu_vitto_2 == 'si' ]:
  os.system("cd .. && bash MenuVitto.sh")


