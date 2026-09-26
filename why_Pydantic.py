
# Function to Receive and Insert patient data into databse

#python has dynamic typing not static

def insert_patient_data(name: str, age:int):

#     print(name)
#     print(age)
#     print('inserted into databse')

    if name == str and age == int:
        if age < 0:
            raise ValueError('age cannot be less than zero')
        else:
            print(name)
            print(age)
            print('data inserted into the database')
    else :
        raise TypeError('incorrect datatype')

insert_patient_data('joker','twenty')
insert_patient_data('shubham','30')

# This makes code lengthy and not acccurated
# That's why pydaantic helps in type validation and data validation
# So that manual code can be avoided







































