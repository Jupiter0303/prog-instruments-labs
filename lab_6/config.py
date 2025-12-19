import json


try:
    with open("settings.json", 'r') as js:
        config = json.load(js)
except FileNotFoundError:
    with open("lab_6/settings.json", 'r') as js:
        config = json.load(js)

INITIAL_FILE = "lab_6/" + config["initial_file"]
ENCRYPTED_FILE = "lab_6/" + config["encrypted_file"]
DECRYPTED_FILE = "lab_6/" + config["decrypted_file"]
SYMMETRIC_KEY = "lab_6/" + config["symmetric_key"]
PUBLIC_PEM = "lab_6/" + config["public_key"]
PRIVATE_PEM = "lab_6/" + config["secret_key"]