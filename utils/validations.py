def validate_email(email):
    return "@" not in email

def email_duplicate(email, db):
    return any(user.email == email for user in db)