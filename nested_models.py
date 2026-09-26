from pydantic import BaseModel

#Nested models -> if we use a model in some other model as a field in pydantic

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city' : 'gurugram', 'state' : 'haryana', 'pin' : '110010'}

address1 = Address(**address_dict)

patient_dict = {'name' : 'joker', 'gender' : 'male', 'age' : 28, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)

print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)

# Better organized data (eg: address)

# Reusability : Use Vitals in multiple models eg: patient, medical record

# Readablity : Easier for developers and API consumers to understand

#validation : Nedted models are validated automatically - no extra work needed
