def top3(d):
 for key1,value1 in d.items():
    for key2,value2 in d.items():
        if(value1<value2):
            print("value 1 {}".format(value1))
            print("value 2 {}".format(value2))
            t=key1
            t1=value1
            key1=key2
            value1=value2
            key2=t
            value2=t1
            d[key1]=value1
            d[key2]=value2
 print(d)
d={}
d1={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
top3(d1) 