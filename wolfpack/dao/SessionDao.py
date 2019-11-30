from . import AuthDao
from wolfpack.Enum import UserRoleEnum, SessionStorageEnum

def isScrumMaster(request):
    checkSession(request)
    u_role = int(request.session[SessionStorageEnum.U_ROLE])
    return u_role == UserRoleEnum.SCRUM_MASTER.value

def isDeveloper(request):
    checkSession(request)
    u_role = int(request.session[SessionStorageEnum.U_ROLE])
    return u_role == UserRoleEnum.DEVELOPER.value

def isProductOwner(request):
    checkSession(request)
    u_role = int(request.session[SessionStorageEnum.U_ROLE])
    return u_role == UserRoleEnum.PRODUCT_OWNER.value

def getUId(request):
    checkSession(request)
    return int(request.session[SessionStorageEnum.U_ID])

def getURole(request):
    checkSession(request)
    return int(request.session[SessionStorageEnum.U_ROLE])

def hasSession(request):
    return AuthDao.isAuthenticated(request)

def checkSession(request):
    if hasSession(request) is False:
        raise Exception("user has no active session. Please log in again")
