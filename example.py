import requests
#d={'df':12,'fg':22,'hh':98}
#for i in d:
    #l=[1,2,3,4,{1:1,2:2}]
#print(d.df)

#def fun(*p):
   # print(p[3])
#e=[1,2,3,0]
#fun(1,3,5,7,8)
class A:
    def __init__(self,d):
        self.d=d
    def fun(self):
        print(self.d)

d={1:2,3:4}
obj=A(d)
#print(obj.d.get(1))
res = requests.get('https://beautiful-soup-4.readthedocs.io/en/latest/')
print(res.text)