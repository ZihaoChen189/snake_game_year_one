import argparse
import os
import collections
import re
from pathlib import Path
parser = argparse.ArgumentParser(description='')
parser = argparse.ArgumentParser(description='')
parser.add_argument('way2', metavar='p', type=str, nargs='+')
parser.add_argument('way', metavar='p', type=str, nargs='+')
parser.add_argument('way1', metavar='p', type=str, nargs='+')
args = parser.parse_args()
way = Path(args.way[0])
l = []
for p in way.glob('*'):
    l.append(str(p))
for x in l:
    with open(x,'r') as f:
        input=(''.join(f.read())).strip('\n')
    first = input.split()
    num = re.sub(r'[0-9]+','',input)
    second = num.split()
    chr = "[-/:;()$&@“.,?!’[\\]{}#%^*+=_\|~<>€£¥•\\''\n]"
    pun = re.sub(chr,'',input)
    address = ((re.sub(r'[0-9]+','',pun)).lower()).split()
    a=re.sub(r'[0-9]+','',pun).split()
    l = []
    for i in range(len(address)):
        while address[i] != a[i]:
            l.append(address[i])
            i+=1
    sum1=0
    sum4=0
    sum2=0
    sum3=0
    for oo in range(len(input)):
        if input[oo].isspace():
            sum2+=1
        elif input[oo].isdigit():
            sum4+=1
        elif input[oo].isalpha():
            sum1+=1
        else:
            sum3+=1
    def tokens(address):
        return re.findall('[a-z]+', address.lower())
    way2 = parser.parse_args().way2[0]
    p2 = Path(way2)
    with open(p2, 'r') as f:
        WORDS = tokens(f.read())
    WORD_COUNTS = collections.Counter(WORDS)
    def known(words):
        return {w for w in words if w in WORD_COUNTS}
    def edits0(word):
        return {word}
    def edits1(word):
        letter = 'abcdefghijklmnopqrstuvwxyz'
        def splits(word):
            return [(word[:i], word[i:]) for i in range(len(word) + 1)]
        double = splits(word)
        off = [a + b[1:] for (a, b) in double if b]
        push = [a + b[1] + b[0] + b[2:] for (a, b) in double if len(b) > 1]
        over = [a + c + b[1:] for (a, b) in double for c in letter if b]
        add = [a + c + b for (a, b) in double for c in letter]
        return set(off + push + over + add)
    def edits2(word):
        return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
    def correct(word):
        xycad = (known(edits0(word)) or
                      known(edits1(word)) or
                      known(edits2(word)) or
                      [word])
        return max(xycad, key=WORD_COUNTS.get)
    def correct_match(match):
        word = match.group()
        def case_of(address):
            return (str.upper if address.isupper() else
                    str.lower if address.islower() else
                    str.title if address.istitle() else
                    str)
        return case_of(word)(correct(word.lower()))
    def correct_address_generic(address):
        return re.sub('[a-zA-Z]+', correct_match, address)
    original_word_list = address
    llist = []
    for original_word in original_word_list:
        correct_word = llist.append(correct_address_generic(original_word))
    try1 =[]
    for try4 in range(len(llist)):
        if llist[try4] != address[try4]:
            try1.append(llist[try4])
    way1 = parser.parse_args().way1[0]
    p = Path(way1)
    name=str((os.path.basename(x))[:-4])+'_a65914zc.txt'
    newfile = p / name
    with newfile.open('w') as output:
        output.write('Formatting ###################\n')
        output.write('Number of upper case removed:'+str(len(l)))
        output.write('\nNumber of punctuation removed:'+str(sum3))
        output.write('\nNumber of numbers removed:'+str(sum4))
        output.write('\nSpellchecking ###################')
        output.write('\nNumber of words:'+str(len(address)))
        output.write('\nNumber of correct words:'+str(len(address)-len(try1)))
        output.write('\nNumber of incorrect words:'+str(len(try1)))
