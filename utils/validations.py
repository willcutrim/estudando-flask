
class UserValidation:
    def validate_email(self, email):
        return "@" not in email

    def email_duplicate(self, email, db):
        return any(user.email == email for user in db)