import strawberry


@strawberry.type
class UserType:
    id : int
    uuid : str
    username : str