#!/usr/bin/python3
import os, sys

###########################################################
# Es wird nicht abgefragt ob die Ordner bereits existieren#
###########################################################

#>> Diesen Pfad anpassen
path = 'YOUR PATH'
#>> Anzahl der Ordner
targetx = 14

#Ordnername
folder_name_main = 'Uni Stuff/'
#Unterordnername
folder_name_sub1 = 'Mathe-Vorkurs/'
#Unterordnername 2
folder_name_sub2 = 'Tag '
#Unterstruktur
folder_name_struc = ['Anaconda', 'PDF']

var_struc = len(folder_name_struc)-1

try:
    os.mkdir(path+folder_name_main)
    os.mkdir(path+folder_name_main+folder_name_sub1)

    x = 1
    while x <= targetx:
        os.mkdir(path+folder_name_main+folder_name_sub1+folder_name_sub2+str(x))
        os.mkdir(path+folder_name_main+folder_name_sub1+folder_name_sub2+str(x)+'/'+str(folder_name_struc[0]))
        os.mkdir(path+folder_name_main+folder_name_sub1+folder_name_sub2+str(x)+'/'+str(folder_name_struc[1]))
        x += 1

except OSError:
    print('Ordner wurde nicht erstellt')
else:
    print('Erfolgreich')
