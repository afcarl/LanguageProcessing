import codecs 

f=codecs.open('train.pos')
j=0
for i in f:
    if i.split():
        j += 1
        l=i.strip().split('	')
        print '\t'.join([str(j), l[0], '_', l[1], '_', '_', '0', 'PLACEHOLDER', '_', '_'])
    else:
        j=0
        print ""
