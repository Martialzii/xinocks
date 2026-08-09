import os, subprocess, time, sys, uuid
def get_hwid():
    return str(uuid.getnode())[-6:]
def gatekeeper():
    os.system("cls")
    hwid = get_hwid()
    recovery_file = f"RECOVERY_{hwid}.txt"
    master_recovery = f"MZ-{hwid}-RCV"
    if not os.path.exists(recovery_file):
        with open(recovery_file, "w") as f: f.write(f"OFFICIAL RECOVERY CODE FOR THIS MACHINE: {master_recovery}")
    print("="*50 + "\n MARTIALZII ENTERPRISE - HARDWARE LOCKED ACCESS\n" + "="*50)
    print(f"DEVICE ID: {hwid}")
    user_key = input("Enter License or Recovery Key: ")
    if user_key == master_recovery or (os.path.exists("license.key") and user_key == open("license.key").read().strip()):
        if user_key == master_recovery:
            new_key = input("Recovery Accepted. Set New User Key: ")
            with open("license.key", "w") as f: f.write(new_key)
        print("\n[+] Access Granted."); time.sleep(1); return True
    else:
        print("\n[!] Access Denied. Contact Support with Device ID."); time.sleep(2); sys.exit()
def menu():
    while True:
        os.system("cls")
        print("="*50 + "\n MARTIALZII NEXUS CORE v1.3 - ENTERPRISE\n" + "="*50)
        print("[1] Launch FraudGuard\n[2] Launch RiskGate\n[Q] Exit")
        c = input("\nSelect Module > ").upper()
        if c == "1":
            if os.path.exists("Martialzii_SeriesC_v1.exe"): subprocess.Popen("Martialzii_SeriesC_v1.exe")
            else: print("Error: Series C EXE not found."); time.sleep(2)
        elif c == "Q": break
if __name__ == "__main__":
    if gatekeeper(): menu()
