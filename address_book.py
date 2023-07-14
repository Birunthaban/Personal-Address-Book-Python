from contact import Contact
class Address_Book :
    def __init__(self)-> None:
        self.__contact_list=[]
    def add_contact(self,name,phone_number,email_address,address)-> None :
        temp =Contact (name,phone_number,email_address,address)
        self.__contact_list.append(temp)
        print("contact added ....")
    def remove_contact(self,email_address):
        for contact in self.__contact_list:
            if contact.email_address ==email_address :
                self.__contact_list.remove(contact)
            else :
                print("Contact Not Found")


    def display_contact(self,search_list):
        for contact in search_list :
            print("Contact Name :" + contact.name)
            print("Contact Phone Number :" + contact.phone_number)
            print("Contact Email Address :" + contact.email_address)
            print("Contact Address :" + contact.address)
 
   
    def search_contact(self,name):
        search_list =[]
        for contact in self.__contact_list:
        
            if contact.name.find(name)!=-1:
                
                search_list.append(contact)
        self.display_contact(search_list)
    def display_all(self):
        self.display_contact(self.__contact_list)
 