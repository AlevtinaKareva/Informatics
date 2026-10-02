import numpy as np
import matplotlib.pyplot as plt
N_steps = 1000 # шагов
n_particles = 1000 # частиц
np.random.seed(42)  #42 - просто рандомное число для начала генерации случайных чисел
steps = np.random.choice([-1, 1], size=N_steps)
x_single = np.cumsum(steps)  # координата на каждом шаге
all_steps = np.random.choice([-1, 1], size=(n_particles, N_steps))
all_trajectories = np.cumsum(all_steps, axis=1)
final_positions = all_trajectories[:, -1]  # положение каждой частицы после N шагов
rms_vs_n = np.sqrt(np.mean(all_trajectories**2, axis=0)) # среднеквадратичное отклонение по всем частицам

fig, axs = plt.subplots(3, 1, figsize=(8, 10))
# График 1: траектория одной частицы
axs[0].plot(range(1, N_steps+1), x_single, linewidth=1.2)
axs[0].axhline(0, color='black', linewidth=0.8)
axs[0].set_title('Траектория одной частицы: x(N)')
axs[0].set_xlabel('N')
axs[0].set_ylabel('x')
axs[0].grid(True, alpha=0.3)

# График 2: гистограмма финальных положений 1000 частиц
axs[1].hist(final_positions, bins=30, edgecolor='black', alpha=0.7)
axs[1].set_title(f'Гистограмма положений после {N_steps} шагов (1000 частиц)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Число частиц')
axs[1].grid(True, alpha=0.3)

# График 3: среднеквадратичное отклонение и корень из числа испытаний
n_vals = np.arange(1, N_steps+1)
axs[2].plot(n_vals, rms_vs_n, label='Среднеквадратичное отклонение', linewidth=1.5)
axs[2].plot(n_vals, np.sqrt(n_vals), '--', color='red', label=r'Теория: $\sqrt{N}$', linewidth=1.5)
axs[2].set_title('Зависимость среднеквадратичного отклонения от N')
axs[2].set_xlabel('N')
axs[2].set_ylabel(r'$\sqrt{\langle x^2 \rangle}$')
axs[2].legend()
axs[2].grid(True, alpha=0.3)

plt.tight_layout() #выравнивание
plt.show()
