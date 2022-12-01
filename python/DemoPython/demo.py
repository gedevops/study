print ("Nhap USD: ")

usd = int(input())
vnd = usd * 24515

#rint("vnd = "+ str(vnd))
a=str(usd) + " USD = " + str(vnd) + " VND"
#print (str(usd) + " USD = " + str(vnd) + " VND")
#b= a[0:7] + a[-4:-1]
#c= str(a) + ' ' + str(b)
c = len(str(vnd))
print(a)
print(c)
if (c==5):
    d = str(vnd)[0:2] + '.' + str(vnd)[2:5]
    print(d)
elif (c==6):
    d = str(vnd)[0:2] + '.' + str(vnd)[2:5]
    print(d)
elif (c==7):
    d = str(vnd)[0:2] + '.' + str(vnd)[2:5] 
    print(d)