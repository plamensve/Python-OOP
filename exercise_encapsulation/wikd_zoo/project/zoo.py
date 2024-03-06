class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) > self.__animal_capacity or self.__budget < price:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            name = next(filter(lambda n: n.name == worker_name, self.workers))
            self.workers.remove(name)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary
        if sum_of_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_of_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care

        if needed_money < self.__budget:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        info_dict = {}
        for animal in self.animals:
            type_of_animal = animal.__class__.__name__
            data = animal.__repr__()
            if type_of_animal not in info_dict.keys():
                info_dict[type_of_animal] = [data]
            else:
                info_dict[type_of_animal].append(data)
        result += f'----- {len(info_dict["Lion"])} Lions:\n'
        result += '\n'.join(info_dict['Lion'])

        result += '\n' + f'----- {len(info_dict["Tiger"])} Tigers:\n'
        result += '\n'.join(info_dict['Tiger'])

        result += '\n' + f'----- {len(info_dict["Cheetah"])} Cheetahs:\n'
        result += '\n'.join(info_dict['Cheetah'])

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        info_dict = {}
        for worker in self.workers:
            type_of_worker = worker.__class__.__name__
            data = worker.__repr__()
            if type_of_worker not in info_dict.keys():
                info_dict[type_of_worker] = [data]
            else:
                info_dict[type_of_worker].append(data)
        result += f'----- {len(info_dict["Keeper"])} Keepers:\n'
        result += '\n'.join(info_dict['Keeper'])

        result += '\n' + f'----- {len(info_dict["Caretaker"])} Caretakers:\n'
        result += '\n'.join(info_dict['Caretaker'])

        result += '\n' + f'----- {len(info_dict["Vet"])} Vets:\n'
        result += '\n'.join(info_dict['Vet'])

        return result
