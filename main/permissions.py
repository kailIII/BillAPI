from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

SAFE_METHODS = ['GET', 'HEAD', 'POST']

class IsOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		elif request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
			if request.user.is_superuser:
				return True
			return False
