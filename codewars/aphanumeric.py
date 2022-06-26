def alphanumeric(password):
    if password:
        if password.isalnum() and ' ' not in password:
            return True

    return False
