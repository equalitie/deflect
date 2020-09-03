from rest_framework.authentication import TokenAuthentication

class TokenAuthenticationChild(TokenAuthentication):
    """
    Extend TokenAuthentication to change property
    """
    keyword = 'Bearer'  # Authorization: Bearer <token>
