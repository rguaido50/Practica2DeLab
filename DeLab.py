#Universidad Simon Bolivar
#Redes definidas por Software
#Raul Guaido 16-10486
#Practica 2 Python & Git

import os 
import pprint
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
