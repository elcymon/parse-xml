# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
import ntpath
import os

resultFolder = 'CSVresults'
os.makedirs(resultFolder,exist_ok=True)

world_db = '/home/elcymon/containers/swarm_sim/sources/w_swarm1/world_db/'
worldFiles = glob(world_db + '*.world')

def getnameXYyaw(model):
    name = model.find('name').text
    pose = model.find('pose').text.split(' ')
    
    return [name,pose[0],pose[1],pose[-1]]

count = 0
for world in worldFiles:
    worldName = ntpath.basename(world).replace('.world','')
    
    tree = ET.parse(world)
    root = tree.getroot()
    modelsDF = pd.DataFrame(columns=['name','x','y','yaw'])
    for model in root.iter('include'):
        if model.find('name') != None:
            if 'litter' in model.find('name').text or 'robot' in model.find('name').text:
                modelsDF.loc[len(modelsDF)] = getnameXYyaw(model)
    print(len(modelsDF))
#    modelsDF.sort_values(by = 'name',inplace=True)
    modelsDF.to_csv(os.sep.join([resultFolder,worldName + '.csv']),index=False)
    count += 1
    print('{}/{} {}'.format(count,len(worldFiles),worldName))
