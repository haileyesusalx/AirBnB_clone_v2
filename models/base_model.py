import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
        else:
            setattr(self, 'updated_at', datetime.now())
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())

    def __str__(self):
        return "[{}] ({}) {}".format(self.id, type(self).__name__, self.__dict__)

    def save(self):
        setattr(self, 'updated_at', datetime.now())

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict.pop('_sa_instance_state', None)
        return new_dict
