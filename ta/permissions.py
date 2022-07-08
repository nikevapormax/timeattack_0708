from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException

from rest_framework import status
from user.models import User as UserModel

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)


class IsCandidateUser(BasePermission):
    """
        1. user type이 candidate일 경우에만 지원가능하도록 설정
        2. 로그인하지 않았다면 "서비스를 이용하기 위해 로그인 해주세요." 메세지 반환
        3. candidate가 아니라면 '접근 권한이 없습니다.' 메세지 반환
    """
    
    SAFE_METHODS = ('POST')
    message = '접근 권한이 없습니다.'
    
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and  user.user_type_id == 1 and request.method in self.SAFE_METHODS:   
            return True

        return False