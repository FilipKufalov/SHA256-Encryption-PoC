import hashlib

def verify_password(password, sha256password):
    return password == sha256password

def access_granted():
    print("Access granted")

def access_denied():
    print("Access denied")

def login(user, password):
    print("User Plain:", user)
    print("Pass Plain:", password)

    user_hash = hashlib.sha256(user.encode()).hexdigest()
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    print("====================")
    print("User SHA256:", user_hash)
    print("Pass SHA256:", password_hash)
    print("====================")

    combined_hash = user_hash + password_hash

    print("Combined User + Pass:", combined_hash)
    print("====================")

    combined_hash = hashlib.sha256(combined_hash.encode()).hexdigest()
    print("Combined User + Pass with SHA256:", combined_hash)

    if verify_password(combined_hash, "e94f95ff511796edc15233f3ab236498ff7fe6989c7b8c60ca7faa5ad76c46ac"):
        access_granted()
    else:
        access_denied()

if __name__ == "__main__":
    vrata = "vrata1"  # -> SHA256 : 142ebf787c3bf4a7d4cb9e887d75264804ad70c661b952033b11bcc200283867
    passw = "test2"    # -> SHA256 : 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752

    login(vrata, passw)