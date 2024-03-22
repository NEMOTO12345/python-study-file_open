goods = ["歯ブラシ","豆腐","牛乳","生肉","タオル"]
kind = [1,0,0,0,1]
price = [200,98,218,320,248]

for g,k,p in zip(goods,kind,price):
    if k == 0:
        print(f'{g}:{p*1.1:.0f}円')
    else:
        print(f'{g}:{p*1.08:.0f}円')