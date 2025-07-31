def check_valid_passwords(password_list):
    valid_passwords= []
    for password in password_list:
        if len(password) < 6 or len(password) > 12:
            continue
        has_lower=False
        has_upper=False
        has_digit=False
        has_special=False
        has_space=False
        for ch in password:
            if ch.islower():
                has_lower=True
            elif ch.isupper():
                has_upper=True
            elif ch.isdigit():
                has_digit=True
            elif ch in "$#@":
                has_special=True
            elif ch == " ":
                has_space=True
        if has_lower and has_upper and has_digit and has_special and not has_space:
            valid_passwords.append(password)
