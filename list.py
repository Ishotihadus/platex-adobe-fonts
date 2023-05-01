import xml.etree.ElementTree as ET
import os
from tabulate import tabulate
from fontTools import ttLib

base_path = os.environ.get('HOME') + '/Library/Application Support/Adobe/CoreSync/plugins/livetype'

tree = ET.parse(f'{base_path}/.c/entitlements.xml')
root = tree.getroot()

data = []

for f in root.find('fonts').iter('font'):
    id = f.find('id').text
    file_name = f'.{id}.otf'
    full_name = f.find('properties').find('fullName').text

    path = None
    for s in ['r', 'w']:
        if os.path.isfile(f'{base_path}/.{s}/{file_name}'):
            path = f'{base_path}/.{s}/{file_name}'
            break
    if path is None:
        continue

    font = ttLib.TTFont(path)
    postscript_name = font['name'].getName(nameID=6, platformID=3, platEncID=1).toStr()

    data.append([file_name, full_name, postscript_name])


data = sorted(data, key=lambda x: x[1])

print(tabulate(data, headers=['File name', 'Font name', 'Postscript Name'], tablefmt='orgtbl'))
