from src.database.config_db import Database
from datetime import datetime
import json
from bson import json_util
from src.models import EquipmentBase

class EquipmentDAO: # DAO - Data Access Object
    def __init__(self):
        self.db = Database(collection='equipment')

    def get_all(self):
        try:
            res = self.db.collection.find({}, {'_id': 0, 'name': 1,'register': 1, 'maintenance': 1, 'c_room': 1, 'c_date': 1} )

            parsed_json = json.loads(json_util.dumps(res))
            return parsed_json
        
        except Exception as e:
            print(f'Houve um erro ao tentar pegar os equipamentos: {e}')
            return None
    
    def create(self, new_equipment: EquipmentBase):
        try:
            result = self.db.collection.insert_one(new_equipment.model_dump())
            
            return result.acknowledged
        except Exception as e:
            print(f'Houve um erro ao tentar pegar os equipamentos: {e}')
            return None

    def read_one(self, register):
        try:
            res = self.db.collection.find_one({'register': register})
            print('one equipment: ', res)

            parsed_json = json.loads(json_util.dumps(res))

            return parsed_json
        except Exception as e:
            return False
        
    def get_equipments_by_current_room(self, current_room):
        try:
            res = self.db.collection.find({'c_room': current_room})

            parsed_json = json.loads(json_util.dumps(res))
            print(f"get equip by c room: {parsed_json}")

            return parsed_json
        except Exception as e:
            return False
        
    def update(self, data_equipment):
        try:
            res = self.db.collection.update_one({'register_': data_equipment.register_}, {'$set':  {'name': data_equipment.name, 'last_maintenance': data_equipment.last_maintenance, 'next_maintenance': data_equipment.next_maintenance}})

            if res.matched_count == 0:
                return False
            else:
                return True
        except Exception as e:
            print(f'Houve um erro ao tentar pegar os equipamentos: {e}')
            return None
        
    def delete(self, register_):
        try:
            res = self.db.collection.delete_one({'register_': register_})

            if res.deleted_count == 0:
                return False
            else:
                return True
        except Exception as e:
            print(f'Houve um erro ao tentar pegar os equipamentos: {e}')
            return None
        
    def get_historic(self):
        try:
            res = self.db.collection.find({}, {'_id': 0, 'name': 1,'register_': 1, 'historic': 1})

            parsed_json = json.loads(json_util.dumps(res))
            
            return parsed_json
        except Exception as e:
            print(f'Houve um erro ao tentar pegar os equipamentos: {e}')
            return None
        
    def update_maintenance(self, data_equipment):
        try:
            res = self.db.collection.update_one({'register_': data_equipment.register_}, {'$set':  {'maintenance': data_equipment.maintenance}})


            if res.matched_count == 0:
                return False
            else:
                return True
        except Exception as e:
            print(f'Houve um erro ao tentar atualizar o manutenção: {e}')
            return None

    def get_current_room_and_date(self, esp_id):
        try:
            res = self.db.collection.find_one({'esp_id': esp_id},  {'_id': 0, 'name': 1, 'register_': 1,  'current_room': 1, 'current_date': 1})
            # print('one equipment: ', res['current_room'])

            return res
        except Exception as e:
            raise e
        
    def update_historic(self, esp_id, room, date):
        try:
            new_data = {
                'room': room,
                'inicial_date': date,
            }
            res = self.db.collection.update_one({'esp_id': esp_id}, {'$push': {'historic': new_data}})
            print('one equipment: ', res)

            return res
        except Exception as e:
            raise e
    
    def update_current_room(self, esp_id, room):
        try:
            date = datetime.now()
            
            res = self.db.collection.update_one({'esp_id': esp_id},{'$set': {'current_room': room, 'current_date': date}})
            print('one equipment type: ', type(res))

            return res
        except Exception as e:
            raise e