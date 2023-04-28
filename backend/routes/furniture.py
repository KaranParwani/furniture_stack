from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from schemas.furniture import Furniture
from . import get_db_conn

furniture_router = APIRouter()

@furniture_router.post("/addFurniture")
def create_furniture(furniture: Furniture) -> dict:
    '''Method to create furniture.
       
       :param furniture: Schema for furniture which includes structure in json like id, name, description and price.
       
       :returns: Returns JSON response if the furniture is added successfully or exception response if it fails.
    '''
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO furniture (name, description, price) VALUES (?, ?, ?)",
                    (furniture.name, furniture.description, furniture.price))
        conn.commit()
        conn.close()
        response = {"message": "Successfully created furniture", 
                    "status_code": status.HTTP_200_OK}
        return JSONResponse(response)
    
    except Exception as e:
        response = {"message": e, 
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
        return JSONResponse(response)

@furniture_router.get("/getFurniture")
def get_all_furniture() -> dict:
    '''Method to get all furnitures.
       
       :param None

       :returns: Returns JSON response if the furnitures are fetched or exception response if it fails.
    '''
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description, price, comment FROM furniture")
        furnitures = cursor.fetchall()
        conn.close()
        furniture_items = [{"id": id,
                            "name": name, 
                            "description": description, 
                            "price": price, 
                            "comment": comment} for id, name, description, price, comment in furnitures]
        
        response = {"message": "Successfully Retrieved Furnitures", 
                    "status_code": status.HTTP_200_OK,
                    "data": furniture_items}
        return JSONResponse(response)
    
    except Exception as e:
        response = {"message": e, 
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
        return JSONResponse(response)