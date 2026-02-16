import re

def clean_name(name):
    if not isinstance(name, str):
        return ""
    return name.lower().strip()

def clean_email(email):
    if not isinstance(email, str):
        return ""
    return email.lower().strip()

def clean_phone(phone):
    phone = str(phone)
    return re.sub(r'\D', '', phone)

def clean_record(record):
    return {
        "id": record["id"],
        "name": clean_name(record["name"]),
        "email": clean_email(record["email"]),
        "phone": clean_phone(record["phone"]),
        "address": record["address"]
    }
