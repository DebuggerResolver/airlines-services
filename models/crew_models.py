from pydantic import BaseModel,Field
from uuid import UUID

class Crew(BaseModel):
    first_name:str=Field(description='First Name of the employee', min_length=3,max_length=10)
    last_name:str=Field(description='Last Name of the employee',min_length=5,max_length=10)
    flight_id_associated:Optional[UUID]=Field(description='Flight id of the flight for which crew member is a part of',default=None)

    