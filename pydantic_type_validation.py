from pydantic import BaseModel
from typing import List, Dict, Optional

# Type validation using pydantic

class Patient(BaseModel):           #pydantic model class

    name : str
    age : int
    weight : float
    marrital_status : bool = False
    allergies : Optional[List[str]] = None              #list will only check if the values in patient_info has a list but List[] will also check if the data is of string type inside a list.

    contact_details : Dict[str,str]     # Same for Dict[]/dict[]



def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)
    

    print('data inserted')


def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)

    print('data updated')

patient_info = {'name': 'shubham', 'age' : 28, 'weight' : 100.8, 'marrital_status' : True, 'allergies' : ['Pollen','Dust'], 'contact_details' : { 'email' : 'abc@gmail.com', 'Mobile_number' : '9999999999' } }          # Dictionary 

patient1 = Patient(**patient_info)  #pydantic object


insert_patient_data(patient1)
#update_patient_data(patient1)




























