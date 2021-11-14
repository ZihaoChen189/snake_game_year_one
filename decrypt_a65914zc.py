import argparse
import binascii
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
for t in Listread:
    with open(t,'r') as f1:
        content=(''.join(f1.read())).strip('\n')
    Document = content.split()
    if Document[0] == 'Morse':
        dict = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '..--..': '?',
        '-..-.': '/',
        '-.--.-': '()',
        '-....-': '-',
        '.-.-.-': '.',
        '/':' '
        }
        Document.pop(0)
        Document[0] = Document[0][5:]
        File = []
        for s in Document:
            File.append((dict[s]).lower())
        path1 = parser.parse_args().path1[0]
        p = Path(path1)        
        name=str((os.path.basename(t))[:-4])+'_a65914zc.txt'
        newfile = p / name
        with newfile.open('w') as output:
            output.write(''.join(File))
    if Document[0][0:4] == 'Hex:':
        Document[0] = Document[0][4:]
        codelist = []
        ASCIIIcode = []
        for var in Document:
            codelist.append((bin(ord(binascii.unhexlify(var)))).strip('\n'))
            O = str(binascii.unhexlify(var)).strip('b')
            y = O.strip("''")
            ASCIIIcode.append((y).strip('\n'))
        path1 = parser.parse_args().path1[0]
        p = Path(path1)
        name=str((os.path.basename(t))[:-4])+'_a65914zc.txt'
        newfile = p / name
        with newfile.open('w') as output:
            output.write((''.join(ASCIIIcode)).lower())
    if Document[0] == 'Caesar':
        Document.pop(0)
        Document[0] = Document[0][11:]
        address = []
        for a in Document:
            for point in a:
                ASCCODE = ord(point)-3
                if ASCCODE > 96:
                    detail = chr(ASCCODE)
                    address.append(detail)
                elif ASCCODE < 97:
                    ASCCODE1 = 123-(97-ASCCODE)
                    detail = chr(ASCCODE1)
                    address.append(detail)
            address.append(' ')
        path1 = parser.parse_args().path1[0]
        p = Path(path1)
        name=str((os.path.basename(t))[:-4])+'_a65914zc.txt'
        newfile = p / name
        with newfile.open('w') as output:
            output.write(''.join(address))


