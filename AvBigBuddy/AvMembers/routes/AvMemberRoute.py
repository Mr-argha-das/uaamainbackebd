import json
from bson import ObjectId
from fastapi import FastAPI ,APIRouter

from AvBigBuddy.AvMembers.models.AvMemberModel import AvMembersModel, AvMembersTable




router= APIRouter()
   
@router.post("/api/v1/AvAddMembers")
async def addMembers(body : AvMembersModel):
    MembersData = AvMembersTable(**body.dict())
    MembersData.save()
    toJson = MembersData.to_json()
    fromJson = json.loads(toJson)
    return{
        "message" : "data added successfully",
        "status" : True,
        "data" :  fromJson
    }


@router.get("/api/v1/AvMembersList")
async def MembersList():
    MembersListData = AvMembersTable.objects.all()
    toJson = MembersListData.to_json()
    fromJson = json.loads(toJson)
    if(MembersListData): 
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
       
@router.delete("/api/v1/AvDeleteAllMemberss")
async def deleteMemberss():
   deleteMembersData = AvMembersTable.objects.delete()
   if deleteMembersData == 0:
      return{
         "message" : "data Deleted Successfully",
         "status" : True,
         "data" : None
      }
   
@router.delete("/api/v1/AvDeleteById/{_id}")
async def MembersDeleteById(_id : str):
    object_id = ObjectId(_id)
    item = AvMembersTable.objects(id=object_id).first()
    item.delete()

    return {
        "message": "Data Deleted Successfully",
        "status": True,
    }
