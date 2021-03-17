import csv
import json
import pickle as pkl
import helpers

# Loads json with complete neo json
neos = []
with open('data/neos.csv') as f:
    reader = csv.DictReader(f)
    for elem in reader:
        neos.append(elem)

# Loads pkl file that loads dictionary with cad organized by designation
with open('cad_by_des.pkl', 'rb') as f:
    cad = pkl.load(f)


# Retrieve neo by either name or pdes
def get_neo(neos=neos, pdes=None, name=None):
    if pdes:
        for object in neos:
            if object['pdes'] == pdes:
                t = object
    if name:
        for object in neos:
            if object['name'] == name:
                t = object
    return t


# retrieve neo attributes from carrier objects from
# get_neo to be used to build attributes
def get_neo_attr(carrier):
    class_attr = {}
    class_attr['designation'] = carrier['pdes']

    if carrier['name'] == '':
        class_attr['name'] = None
    else:
        class_attr['name'] = carrier['name']

    if carrier['diameter'] == '':
        class_attr['diameter'] = float('nan')
    else:
        class_attr['diameter'] = float(carrier['diameter'])

    if carrier['pha'] == 'Y':
        class_attr['hazardous'] = True
    else:
        class_attr['hazardous'] = False
    return class_attr


# From close approach object extracted form organized
# dictionary, parse and pass data to
# object that can easily be passed to class object dictionary.
def get_cad_attr(cad=cad, pdes=None):
    cad_attr = {}
    cad_object = cad[pdes][0]
    cad_attr['time'] = helpers.cd_to_datetime(cad_object['cd'])
    cad_attr['distance'] = float(cad_object['dist'])
    cad_attr['velocity'] = float(cad_object['v_rel'])
    cad_attr['_designation'] = cad_object['des']
    return cad_attr
