import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [10,14,8,12,6]


plt.plot(x_values, y_values, marker = '*', linestyle = '-', color = 'r', label = 'Data')

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Sample Line Graph')

plt.grid(False)

plt.legend()

plt.show()