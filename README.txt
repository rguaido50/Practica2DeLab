Universidad Simon Bolivar
Redes definidas por Software
Raul Guaido 16-10486
Profesora: Emma Di Battista

Practica 2 Python & Git

El programa realiza una consulta a la api de meraki y lista las organizaciones a las 
que se tiene acceso, esto se hace mediante el uso de la operacion GET. 

Se solicito hacer un inventario de los devices de tipo appliance y wireless, para 
esto se utilizo la operacion GET nuevamente. Se listarion estos dispositivos con
informacion solicitada. Los devices son guardados en un archivo .csv que no sera 
compartido en el repositorio. 
Para obtener los dispositivos debe ingresar, de la lista mostrada, de que 
organizacion desea adquirir la informacion de los devices.

Se Agrego la Solicitud de verificar que el programa esta obteniendo la 
respuesta deseada.

Se obtiene mediante la funicon get la lista de las organizaciones de
meraki, son guardadas y luego mostradas al usuario para que pueda 
seleccionar de que organizacion desea obtener la lista de los dispositivos
luego se obtiene esta lista mediante get y son guardadas en un .csv

Para finalizar luego de cada solicitud se hace una validacion de esta.
