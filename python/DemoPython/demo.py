print ("Nhap USD: ")

usd = int(input())
vnd = usd * 24515

#rint("vnd = "+ str(vnd))
a=str(usd) + " USD = " + str(vnd) + " VND"
#print (str(usd) + " USD = " + str(vnd) + " VND")
#b= a[0:7] + a[-4:-1]
#c= str(a) + ' ' + str(b)


c = len(str(vnd))
#print(a)
#print(c)
if (c==5):
    d = str(vnd)[0:2] + '.' + str(vnd)[2:5]
    print( str(usd) + " USD = " + str(d) + " VND")
elif (c==6):
    d = str(vnd)[0:3] + '.' + str(vnd)[3:6]
    print( str(usd) + " USD = " + str(d) + " VND")
elif (c==7):
    d = str(vnd)[0:1] + '.' + str(vnd)[1:4] + '.' + str(vnd)[4:8] 
    print( str(usd) + " USD = " + str(d) + " VND")
elif (c==8):
    d = str(vnd)[0:2] + '.' + str(vnd)[2:5] + '.' + str(vnd)[5:8] 
    print( str(usd) + " USD = " + str(d) + " VND")
elif (c==9):
    d = str(vnd)[0:3] + '.' + str(vnd)[3:6] + '.' + str(vnd)[6:9] 
    print(d)
elif (c==10):
    d = str(vnd)[0:1] + '.' + str(vnd)[1:4] + '.' + str(vnd)[4:7] + '.' + str(vnd)[7:10]
    print( str(usd) + " USD = " + str(d) + " VND")
else:
    print( str(usd) + " USD" "  exceeding calculation!" )