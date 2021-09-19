# Nama  : Aria Pratama Effendi
# NIM   : 2041720112
# Kelas : TI-2F
import numpy as np
from numpy.lib.shape_base import row_stack
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# variabel input production
x_production = np.arange(0, 10000, 1) 

production_low = fuzz.trimf(x_production, [2000 , 2000, 6000])
production_middle = fuzz.trimf(x_production, [2000 , 6000, 10000])
production_high = fuzz.trimf(x_production, [6000, 10000, 10000])

# input production score nya
production_score = 5.5

# production degree
production_low_degree = fuzz.interp_membership(x_production, production_low, production_score)
production_middle_degree = fuzz.interp_membership(x_production, production_middle, production_score)
production_high_degree = fuzz.interp_membership(x_production, production_high, production_score)

# melakukan visusalisasi
fig_scale_x = 2.0
fig_scale_y = 1.5
fig = plt.figure(figsize=(6.4 * fig_scale_x, 4.8 * fig_scale_y))
row = 2
col = 3

plt.subplot(row, col, 1)
plt.title("Production")
plt.plot(x_production, production_low, label="low", marker=".")
plt.plot(x_production, production_middle, label="middle", marker=".")
plt.plot(x_production, production_high, label="high", marker=".")
plt.legend(loc="upper left")

#mencari nilai aktivasi
low_degree = production_low_degree
middle_degree = production_middle_degree
high_degree = production_high_degree

#mencari rata-rata
w1 = low_degree
w2 = middle_degree
w3 = high_degree

z1 = 5.0 + 0.2 * production_score
z2 = 5.0 + 0.5 * production_score
z3 = 5 + 1.0 * production_score
z = (w1 * z1 + w2 * z2 + w3 * z3) / (w1 + w2 + w3)
print(z)