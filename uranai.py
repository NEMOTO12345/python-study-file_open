import random

uranai = ['大吉','中吉','小吉','凶','大凶','happy']

i = open('uranai.txt','w')
i.write(random.choice(uranai))
i.close()