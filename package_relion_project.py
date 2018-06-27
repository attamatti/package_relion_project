#!/usr/bin/env python

# Matt Iadanza
# Astbury Centre for Structural Molecular Biology
# University of Leeds
# Leeds, LS2 9JT
# please acknowledge if you find this script useful!

import sys
import subprocess

###---------function: read the star file get the header, labels, and data -------------#######
def read_starfile(f):
    alldata = open(f,'r').readlines()
    labelsdic = {}
    data = []
    header = []
    for i in alldata:
        if '#' in i:
            labelsdic[i.split('#')[0]] = int(i.split('#')[1])-1
        if len(i.split()) > 3:
            data.append(i.split())
        if len(i.split()) < 3:
            header.append(i.strip("\n"))
    return(labelsdic,header,data)
#---------------------------------------------------------------------------------------------#

if len(sys.argv) != 2:
    sys.exit('USAGE: package_relion_project.py <star file>')

# get the starfile - figure out which particle images ar needed
(labels,header,data) = read_starfile(sys.argv[1])
partfiles = []
for i in data:
    if i[labels['_rlnImageName ']].split('@')[-1] not in partfiles:
        partfiles.append(i[labels['_rlnImageName ']].split('@')[-1])

# make the packet
count = 0
manifest = open('TMP-manifest.txt','w')
for i in partfiles:
    manifest.write('{0}\n'.format(i))
    count +=1
manifest.write('{0}\n'.format(sys.argv[1]))
manifest.close()
print("\nMaking archive relion_packet.tar.gz")
subprocess.call(['tar','cfz','relion_packet.tar.gz','--files-from','TMP-manifest.txt'])
print("Packed {0} files".format(count))

#clean up
subprocess.call(['rm','TMP-manifest.txt'])
print('Finished successfullly')

# report back to user
print('''
Copy relion_packet.tar.gz to your project directory
then run the command:
        tar xvf relion_packet.tar.gz''')
