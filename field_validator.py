from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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


    @field_validator('email')
    @classmethod                                            # always remember field validator is a class method
    def email_validator(cls, value):

        valid_domain = ['hdfc.com','icici.com']

            #abc@gmail.com

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')

        return value

    #field validator only works on single field validation

                                                            # field validator operates in 2 modes. 1.) Before mode 2.) After mode(default)

    @field_validator('name')                  # when mode is after -> value will come after type coercion but if mode is before value will come before coercion 
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')    # by default mode is after
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should be between 0-100')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)

    print('data updated')

patient_info = {'name': 'shubham','email' : 'abc@hdfc.com', 'age' : '28', 'weight' : 100.8,  'marrital_status' : True, 'allergies' : ['Pollen','Dust'], 'contact_details' : { 'email' : 'abc@gmail.com', 'Mobile_number' : '9999999999' } }          # Dictionary 

patient1 = Patient(**patient_info)                              # validation -> Type coercion


#insert_patient_data(patient1)
update_patient_data(patient1)































































