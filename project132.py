import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("pro_final.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
dist = df["Distance"].tolist()
gravity = df["Gravity"].tolist()


mass.sort()
radius.sort()
dist.sort()
gravity.sort()



plt.plot(radius , mass)
plt.title("Radius VS Mass")
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()

plt.plot(mass , gravity)
plt.title("Mass VS Gravity")
plt.ylabel("gravity")
plt.xlabel("mass")
plt.show()









