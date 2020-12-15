import cv2
from numpy import *
import pytesseract
import csv
import pandas as pd

pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img= cv2.imread("Screenshot.png")
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
a=pytesseract.image_to_string(img)

with open ("t.txt","w") as f:
    f.write(a)

dic = {}
l=[]
with open ("t.txt","r") as f:
    m = f.readlines()
    for i in m:
        l.append(i)


def cut(x):
    list1=[]
    for i in t1:
        if i == '':
            index = t1.index('')
            list1.append(index)
            del t1[0:index + 1]

    asd= max(list1)
    return asd



t= list(map(lambda x:x.strip(),l))
t1=t.copy()
c=cut(t1)


def get(z):
    if len(t)>0:
        n = []
        for i in t:
            n.append(i)


            if i == '' :
                break

        index = t.index('')
        del t [0:index+1]

        global c
        if len(n)==c+1:
            return n

        else:
            for i in t:
                n.append(i)

                if i == '':
                    break

            if len(n)<c+1:
                ll=(c+1)-len(n)
                for i in range (0,ll):
                    n.append(0)
            elif len(n)>c+1:
                length = len(n)

                del n [(c+1):length+1]
                return n

            else:
                return

            return n
    else:
        return


l1=get(t)
l2=get(t)
l3=get(t)
l4=get(t)
l5=get(t)
l6=get(t)
l7=get(t)
l8=get(t)

dic['col1']=l1
dic['col2']=l2
dic['col3']=l3
dic['col4']=l4
dic['col5']=l5
dic['col6']=l6
dic['col7']=l7
dic['col8']=l8


df=pd.DataFrame(dic)
df.dropna(how="all",axis=1,inplace=True)
print(df)
df.to_csv('csv.csv',index=False)









