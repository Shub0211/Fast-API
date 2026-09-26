from pydantic_type_validation import BaseModel


# Type validation using pydantic

class Patient(BaseModel):           #pydantic model class

    name : str
    age : int



def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)

    print('data inserted')


def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)

    print('data updated')

patient_info = {'name': 'shubham', 'age' : 28}          # Dictionary 

patient1 = Patient(**patient_info)  #pydantic object


insert_patient_data(patient1)
update_patient_data(patient1)




























