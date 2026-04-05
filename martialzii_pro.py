import hashlib
import matplotlib.pyplot as plt
import pandas as pd
import sys

# 1. THE SECURITY LOCK
def check_license(input_key, device_id):
    master_salt = "MARTIALZII_LEGACY_2026_VIPER"
    expected = hashlib.sha256(f"{device_id}{master_salt}".encode()).hexdigest()[:16].upper()
    return input_key.upper() == expected

print("--- MARTIALZII ENTERPRISE: SERIES C SECURE BOOT ---")
dev_id = "YOGA12-TEST" 
user_key = input(f"ENTER LICENSE KEY FOR {dev_id}: ")

if not check_license(user_key, dev_id):
    print("\n❌ ACCESS DENIED: INVALID OR EXPIRED LICENSE.")
    print("PURCHASE AT: https://cyrusphere46.gumroad.com/l/series-c-fraudguard")
    sys.exit()

# 2. THE STORM ENGINE UNLOCK
print("\n✅ KEY VERIFIED. INITIALIZING STORM ANALYTICS...")

data = {'Time': ['10:00', '11:00', '12:00', '13:00', '14:00'], 'Blocked_Attempts': [5, 12, 8, 25, 3]}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6), facecolor='#0a0a0a')
ax = plt.axes(); ax.set_facecolor('#0a0a0a')
plt.plot(df['Time'], df['Blocked_Attempts'], color='#39FF14', marker='o', linewidth=2)
plt.title('MARTIALZII STORM: ACTIVE PROTECTION', color='white', fontsize=14)
plt.xlabel('Timeline', color='#39FF14'); plt.ylabel('Blocked Events', color='#39FF14')
plt.grid(color='#333333', linestyle='--')
plt.show()