from fastapi import APIRouter
from src.controllers.FileController import FileController
from src.schemas.file import URL

router = APIRouter(
    prefix="/file",
    tags=['File']
)


@router.get('/')
async def getAmount(url: str = False):
    try:
        fileController = FileController()
        return await fileController.getBillMetadata(url)
    except Exception as e:
        print(e)
        return {"error": "Oops! error"}
