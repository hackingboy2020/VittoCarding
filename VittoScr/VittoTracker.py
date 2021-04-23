# Un simple IpTracker bien facha
# TaylerVitto




import urllib
import json
import os
import sys
from color import color


os.system("clear")

print('''\033[1;37m
                       
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
                                       

            \033[1;33mCreado por hackingboy2020''')           
print
print
ip = raw_input("\033[0;31m(-)=============>> \033[1;37mEscribe la IP : ")
 
url = 'http://ip-api.com/json/'
hackingboy2020 = urllib.urlopen(url + ip)
leer = hackingboy2020.read()
uwu = json.loads(leer)

color()
print(uwu)

print
menu_vitto_3 = raw_input("\033[1;37m()----> \033[1;31mQuieres volver al menu? Escribe si/no: \033[1;37m")

if [ menu_vitto_3 == 'si' ]:
  os.system("cd .. && bash MenuVitto.sh")



print('''\033[0;31m
                                                                                                                            
  __   _  _  ____    ____  ____    _  _   __   _  _  __     ____  __  ____  __ _    _  _   
 /  \ / )( \(  __)  (_  _)(  __)  / )( \ / _\ ( \/ )/ _\   (  _ \(  )(  __)(  ( \  (_)( \  
(  O )) \/ ( ) _)     )(   ) _)   \ \/ //    \ )  //    \   ) _ ( )(  ) _) /    /  ( ) ) ) 
 \__\)\____/(____)   (__) (____)   \__/ \_/\_/(__/ \_/\_/  (____/(__)(____)\_)__)  (/ (_/                                                     
  
\n''')
