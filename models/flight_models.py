from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class Flight(BaseModel):
    name:str=Field(description='Name of flight ', min_length=4,max_length=20)
    number_of_seats:int=Field(description='Number of seats in the flight',geq=10,leq=120)
    scheduled_at:Optional[datetime]=Field(description='Scheduled time',default=None)

