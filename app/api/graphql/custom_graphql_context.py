from app.services.user import UserService


class CustomGraphQLContext:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
