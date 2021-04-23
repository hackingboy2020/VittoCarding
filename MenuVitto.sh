#!/bin/bash
clear

cian="\033[1;36m"
blanco="\033[1;37m"
rojo="\033[1;31m"

echo -e $blanco"
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
            
            \033[1;33mCreado por hackingboy2020"

echo -e $cian
echo -e "\033[1;37m()----> \033[1;36mDedicado a TaylerVitto "
echo -e "\033[1;37m()----> \033[1;36mCanal de su YT: https://www.youtube.com/channel/UC1NpqO-QGzr_K-rQGnF_g5w " 


echo -e $rojo" " 
echo
echo -e "\033[1;37m()----> \033[1;31mOpcion (1): Generador de CC, esta opción te permite generar cc mediante bins."
echo
echo
echo -e "\033[1;37m()----> \033[1;31mOpcion (2): Informacion de un BIN, esta opcion te arroja la informacion de un bin "
echo
echo
echo -e "\033[1;37m()----> \033[1;31mOpcion (3): Extrapolacion, es un método de no quemar un BIN, o sacarle el BIN a una tarjeta real."
echo
echo
echo -e "\033[1;37m()----> \033[1;31mOpcion (4): FuerzaBruta a tarjetas CC, genera del 001-999 para adivinar el ccv"
echo
echo
echo -e "\033[1;37m()----> \033[1;31mOpcion (5): IpTracker, Esta opcion es extra y sirve para trackear una ip"
echo
echo
echo

read -p "()----> Elije una opcion del 1-5: " menuvitto

if [ $menuvitto = 3 ]; then
cd VittoScr && bash extrapolacion.sh
fi

if [ $menuvitto = 4 ]; then
cd VittoScr && python3 FuerzaBruta.py
fi

if [ $menuvitto = 5 ]; then
cd VittoScr && python VittoTracker.py
fi

if [ $menuvitto = 1 ]; then
cd VittoScr && python3 VittoUWU.py --tool CC-GEN
fi

if [ $menuvitto = 2 ]; then
cd VittoScr && python3 VittoUWU.py --tool BIN-INFO
fi
