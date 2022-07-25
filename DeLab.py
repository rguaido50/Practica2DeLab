#Universidad Simon Bolivar
#Redes definidas por Software
#Raul Guaido 16-10486
#Practica 2 Python & Git

import os 
import pprint
from pprint import pp
import requests 
import json
import csv

#1. Solicitan una función para listar todas las organizaciones a las que tiene usted acceso con el API Key.

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.get(url, headers = headers, data = payload)
#Validamos que la solicitud se realizo correctamente
if(response.raise_for_status()==None):
    print("La consulta fue realizada correctamente.")
else:
    exit()


organizations = response.text.encode('utf8')
#pprint(organizations)
organizations_json = response.json()
#pprint(organizations_json)
#Guardamos en una lista las organizaciones
organizations_list = []
for organization in organizations_json:
    organizations_list.append(organization['name'])
print('Lista de organizaciones: ')
pp(organizations_list)

#3. Solicitu de Inventariar todos los dispositivos en la red
#Agregamos que organizacion queremos. 
nameOrg = input("Ingrese el nombre de la organización que desea consultar:")
#De la organizacion deseada obtenemos el ID para el GET
OrgID = []
for i in range(len(organizations_list)):
    if(organizations_json[i]['name'] == nameOrg):
        OrgID.append(organizations_json[i])
    OrgID.append(0)
  
urlID = OrgID[0]['id']
urlorg = "https://api.meraki.com/api/v1/organizations/organizationId/devices/statuses"
url1 = urlorg.replace("organizationId", urlID)
payload1 = None

headers1 = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.get(url1, headers = headers1, data = payload1)
#pprint(response.json())

#Validamos que la solicitud se realizo correctamente
if(response.raise_for_status()==None):
    print("La consulta fue realizada correctamente.")
else:
    exit()

response_list = response.json()
#Creamos las listas de los devices
wireless_list = []
appliance_list = []
#Guardamos los dispositivos en las listas
for device in response_list:
    if device['productType'] == 'wireless':
        wireless_list.append(device)
    if device['productType'] == 'appliance':
        appliance_list.append(device)

#print(wireless_list)
#print(appliance_list)

features = ['modelo','nombre','MAC','IPpub','IPLAN','numSerial','status']

with open("Dispositivos.csv", 'w') as f:
    writer_f = csv.writer(f)
    writer_f.writerow(features)
    f.close()

for device in wireless_list:
    device_feature = []
    device_feature.append(device['productType'])
    device_feature.append(device['model'])
    device_feature.append(device['name'])
    device_feature.append(device['mac'])
    device_feature.append(device['publicIp'])
    device_feature.append(device['lanIp'])
    device_feature.append(device['serial'])
    device_feature.append(device['status'])
    with open("Dispositivos.csv", 'a', newline = '') as f:
        writer_f = csv.writer(f)
        writer_f.writerow(device_feature)
    f.close()


for device in appliance_list:
    device_feature = []
    device_feature.append(device['productType'])
    device_feature.append(device['model'])
    device_feature.append(device['name'])
    device_feature.append(device['mac'])
    device_feature.append(device['publicIp'])
    device_feature.append(device['wan1Ip'])
    device_feature.append(device['serial'])
    device_feature.append(device['status'])
    with open("Dispositivos.csv", 'a', newline = '') as f:
        writer_f = csv.writer(f)
        writer_f.writerow(device_feature)
    f.close()

