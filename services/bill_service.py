from utilities.base_service import BaseService
from models.bill import Bill

class BillService(BaseService):
    def list_all(self):
        return self.data
    def add(self, entity):
        if not isinstance(entity, Bill):
            raise TypeError ('expected an instance of bill')
        bill_data={
            'id': entity.id,
            'user_id': entity.user_id,
            'meal_id': entity.meal_id,
            'total_price': entity.total_price,
            'is_paid': entity.is_paid
        }
        self.data.append(bill_data)

    def remove(self, bill_id):
        self.data = [bill for bill in self.data if bill['id']!=bill_id]

    def update(self, bill_id, updated_info):
        for bill in self.data:
            if bill["id"]==bill_id:
                bill['is_paid']=updated_info.get('is_paid', bill['is_paid'])
                break

        