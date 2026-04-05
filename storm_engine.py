import matplotlib.pyplot as plt
import pandas as pd

# Data for the Martialzii STORM Dashboard
data = {
    'Time': ['10:00', '11:00', '12:00', '13:00', '14:00'],
    'Blocked_Attempts': [5, 12, 8, 25, 3]
}
df = pd.DataFrame(data)

# Visual Styling (Viper Green)
plt.figure(figsize=(10, 6), facecolor='#0a0a0a')
ax = plt.axes()
ax.set_facecolor('#0a0a0a')

plt.plot(df['Time'], df['Blocked_Attempts'], color='#39FF14', marker='o', linewidth=2)
plt.fill_between(df['Time'], df['Blocked_Attempts'], color='#39FF14', alpha=0.1)

plt.title('MARTIALZII STORM: REAL-TIME THREAT ANALYTICS', color='white', fontsize=14)
plt.xlabel('Timeline (EAT)', color='#39FF14')
plt.ylabel('Blocked Security Events', color='#39FF14')
plt.xticks(color='white')
plt.yticks(color='white')
plt.grid(color='#333333', linestyle='--')

print('--- MARTIALZII STORM ENGINE ACTIVE ---')
plt.show()