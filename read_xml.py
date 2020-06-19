import sys

from pprint import pprint

import json
import xmltodict

with open(sys.argv[1],"r") as f:
    xmlString = f.read()

info = xmltodict.parse(xmlString)

info = info['verilator_xml']['netlist']
info_output = {}
info_output['name'] = info['module']['@name']

port_type = {}
for i in info['typetable']['basicdtype']:
    if('@left' in i.keys()):
        port_type[i['@id']] = {'type':i['@name'], 'msb':int(i['@left']), 'lsb':0}
    else:
        port_type[i['@id']] = {'type':i['@name'], 'msb':0, 'lsb':0}

port_list = []
for i in info['module']['var']:
    port_list.append( 
        {"name":i['@name'],
         "direction":i['@dir'],
         "dtype":port_type[ i['@dtype_id'] ] 
        } 
    )

info_output['port_list'] = port_list


jsonString = json.dumps(info_output, indent=4)

#print(jsonString)

with open(sys.argv[1][:-3]+'json',"w") as f:
    f.write(jsonString)