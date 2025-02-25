from mongoengine import Document, StringField, IntField
from pydantic import BaseModel

class AVCountersTable(Document):
    project= StringField(required =True)
    member = StringField(required =True)
    loveus = StringField(required =True)
    happyClient = StringField(required =True)
    

class AVCountersModel(BaseModel):
    project :str
    member :str
    loveus :str
    happyClient :str