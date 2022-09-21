from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import FileResponse
from system.config import db
from api.context import DATADIR
from api.show import show_exception
from api.models import ImmMake, ImmCheck, ImmPdfform, ImmWebform, ImmWord, ImmRun,Word
from api import oauth2
from basemodels.user import User
from api.schemas import EmploymentCertificate,EmploymentCompany

case = db.case

router = APIRouter(
    prefix="/case", tags=["Cases"], responses={404: {"description": "Nof found"}}
)

def remove_items(e:ValidationError,items:list):
    for err in e.errors():
        print(err)
    return e

def permission_check(command: str, user: User):
    user_permissions = user.get("permission")
    if not command in user_permissions and not "all" in user_permissions:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You have no permission for make command.",
        )


@router.post("/make")
async def make(data: ImmMake, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("make", current_user)
    try:
        filename = data.make()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e,data.language)


@router.post("/check")
async def check(data: ImmCheck, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("check", current_user)
    try:
        return data.check()
    except Exception as e:
        show_exception(e,data.language)


@router.post("/word")
async def word(data: ImmWord, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("word", current_user)
    try:
        filename = data.word()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e,data.language)


@router.post("/webform")
async def webform(
    data: ImmWebform, current_user: User = Depends(oauth2.get_current_user)
):
    permission_check("webform", current_user)
    try:
        filename = data.webform()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e,data.language)


@router.post("/pdfform")
async def pdfform(
    data: ImmPdfform, current_user: User = Depends(oauth2.get_current_user)
):
    permission_check("pdfform", current_user)
    try:
        filename = data.pdfform()
        return FileResponse(filename)
    except Exception as e:
        show_exception(e,data.language)


@router.post("/run")
async def run(data: ImmRun, current_user: User = Depends(oauth2.get_current_user)):
    print("run")
    permission_check("run", current_user)
    try:
        return data.run()
    except Exception as e:
        show_exception(e,data.language)


#get_companies and get_certificate are specially for employment certificate generation. It requires interactive dialog to get which company to generate word.
@router.post("/get_companies")
async def get_companies(
    request: EmploymentCompany, current_user: User = Depends(oauth2.get_current_user)
):
    permission_check("run", current_user)
    try:
        companies= request.data.get_companies()
        return companies
    except Exception as e:
        e=remove_items(e,["body","data"])
        show_exception(e,request.language)
        
@router.post("/get_certificate")
async def get_certificate( request: EmploymentCertificate, current_user: User = Depends(oauth2.get_current_user)):
    """Get specific company's employment certificate"""
    permission_check("run", current_user)
    try:
        context=request.data.context(request.company)
        word_temp=DATADIR / "word/employment_certificate.docx"
        word=Word(context=context)
        word_name=word.make(str(word_temp.absolute()))
        return FileResponse(word_name)
    except Exception as e:
        show_exception(e,request.language)
