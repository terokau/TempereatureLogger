import numpy as np
import matplotlib.pyplot as plt

def main():
	print("start of program")
	a = np.array([1,2,3,6,123,51])
	print(a)
	print(a[a<10])
	plot()
	


def plot():
	plt.ion()
	for i in range(50):
		y = np.random.random([10,1])
		plt.plot(y)
		plt.draw()
		plt.pause(0.1)
		plt.clf()

if __name__ == "__main__":
	main()
