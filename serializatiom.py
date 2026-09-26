from pydantic import BaseModel

# pydantic object models can be exported in 2 formats.

# 1.) python dictionary
# 2.) JSON

# pydantic give us control what we need to export eg: include, exclude, unset

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str
    # gender : str = 'Male' # for unset
    age : int
    address : Address

address_dict = {'city' : 'gurugram', 'state' : 'haryana', 'pin' : '110010'}

address1 = Address(**address_dict)

patient_dict = {'name' : 'joker', 'gender' : 'Male', 'age' : 28, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  
# This will convert existing pydantic object model into python dictionary

temp = patient1.model_dump(include=['name','gender']) 

temp = patient1.model_dump(exclude=['name','gender']) 

temp = patient1.model_dump(exclude={'address':['state']}) 

# temp = patient1.model_dump(exclude_unset=True) 
# gender will not shown if not mentioned  

print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()  
print(temp1)



























