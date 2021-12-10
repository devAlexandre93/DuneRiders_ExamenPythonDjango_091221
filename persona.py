# Classe du Persona

class Persona:
    def __init__(self, first_name, last_name, address_street = '', address_number = 0, city = '', postcode = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.address_street = address_street
        self.address_number = address_number
        self.city = city
        self.postcode = postcode

    def __str__(self):
        return(f"Hi ! I'm {self.first_name} {self.last_name}.")

    def set_address(self, address_street, address_number, city, postcode):
        self.address_street = address_street
        self.address_number = address_number
        self.city = city
        self.postcode = postcode

    def show_address(self):
        print(f"My full address is : {self.address_number} {self.address_street}, {self.city} ({self.postcode})")

# Liste

my_list = [
    {
        "first_name":"Ilyès",
        "last_name":"Fleury",
        "address_street":"Rue Paul Bert",
        "address_number":73,
        "city":"Dunkerque",
        "postcode":12681
    },
    {
        "first_name":"Lia",
        "last_name":"Dumont",
        "address_street":"Rue Louis-Blanqui",
        "address_number":30,
        "city":"Lille",
        "postcode":63996
    },
    {
        "first_name":"Eléonore",
        "last_name":"Caron",
        "address_street":"Avenue du Château",
        "address_number":87,
        "city":"Rennes",
        "postcode":78482
    },
    {
        "first_name":"Eva",
        "last_name":"Girard",
        "address_street":"Rue du Bon-Pasteur",
        "address_number":9,
        "city":"Rueil-Malmaison",
        "postcode":23879
    }
]

for i in my_list:
    my_persona_from_list = Persona(i['first_name'], i['last_name'])
    print(my_persona_from_list)
    my_persona_from_list.set_address(i['address_street'], i['address_number'], i['city'], i['postcode'])
    my_persona_from_list.show_address()
    print("--")

