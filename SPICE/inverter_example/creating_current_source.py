import numpy as np
import matplotlib.pyplot as plt


tau_r = 20e-12
tau_f = 200e-12
Q = 250e-15
I0 = Q / (tau_f - tau_r)

t = np.linspace(0, 1e-9, 200)
I = I0*(np.exp(-t/tau_f) - np.exp(-t/tau_r))

# --- Plot ---
plt.plot(t*1e12, I*1e6)
plt.xlabel("Time (ps)")
plt.ylabel("Current (uA)")
plt.title("SET Double Exponential Current")
plt.show()


with open("set_pwl.sp", "w") as f:
    f.write("I_SET 0 OUT pwl (\n")
    for time, current in zip(t, I):
        f.write(f"+ {time*1e9}NS {current}\n")
    f.write(")\n")
