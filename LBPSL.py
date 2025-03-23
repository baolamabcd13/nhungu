import matplotlib.pyplot as plt

lbpsl = [0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
plant_sl = [0.60, 0.65, 0.70, 0.80, 0.90, 1.00]
wh_sl = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

plt.figure(figsize=(8, 5))
plt.plot(lbpsl, plant_sl, marker='D', color='mediumpurple', label='Plant SL')
plt.plot(lbpsl, wh_sl, marker='s', color='maroon', label='WH SL')

plt.xlabel('LBPSL')
plt.ylabel('Service Level')
plt.title('Service Level at Different LBPSL')

plt.ylim(0.00, 1.20)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()