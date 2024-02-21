from .manageK2appFunctio import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def managek2App_api(request):
        if request.method == 'POST':
            if request.data:
                data = request.data
                if 'operation' in data:
                    operation = data['operation']    
                    if operation == 'getPrimarySecondaryFunctions':
                        if 'state' in data and 'district' in data:
                            state = data['state']
                            district = data['district']

                            response = getPrimarySecondaryFunctions_fn(state, district)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})

        # ----------------------------------------------------------------------------------------------------------
                    elif operation == 'getFieldNameInLocalLanguage':
                        if ('language' in data and
                            'k2Type' in data):            
                            language = data['language'] 
                            k2Type = data['k2Type']         
                            response = getLanguages_fn(language,k2Type)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------
                    elif operation == 'getk2support':
                        if 'state' in data and 'district' in data:
                            state = data['state']
                            district = data['district']

                            response = getk2support_fn(state, district)
                            return JsonResponse(response,safe =False)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})

                    
        # -----------------------------------------------------------------------------------------

                    elif operation == 'getStateDistrictList':
                        response = getStateDistrictList_fn()
                        return JsonResponse(response)

        # ----------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------- 
                    elif operation == 'getVillageList':
                        if 'state' in data and 'district' in data:
                            state = data['state']
                            district = data['district']
                            response = getVillageList_fn(state, district)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({"message": "Missing parameters"})
        # ----------------------------------------------------------------------------------
                    elif operation == 'getTertiaryFourthFunctions':
                        if 'priSecId' in data:
                            priSecId = data['priSecId']

                            response = getTertiaryFourthFunctions_fn(priSecId)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})

                    else:
                        return JsonResponse({'message': 'Invalid operation'})
                else:
                    return JsonResponse({'message': 'Missing operation'})
            else:
                    return JsonResponse({'result': 'failure','message': 'Missing request'})
        return JsonResponse({'Message: Success'})
    # -------------------------------------------------------------------------------------------

 