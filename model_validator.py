from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

# Data validation using pydantic

class Patient(BaseModel):           #pydantic model class

    name : str                     
    email: EmailStr                                
    age : int 
    weight : float
    marrital_status : bool
    allergies : List[str]
    contact_details : Dict[str,str]   



    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('patients older than 60 must have emergency contact details')
        return model

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)

    print('data updated')

patient_info = {'name': 'shubham','email' : 'abc@hdfc.com', 'age' : '75', 'weight' : 100.8,  'marrital_status' : True, 'allergies' : ['Pollen','Dust'], 'contact_details' : { 'email' : 'abc@gmail.com', 'Mobile_number' : '9999999999', 'emergency' : '2222222222' } }          # Dictionary 

patient1 = Patient(**patient_info)                              # validation -> Type coercion


#insert_patient_data(patient1)
update_patient_data(patient1)































































































