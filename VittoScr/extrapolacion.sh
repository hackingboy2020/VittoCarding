#!/bin/bash
clear

amarillo="\033[1;33m"
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
    
            \033[1;33mCreado por hackingboy2020
    "


echo " "
echo -e $rojo" "
read -p "----> Escribe la CC a extrapolar : " Extrapolacion
echo -e $blanco" "
echo -e "$rojo----> $blanco${Extrapolacion:0:12}xxxx "
echo -e "$rojo----> $blanco${Extrapolacion:0:11}xxxxx "
echo -e "$rojo----> $blanco${Extrapolacion:0:8}xxxx${Extrapolacion:12:1}x${Extrapolacion:14:16} "
echo -e "$rojo----> $blanco${Extrapolacion:0:10}xxxxxx "
echo -e "$rojo----> $blanco${Extrapolacion:0:6}x${Extrapolacion:7:1}x${Extrapolacion:9:1}x${Extrapolacion:11:1}x${Extrapolacion:13:1}x${Extrapolacion:15:1} "

echo -e $amarillo " "
read -p "()> Quieres volver al menu? Escribe Si/No: " MenuVolver



if [ $MenuVolver = Si ]; then
cd .. && bash MenuVitto.sh
fi

if [ $MenuVolver = si ]; then
cd .. && bash MenuVitto.sh
fi