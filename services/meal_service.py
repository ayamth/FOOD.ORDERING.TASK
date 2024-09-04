from utilities.base_service import BaseService
from models.meal import Meal

class MealService(BaseService):
    def list_all(self):
        return self.data

    def add(self, meal):
        if isinstance(meal, Meal):
            self.data.append(meal.to_dict()) #save as dictionary
        else:
            raise ValueError("invalid meal object. must be an instance of meal")
        

    def remove(self, meal_id):
        self.data= [meal for meal in self.data if meal['id']!=meal_id]

    def update(self, meal_id, updated_info):
        meal_found = False
    
        for meal in self.data:
            if meal['id'] == meal_id:
                meal.update(updated_info)
                meal_found = True
                break
        
        if not meal_found:
            raise ValueError('Meal with given ID not found')
