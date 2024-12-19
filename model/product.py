import uuid

class Product:
    def __init__(self,name, label_description, category, raw_material_list, manufacturing_date, expiration_date, quantity):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__label_description = label_description
        self.__category = category
        self.__raw_material_list = raw_material_list
        self.__manufacturing_date = manufacturing_date
        self.__expiration_date = expiration_date
        self.__quantity = quantity

    @property
    def id(self): 
        return str(self.__id)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def label_description(self):
        return self.__label_description

    @label_description.setter
    def label_description(self, value):
        self.__label_description = value
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        self.__category = value
    
    @property
    def raw_material_list(self):
        return self.__raw_material_list
    
    @raw_material_list.setter
    def raw_material_list(self, value):
        self.__raw_material_list = value
    
    @property
    def manufacturing_date(self):
        return self.__manufacturing_date
    
    @manufacturing_date.setter
    def manufacturing_date(self, value):
        self.__manufacturing_date = value

    @property
    def expiration_date(self):
        return self.__expiration_date
    
    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    


