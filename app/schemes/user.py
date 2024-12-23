import strawberry


@strawberry.type
class User:
    id : int
    uuid : str
    username : str