from utilities.general_utils import generate_id
class Meal:
    def __init__(self, name, price):
        self.id = generate_id()
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }