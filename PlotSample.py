import matplotlib.pyplot as plt
import csv
x = []
y = []
with open('C:\\Users\\elkxsnk\\PycharmProjects\\FirstEricsson\\Plot.csv') as csvfile:
    for i in csvfile:
        i = i.split(',')
        x.append(int(i[0]))
        y.append(int(i[1]))

print(x)
print(y)

plt.plot(x,y,label='Loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph, check it out')
plt.legend()
plt.show()