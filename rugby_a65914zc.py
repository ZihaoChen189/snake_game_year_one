import argparse
import os
from pathlib import Path
parser = argparse.ArgumentParser(description='')
parser = argparse.ArgumentParser(description='')
parser.add_argument('path', metavar='p', type=str, nargs='+')
parser.add_argument('path1', metavar='p', type=str, nargs='+')
args = parser.parse_args()
path = Path(args.path[0])
Listread = []
for p in path.glob('*'):
    Listread.append(str(p))
for x in Listread:
    Lista = []
    Listb = []
    with open(x,'r') as file:
        content=(''.join(file.read())).strip('\n')
    Document=content.split('T')  
    for a in Document:
        find = a.find('1')
        if find == 0:
            Lista.append(''.join(a.split('1')))
        else:
            Listb.append(''.join(a.split('2')))
    List1 = ['t','c','p','d']
    Score = [5,2,3,3]
    Sum1 = 0
    Sum2 = 0
    for a in Lista:
        for y in List1:
            if str(a)==str(y):
                Sum1 += Score[List1.index(y)]
    for b in Listb:
        for w in List1:
            if str(b)==str(w):
                Sum2 += Score[List1.index(w)]
    d=str(Sum1)
    e=str(Sum2)
    for c in range(len(Listread)):
            path1 = parser.parse_args().path1[0]
            p = Path(path1)
            name=str((os.path.basename(x))[:-4])+'_a65914zc.txt'
            output = p / name
            with output.open('w') as newfile:
                newfile.write(d+':'+e)
