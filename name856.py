import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

