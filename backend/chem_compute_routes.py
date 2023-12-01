from fastapi import APIRouter
import logging
import chempy

router = APIRouter()
logging.basicConfig(level=logging.INFO)


@router.get("/")
async def get_routes():
    return {"message": "Hello, routes!"}


@router.post("/")
async def create_route():
    return {"message": "Route created successfully!"}


@router.put("/{route_id}")
async def update_route(route_id: int):
    return {"message": f"Route {route_id} updated successfully!"}


@router.delete("/{route_id}")
async def delete_route(route_id: int):
    return {"message": f"Route {route_id} deleted successfully!"}
