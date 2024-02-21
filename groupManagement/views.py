from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .groupManagementFunction import *
@api_view(['POST'])
def managegroup_api(request):
        if request.method == 'POST':
            if request.data:
                data = request.data

                if 'operation' in data:
                    operation = data['operation']

                    if operation == 'getUserGroups':
                        if ('groupId' in data):
    
                            groupId = data['groupId']
                            response = getUserGroups_fn(groupId)
                            
                            return JsonResponse(response)
                        else:
                            return ("Wrong JSON data")
#----------------------------------------------------------------------------------
                       