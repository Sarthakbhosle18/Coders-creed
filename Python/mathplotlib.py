import matplotlib.pyplot as plt

x = [10,20,30,40,50]
y = [50,20,10,30,40]

plt.plot(x,y,'o-r',ms=12,mec='r',mfc='w')
plt.grid()
plt.xlabel("Days")
plt.ylabel("calories")

plt.show()

# plt.pie(x,labels=['day1','day2','day3','day4','day5'])
# plt.bar(x,y)
plt.scatter(x=x,y=y)
plt.show()