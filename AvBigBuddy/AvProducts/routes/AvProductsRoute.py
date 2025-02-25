import json
from bson import ObjectId
from fastapi import FastAPI ,APIRouter

from AvBigBuddy.AvProducts.models.AvProductsModel import AvProductModel, AvProductTable


router= APIRouter()
   
@router.post("/api/v1/AvAddProduct")
async def addProduct(body : AvProductModel):
    ProductData = AvProductTable(**body.dict())
    ProductData.save()
    toJson = ProductData.to_json()
    fromJson = json.loads(toJson)
    return{
        "message" : "data added successfully",
        "status" : True,
        "data" :  fromJson
    }
    
@router.get("/api/v1/AvProductList")
async def ProductList():
    ProductListData = AvProductTable.objects.all()
    toJson = ProductListData.to_json()
    fromJson = json.loads(toJson)
    if(ProductListData): 
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
       
@router.delete("/api/v1/AvDeleteAllProducts")
async def deleteProducts():
   deleteProductData = AvProductTable.objects.delete()
   if deleteProductData == 0:
      return{
         "message" : "data Deleted Successfully",
         "status" : True,
         "data" : None
      }
   
@router.delete("/api/v1/AvDeleteById/{_id}")
async def productDeleteById(_id : str):
    object_id = ObjectId(_id)
    item = AvProductTable.objects(id=object_id).first()
    item.delete()

    return {
        "message": "Data Deleted Successfully",
        "status": True,
    }