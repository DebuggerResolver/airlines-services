from pydantic import BaseModel
from enum import Enum ,auto
from uuid import uuid4 ,UUID,Field

class TransactionType(Enum):
    PAYMENT=auto()
    CANCELLATION=auto()
    REFUND=auto()

class Transactions(BaseModel):
    user_id:UUID=Field(description='user_id')
    flight_id:UUID=Field(description='Flight id of the flight where user onboaded it ')
    source:str=Field(description='Pickup point for user')
    destination:str=Field(description='Dropping point for user')
    charges:float=Field(description='Fare charges')
    transaction_type:TransactionType=Field(description='Type of transactions ')
    