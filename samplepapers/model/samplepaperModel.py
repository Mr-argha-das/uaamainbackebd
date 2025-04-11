from mongoengine import Document, StringField, ListField, IntField
from pydantic import BaseModel

class SamplePaperTable(Document):
    seo_title = StringField(required=True)
    seo_description = StringField(required=True)
    fileimages = ListField(StringField())
    pageCount = IntField(required=True)
    moduleName = StringField(required=True)
    moduleCode = StringField(required=True)
    wordcount = IntField(required=True)
    price = IntField(required=True)
    description = StringField(required=True)
    sample_file = StringField(required=True)
    sample_category = StringField(required=True)
    file = StringField(required=True)

class  SamplePaperModel(BaseModel):
    seo_title:str
    seo_description : str
    pageCount:int
    moduleName:str
    moduleCode:str
    wordcount:int
    price : int
    sample_file : str
    sample_category : str
    description: str


class SampleBodyModel(BaseModel):
    seo_title : str
    seo_description : str
    fileimages : list[str]
    pageCount : int
    moduleName : str
    moduleCode : str
    wordcount : int
    price : int
    sample_file : str
    sample_category : str
    description : str
    file : str