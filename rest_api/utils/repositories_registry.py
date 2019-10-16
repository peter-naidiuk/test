

class RepositoryRegistry:

    def __init__(self, repositories):
        for repository in repositories:
            setattr(self, repository.__name__, repository)
