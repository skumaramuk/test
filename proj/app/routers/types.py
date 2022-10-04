from fastapi import FastAPI, Response, Depends, APIRouter
from .. import schemas, utils

router = APIRouter(
    prefix="/types",
    tags=['Types']
)


@router.get('/')
def get_user(params: schemas.QueryTypes = Depends()):
    params = params.dict()
    return utils.filter_types(**params)