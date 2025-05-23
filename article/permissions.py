# 这个文件里定义了权限信息
from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 判断查看方法是否在SAFE_METHODS里面（里面默认是GET,HEAD,OPTION等查看类请求方法）
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅管理员可进行其他操作
        return request.user.is_superuser