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
import time

#Headers, url y payload
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}
payload = None

#url para consultas
urlname = "https://api.meraki.com/api/v1/organizations"
urlID = "https://api.meraki.com/api/v1/organizations/organizationId/devices/statuses"

#Funcion para obtener el ID de DeLab
def obtid(archivo_json):
    organizations_list = []
    for organization in archivo_json:
        organizations_list.append(organization['name'])
    OrgID = []
    for i in range(len(organizations_list)):
        if(archivo_json[i]['name'] == 'DeLab'):
            OrgID.append(archivo_json[i])
    OrgID.append(0)
    return OrgID

#Funicon para obtener las organizaciones
def obtname():
    response = requests.get(urlname, headers = headers, data = payload)
    #Validamos que la solicitud se realizo correctamente
    if(response.raise_for_status()==None):
        print("La consulta fue realizada correctamente.")
    else:
        exit()
    organizations = response.text.encode('utf8')
    organizations_json = response.json()
    return organizations_json

def obtdevice(listaID):
    url = listaID[0]['id']
    urlorg = urlID.replace("organizationId", url)
    response = requests.get(urlorg, headers = headers, data = payload)
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
    return
###Funcion Principal(se repite cada 5 min)
timer = 0
while True:
    clock = time.time()
    if(clock - timer > 300):
        timer = time.time()
        orgname = obtname()
        IDorg = obtid(orgname)
        listdevice = obtdevice(IDorg)
        print("Se ha actualizado la lista de dispositivos en la red")
