from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from schemas.comment import Comment
from . import get_db_conn

comment_router = APIRouter()

@comment_router.post("/{furniture_id}/addComment")
def create_comment(furniture_id: int, comment: Comment) -> dict:
    '''Method to add comment on furniture.
       
       :param furniture_id: ID of furniture where to add comment.
       :param comment: Comment dictionary which takes comment as input.
    
       :returns: Returns JSON response if the adding is successfully done or exception response if it fails.
    '''
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE furniture SET comment = ? WHERE id = ?;",
                    (comment.comment, furniture_id))
        conn.commit()
        conn.close()
        response = {"message": "Successfully created comment", 
                    "status_code": status.HTTP_200_OK}
        return JSONResponse(response)
    
    except Exception as e:
        response = {"message": e, 
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
        return JSONResponse(response)
    

@comment_router.post("/getCommentFurniture")
def get_commented_furniture(search_input: dict):
    '''Method to get furniture that has pattern.
       
       :param search_input: search input where the comment was find.
    
       :returns: Returns JSON response if the furnitures are fetched is successfully done 
                 or exception response if it fails.
    '''
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM furniture WHERE comment LIKE ?", 
                       ('%' + search_input.get('pattern') + '%',))
        comment_rows = cursor.fetchall()
        conn.close()
        comment_list = [{"id": id,
                        "name": name, 
                        "description": description, 
                        "price": price, 
                        "comment": comment} for id, name, description, price, comment in comment_rows]
        response = {"message": "Successfully retrived furniture", 
                    "status_code": status.HTTP_200_OK,
                    "data": comment_list}
        return JSONResponse(response)
    
    except Exception as e:
        response = {"message": e, 
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
        return JSONResponse(response)
    
