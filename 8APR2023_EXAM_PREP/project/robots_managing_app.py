from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = next(filter(lambda r: r.name == robot_name, self.robots))
        current_service = next(filter(lambda s: s.name == service_name, self.services))
        if current_robot.__class__.__name__ == 'MaleRobot' and current_service.__class__.__name__ == 'SecondaryService' or \
                current_robot.__class__.__name__ == 'FemaleRobot' and current_service.__class__.__name__ == 'MainService':
            return "Unsuitable service."
        self.robots.remove(current_robot)

        if current_service.capacity == 0:
            raise Exception("Not enough capacity for this robot!")

        current_service.robots.append(current_robot)
        current_service.capacity -= 1
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = next(filter(lambda s: s.name == service_name, self.services))
        try:
            current_robot = next(filter(lambda r: r.name == robot_name, current_service.robots))
            current_service.robots.remove(current_robot)
            self.robots.append(current_robot)
            return f"Successfully removed {robot_name} from {service_name}."
        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        current_service = next(filter(lambda s: s.name == service_name, self.services))
        counter = 0
        for r in current_service.robots:
            r.eating()
            counter += 1

        return f"Robots fed: {counter}."

    def service_price(self, service_name: str):
        current_service = next(filter(lambda s: s.name == service_name, self.services))
        total_price = 0
        for r in current_service.robots:
            total_price += r.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for s in self.services:
            result.append(s.details())
        return '\n'.join(result)
