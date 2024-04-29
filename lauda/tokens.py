from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.crypto import get_random_string

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + get_random_string(length=15)


token = TokenGenerator()
