# !/usr/bin/python
# coding:utf-8

import os, stat, time

#Ruta
path_to_explore="./Ejercicio_walk/"

#Variable file_size(tamaño)
file_size=0

#Dia actual
dia=int(time.strftime("%y"))
        
#Muestra la ruta de todo  
for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		
		#Muestra la ruta con el nombre de archivo
		name_path=os.path.join(root, name)
        
		#Muestra el tamaño del archivo
		file_size=os.stat(name_path).st_size
        
		#Muestra la fecha del ultimo acceso
		last_access=time.ctime(os.path.getatime(name_path))
 
        
		#Para ver cual pesa mas de 1gb y tenga 1 año o mas de tiempo
		if ((file_size > 2**30) and (all_time >= 1 or all_time < 0)):
			
			#Muestra de vuelta la ruta del archivo
			print(name_path) ,
			
			#Muestra lo que pesa
			print "este archivo pesa" ,
			#Peso en GB.
			size = os.stat(name_path).st_size / 1073741824
			print size
			print "GB"	
			#Muestra la ultima modificacion
			print last_access
			print ""
