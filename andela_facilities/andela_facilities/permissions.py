from rest_framework.permissions import BasePermission


class GroupPermissions(BasePermission):
    """Base permission for groups"""
    def group_member(self, request, group):
        """
        return group name
        """
        return request.user.groups.filter(name=group).exists()


class IsFacilities(GroupPermissions):
    """Permission class for members of facilities"""
    def has_permission(self, request, view):
        """
        Return `True` if user is in facilities.
        """
        return self.group_member(request, 'Facilities')


class IsFellow(GroupPermissions):
    """Permission class for fellows"""
    def has_permission(self, request, view):
        """
        Return `True` if user is a fellow.
        """
        return self.group_member(request, 'Fellows')


class IsFinance(GroupPermissions):
    """Permission class for members of finance team"""
    def has_permission(self, request, view):
        """
        Return `True` if user is in finanace.
        """
        return self.group_member(request, 'Finance')


class IsOccupant(GroupPermissions):
    """Permission class for occupants"""
    def has_permission(self, request, view):
        """
        Return `True` if user is an occupant.
        """
        return self.group_member(request, 'Occupants')


class IsPc(GroupPermissions):
    """Permission class for members of P&C"""
    def has_permission(self, request, view):
        """
        Return `True` if user is in P&C.
        """
        return self.group_member(request, 'P&C')
