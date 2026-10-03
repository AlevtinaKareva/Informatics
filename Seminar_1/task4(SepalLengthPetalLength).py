import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('../iris_data.csv')
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()                                # превращаем в плоский список из 6 осей: axs[0]..axs[5]
fig.suptitle('Комбинации длин и ширин лепестков и чашелистников (Petal и Sepal)', fontsize=22)

# 1. SepalLength от SepalWidth
ax = axs[0]
ax.set_title('SepalLength от SepalWidth', fontsize=14)
ax.set_xlabel('SepalWidth')
ax.set_ylabel('SepalLength')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalLengthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalLengthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalLengthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')          # точки setosa
ax.scatter(x_vi, y_vi, color='orange', label='virginica')   # точки virginica
ax.scatter(x_ve, y_ve, color='green', label='versicolor')   # точки versicolor
b, a = np.polyfit(x_s, y_s, deg=1)                 # МНК для setosa
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)               # МНК для virginica
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)               # МНК для versicolor
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)                              # легенда
ax.grid(alpha=0.3)

# 2. SepalLength от PetalWidth
ax = axs[1]
ax.set_title('SepalLength от PetalWidth', fontsize=14)
ax.set_xlabel('PetalWidth')
ax.set_ylabel('SepalLength')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalLengthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalLengthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalLengthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')
ax.scatter(x_vi, y_vi, color='orange', label='virginica')
ax.scatter(x_ve, y_ve, color='green', label='versicolor')
b, a = np.polyfit(x_s, y_s, deg=1)
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# 3. SepalLength от PetalLength
ax = axs[2]
ax.set_title('SepalLength от PetalLength', fontsize=14)
ax.set_xlabel('PetalLength')
ax.set_ylabel('SepalLength')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalLengthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalLengthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalLengthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalLengthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalLengthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalLengthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')
ax.scatter(x_vi, y_vi, color='orange', label='virginica')
ax.scatter(x_ve, y_ve, color='green', label='versicolor')
b, a = np.polyfit(x_s, y_s, deg=1)
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# 4. PetalLength от SepalWidth
ax = axs[3]
ax.set_title('PetalLength от SepalWidth', fontsize=14)
ax.set_xlabel('SepalWidth')
ax.set_ylabel('PetalLength')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalLengthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalLengthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalLengthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')
ax.scatter(x_vi, y_vi, color='orange', label='virginica')
ax.scatter(x_ve, y_ve, color='green', label='versicolor')
b, a = np.polyfit(x_s, y_s, deg=1)
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# 5. PetalLength от PetalWidth
ax = axs[4]
ax.set_title('PetalLength от PetalWidth', fontsize=14)
ax.set_xlabel('PetalWidth')
ax.set_ylabel('PetalLength')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalLengthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalLengthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalLengthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')
ax.scatter(x_vi, y_vi, color='orange', label='virginica')
ax.scatter(x_ve, y_ve, color='green', label='versicolor')
b, a = np.polyfit(x_s, y_s, deg=1)
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# 6. PetalWidth от SepalWidth
ax = axs[5]
ax.set_title('PetalWidth от SepalWidth', fontsize=14)
ax.set_xlabel('SepalWidth')
ax.set_ylabel('PetalWidth')
x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'PetalWidthCm'])
x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'PetalWidthCm'])
x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'PetalWidthCm'])
ax.scatter(x_s, y_s, color='blue', label='setosa')
ax.scatter(x_vi, y_vi, color='orange', label='virginica')
ax.scatter(x_ve, y_ve, color='green', label='versicolor')
b, a = np.polyfit(x_s, y_s, deg=1)
ax.plot(x_s, b * x_s + a, color='blue', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_vi, y_vi, deg=1)
ax.plot(x_vi, b * x_vi + a, color='orange', label=f'y={b:.2f}x+{a:.2f}')
b, a = np.polyfit(x_ve, y_ve, deg=1)
ax.plot(x_ve, b * x_ve + a, color='green', label=f'y={b:.2f}x+{a:.2f}')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # выравнивание
plt.show()