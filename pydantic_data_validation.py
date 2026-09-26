from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Data validation using pydantic

class Patient(BaseModel):           #pydantic model class

    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples='Shubham', default=None)]                      # Field and annotated both can also use to attach metadata/description
    email: EmailStr
    linkdin_url : AnyUrl                                    #custom_data_type
    age : int = Field(gt=0, lt=120)                         # Field Validation
    weight : Annotated[float, Field(gt=0, strict=True)]                             # Field Validation
    marrital_status : Annotated[bool, Field(default = False, description='Married or not')]
    allergies : Annotated[Optional[List[str]], Field(default=None, max_length = 5)]  # Field Validation

    contact_details : Dict[str,str]   

                                                            

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkdin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)
    

    print('data inserted')


def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.marrital_status)
    print(patient.allergies)
    print(patient.contact_details)

    print('data updated')

patient_info = {'name': 'shubham','email' : 'abc@gmail.com', 'linkdin_url' : 'http://linkdin.com', 'age' : 28, 'weight' : 100.8,  'marrital_status' : True, 'allergies' : ['Pollen','Dust'], 'contact_details' : { 'email' : 'abc@gmail.com', 'Mobile_number' : '9999999999' } }          # Dictionary 

patient1 = Patient(**patient_info)  #pydantic object


insert_patient_data(patient1)
#update_patient_data(patient1)































































