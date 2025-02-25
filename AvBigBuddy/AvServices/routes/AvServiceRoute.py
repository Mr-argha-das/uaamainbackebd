import json
from bson import ObjectId
from fastapi import FastAPI ,APIRouter

from AvBigBuddy.AvServices.models.AvServiceModel import AvServiceModel, AvServiceTable



router= APIRouter()
   
@router.post("/api/v1/AvAddService")
async def addService(body : AvServiceModel):
    serviceData = AvServiceTable(**body.dict())
    serviceData.save()
    toJson = serviceData.to_json()
    fromJson = json.loads(toJson)
    return{
        "message" : "data added successfully",
        "status" : True,
        "data" :  fromJson
    }
    
@router.get("/api/v1/AvServiceList")
async def serviceList():
    serviceListData = AvServiceTable.objects.all()
    toJson = serviceListData.to_json()
    fromJson = json.loads(toJson)
    if(serviceListData): 
      return{
        "message" : "Data Fetched Successfully",
        "status" : True,
        "data" : fromJson,
    }
    else:
       return{
          "message" : "Data Not Found",
          "status" : False,
          "data": None
       }
       
@router.delete("/api/v1/AvDeleteAllServices")
async def deleteServices():
   deleteServiceData = AvServiceTable.objects.delete()
   if deleteServiceData == 0:
      return{
         "message" : "data Deleted Successfully",
         "status" : True,
         "data" : None
      }
   
@router.delete("/api/v1/AvDeleteById/{_id}")
async def ServiceDeleteById(_id : str):
    object_id = ObjectId(_id)
    item = AvServiceTable.objects(id=object_id).first()
    item.delete()
    
    return {
        "message": "Data Deleted Successfully",
        "status": True,
    }