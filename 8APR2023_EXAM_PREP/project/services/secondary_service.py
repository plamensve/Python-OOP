from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        message = f"{self.name} Secondary Service:\n"
        message += f"Robots: {' '.join((r.name for r in self.robots)) if self.robots else 'none'}"
        return message
