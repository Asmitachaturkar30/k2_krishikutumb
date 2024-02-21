from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def manageBucket_api(request):
        if request.method == 'POST':
            if request.data:
                data = request.data
                if 'operation' in data:
                    operation = data['operation']    
                    if operation == 'getPrimarySecondaryFunctions':
                        if 'state' in data and 'district' in data:
                            state = data['state']
                            district = data['district']

                            # response = getPrimarySecondaryFunctions_fn(state, district)
                            # return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})
                else:
                    return JsonResponse({'message': 'Missing operation'})
            else:
                    return JsonResponse({'result': 'failure','message': 'Missing request'})
        return JsonResponse({'Message: Success'})
    # -------------------------------------------------------------------------------------------

 