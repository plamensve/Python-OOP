from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        message = f"{self.name} Main Service:\n"
        message += f"Robots: {' '.join((r.name for r in self.robots)) if self.robots else 'none'}"
        return message
