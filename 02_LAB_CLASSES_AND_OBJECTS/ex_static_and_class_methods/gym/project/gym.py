from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        try:
            customer = next(filter(lambda c: c.name == customer.name, self.customers))
        except StopIteration:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        try:
            trainer = next(filter(lambda t: t.name == trainer.name, self.trainers))
        except StopIteration:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        try:
            equipment = next(filter(lambda e: e.name == equipment.name, self.equipment))
        except StopIteration:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        try:
            plan = next(filter(lambda p: p.trainer_id == plan.trainer_id, self.plans))
        except StopIteration:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        try:
            subscription = next(filter(lambda s: s.date == subscription.date, self.subscriptions))
        except StopIteration:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription.customer_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription.trainer_id, self.trainers))
        plan = next(filter(lambda p: p.id == subscription.exercise_id, self.plans))
        equipment = next(filter(lambda e: e.id == plan.equipment_id, self.equipment))

        return f"Subscription <{subscription.id}> on {subscription.date}\n" \
               f"Customer <{customer.id}> {customer.name}; Address: {customer.address}; Email: {customer.email}\n" \
               f"Trainer <{trainer.id}> {trainer.name}\n" \
               f"Equipment <{equipment.id}> {equipment.name}\n" \
               f"Plan <{plan.id}> with duration {plan.duration} minutes"


