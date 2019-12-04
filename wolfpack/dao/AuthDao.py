from wolfpack.dao import UserDao
from wolfpack.Enum import SessionStorageEnum


def isAuthenticated(request):
    return request.session[str(SessionStorageEnum.U_ID)] is not None


# request is the request variable from View
def login(request, email, password, role):
    user = UserDao.getUserByEmailAndPassword(email, password, role)
    if user is None:
        return False
    else:
        request.session['user'] = user
        request.session[str(SessionStorageEnum.U_ID)] = user.id
        request.session[str(SessionStorageEnum.U_ROLE)] = user.role
        return True
