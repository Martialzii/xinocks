import hashlib

def generate_martialzii_key(device_id):
    # Your Secret Master Salt - DO NOT SHARE
    master_salt = "MARTIALZII_LEGACY_2026_VIPER" 
    
    # Create the Encrypted Signature
    raw_string = f"{device_id}{master_salt}"
    license_key = hashlib.sha256(raw_string.encode()).hexdigest()[:16].upper()
    
    print(f"\n--- MARTIALZII KEYGEN ACTIVE ---")
    print(f"DEVICE ID: {device_id}")
    print(f"ENCRYPTED KEY: {license_key}")
    print(f"--------------------------------\n")

# Usage
uid = input("Enter Customer Device ID: ")
generate_martialzii_key(uid)