import matplotlib.pyplot as plt

warehouses = [3, 4, 5, 6]
plant_inventory = [4250, 3475, 3668, 3475]
wh_inventory = [9778, 10936, 11928, 12698]

plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7, zorder=0)

plt.bar(warehouses, plant_inventory, label='Plant Exp. Inv.', color='mediumpurple', zorder=3)
plt.bar(warehouses, wh_inventory, bottom=plant_inventory, label='WH Exp. Inv.', color='purple', zorder=3)

plt.xlabel('No. of WH\'s')
plt.ylabel('Expected Inventory (Mlbs)')
plt.title('Expected Inventory by No. of Warehouses')

for i in range(len(warehouses)):
    plt.text(warehouses[i], plant_inventory[i] / 2, f'{plant_inventory[i]}', ha='center', color='white', zorder=4)
    plt.text(warehouses[i], plant_inventory[i] + wh_inventory[i] / 2, f'{wh_inventory[i]}', ha='center', color='white', zorder=4)

plt.ylim(0, 18000)
plt.xticks(warehouses)
plt.legend()
plt.tight_layout()

plt.show()