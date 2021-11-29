import random

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890qwer"
for i in range(10):
    fh = open(f'./scramble/eng.penitentiarygothicfill.exp{i}.gt.txt', 'w')
    rand = ''.join(random.sample(s, len(s)))
    print(rand)
    fh.write(rand)
    fh.close()

