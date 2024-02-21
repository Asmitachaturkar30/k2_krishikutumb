from django.shortcuts import render
from .myIotFunctions import *
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def myIotSystems_api(request):
    if request.method == 'POST':
        if request.data:
            data = request.data

            if 'operation' in data:
                operation = data['operation']

                if operation == 'createIOTDevice':
                    if (
                        'user' in data and 'profileId' in data['user'] and 'deviceRegisteredNumber' in data['user'] and
                        'deviceName' in data['user'] and 'deviceType' in data['user'] and 'deviceVendor' in data['user'] and 'deviceTypeAgriculture' in data['user'] and
                        'deviceStatus' in data['user'] and 'deviceConfig1ParaName' in data['user'] and 'deviceConfig1ParaValue1' in data['user'] and
                        'deviceConfig1ParaValue2' in data['user'] and 'deviceConfig1ParaValue3' in data['user'] and 'deviceConfig2ParaName' in data['user'] and
                        'deviceConfig2ParaValue1' in data['user'] and 'deviceConfig2ParaValue2' in data['user'] and 'deviceConfig2ParaValue3' in data['user'] and
                        'deviceConfig3ParaName' in data['user'] and 'deviceConfig3ParaValue1' in data['user'] and 'deviceConfig3ParaValue2' in data['user'] and
                        'deviceConfig3ParaValue3' in data['user'] and 'deviceConfig4ParaName' in data['user'] and 'deviceConfig4ParaValue1' in data['user'] and
                        'deviceConfig4ParaValue2' in data['user'] and 'deviceConfig4ParaValue3' in data['user'] and 'deviceConfig5ParaName' in data['user'] and
                        'deviceConfig5ParaValue1' in data['user'] and 'deviceConfig5ParaValue2' in data['user'] and 'deviceConfig5ParaValue3' in data['user'] 
                        ):
                        user = data['user']
                        profileId = user['profileId']
                        deviceRegisteredNumber = user['deviceRegisteredNumber']
                        deviceName = user['deviceName']
                        deviceType = user['deviceType']
                        deviceVendor = user['deviceVendor']
                        deviceTypeAgriculture = user['deviceTypeAgriculture']
                        deviceStatus = user['deviceStatus']
                        deviceConfig1ParaName = user['deviceConfig1ParaName']
                        deviceConfig1ParaValue1 = user['deviceConfig1ParaValue1']
                        deviceConfig1ParaValue2 = user['deviceConfig1ParaValue2']
                        deviceConfig1ParaValue3 = user['deviceConfig1ParaValue3']
                        deviceConfig2ParaName = user['deviceConfig2ParaName']
                        deviceConfig2ParaValue1 = user['deviceConfig2ParaValue1']
                        deviceConfig2ParaValue2 = user['deviceConfig2ParaValue2']
                        deviceConfig2ParaValue3 = user['deviceConfig2ParaValue3']
                        deviceConfig3ParaName = user['deviceConfig3ParaName']
                        deviceConfig3ParaValue1 = user['deviceConfig3ParaValue1']
                        deviceConfig3ParaValue2 = user['deviceConfig3ParaValue2']
                        deviceConfig3ParaValue3 = user['deviceConfig3ParaValue3']
                        deviceConfig4ParaName = user['deviceConfig4ParaName']
                        deviceConfig4ParaValue1 = user['deviceConfig4ParaValue1']
                        deviceConfig4ParaValue2 = user['deviceConfig4ParaValue2']
                        deviceConfig4ParaValue3 = user['deviceConfig4ParaValue3']
                        deviceConfig5ParaName = user['deviceConfig5ParaName']
                        deviceConfig5ParaValue1 = user['deviceConfig5ParaValue1']
                        deviceConfig5ParaValue2 = user['deviceConfig5ParaValue2']
                        deviceConfig5ParaValue3 = user['deviceConfig5ParaValue3']

                        response = createIOTdevice_fn(profileId, deviceRegisteredNumber, deviceName, deviceType, deviceVendor,deviceTypeAgriculture, deviceStatus,
                        deviceConfig1ParaName, deviceConfig1ParaValue1,deviceConfig1ParaValue2, deviceConfig1ParaValue3, 
                        deviceConfig2ParaName, deviceConfig2ParaValue1,deviceConfig2ParaValue2, deviceConfig2ParaValue3, 
                        deviceConfig3ParaName, deviceConfig3ParaValue1,deviceConfig3ParaValue2, deviceConfig3ParaValue3,
                        deviceConfig4ParaName, deviceConfig4ParaValue1,deviceConfig4ParaValue2, deviceConfig4ParaValue3, 
                        deviceConfig5ParaName,deviceConfig5ParaValue1,deviceConfig5ParaValue2, deviceConfig5ParaValue3)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# --------------------------------------------------------------------------------
                elif operation == 'getMobileIOTDetails':
                    if 'profileId' in data:
                        profileId = data['profileId']
                        response = getMobileIOTDetails_fn(profileId)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})
#----------------------------------------------------------------------------------- 

                elif operation == 'getMobileIOTWorkingHistory':
                    if ('profileId' in data and
                        'deviceId' in data
                    ):

                        profileId = data['profileId']
                        deviceId = data['deviceId']
                        response = getMobileIOTWorkingHistory_fn(profileId, deviceId)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})
# ------------------------------------------------------------------------------------------------


                elif operation == 'createIOTWorkingData':
                    if (
                            'user' in data and
                            #'id' in data['user'] and
                            'deviceId' in data['user'] and
                            'profileId' in data['user'] and
                            'deviceConfig1ParaName' in data['user'] and
                            'deviceConfig1ParaValue' in data['user'] and
                            'deviceConfig2ParaName' in data['user'] and
                            'deviceConfig2ParaValue' in data['user'] and
                            'deviceConfig3ParaName' in data['user'] and
                            'deviceConfig3ParaValue' in data['user'] and
                            'deviceConfig4ParaName' in data['user'] and
                            'deviceConfig4ParaValue' in data['user'] and
                            'deviceConfig5ParaName' in data['user'] and
                            'deviceConfig5ParaValue' in data['user']


                    ):
                        user = data['user']
                        deviceId = user['deviceId']
                        profileId = user['profileId']
                        deviceConfig1ParaName = user['deviceConfig1ParaName']
                        deviceConfig1ParaValue = user['deviceConfig1ParaValue']
                        deviceConfig2ParaName = user['deviceConfig2ParaName']
                        deviceConfig2ParaValue = user['deviceConfig2ParaValue']
                        deviceConfig3ParaName = user['deviceConfig3ParaName']
                        deviceConfig3ParaValue = user['deviceConfig3ParaValue']
                        deviceConfig4ParaName = user['deviceConfig4ParaName']
                        deviceConfig4ParaValue = user['deviceConfig4ParaValue']
                        deviceConfig5ParaName = user['deviceConfig5ParaName']
                        deviceConfig5ParaValue = user['deviceConfig5ParaValue']


                        response = createIOTworkingdata_fn(deviceId, profileId, deviceConfig1ParaName, deviceConfig1ParaValue, deviceConfig2ParaName, deviceConfig2ParaValue, deviceConfig3ParaName, deviceConfig3ParaValue, deviceConfig4ParaName,
                                                        deviceConfig4ParaValue, deviceConfig5ParaName, deviceConfig5ParaValue)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                else:
                        return JsonResponse({'message': 'Invalid operation'})  
            else:
                return JsonResponse({'message': 'Missing operation'})
        else:
                return JsonResponse({'message': 'Invalid request'})
    return JsonResponse({'Message: Success'})
# ---------------------------------------------------------------------------------------------------------------
