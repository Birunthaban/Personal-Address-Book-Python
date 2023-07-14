class Contact:

    def __init__(self, name, phone_number, email_address, address):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__address = address
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name= name
    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,phone_number):
        self.__phone_number= phone_number
    @property
    def email_address(self):
        return self.__email_address
    @email_address.setter
    def email_address(self,email_address):
        self.__email_address= email_address
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,address):
        self.__name= address
