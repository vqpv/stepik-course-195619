def check_password():
    password = yield
    while True:
        result = False
        if (len(password) >= 10) and any(i.isupper() for i in password) and any(i.isdigit() for i in password) and any(i for i in password if i in ["!", "@", "#", "$", "%"]):
            result = True
        password = yield result
