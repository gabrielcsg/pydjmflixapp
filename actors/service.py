from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.__actor_repository = ActorRepository()

    def get_actors(self):
        return self.__actor_repository.get_actors()

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        return self.__actor_repository.create_actor(actor)
