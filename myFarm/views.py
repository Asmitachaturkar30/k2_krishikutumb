from .myFarmFunction import *
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def myFarm_api(request):
        if request.method == 'POST':
            if request.data:
                data = request.data

                if 'operation' in data:
                    operation = data['operation']
#-------------------------------------------------------------------------------------------------------------------------------
                    if operation == 'createFarmDetails':
                        if (    
                            'user' in data and
                            'profileId' in data['user'] and
                            'farmName' in data['user'] and
                            'farmType' in data['user'] and
                            'soilType' in data['user'] and
                            'farmStatus' in data['user'] and
                            'farmSizeInAcre' in data['user'] and
                            'farmElectricity' in data['user'] and
                            'waterPHValue' in data['user'] and
                            'farmWaterSource' in data['user']):
                            
                            user = data['user']
                            profileId = user['profileId']
                            farmName = user['farmName']
                            farmType = user['farmType']
                            soilType = user['soilType']
                            farmStatus = user['farmStatus']
                            farmSizeInAcre = user['farmSizeInAcre']
                            farmElectricity = user['farmElectricity']
                            waterPHValue = user['waterPHValue']
                            farmWaterSource = user['farmWaterSource']

                            response = createFarmDetails_fn(profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'}) 
        #-------------------------------------------------------------------------------------------               
        # ---------------------------------------------------------------------------------------------------------------
                    elif operation == 'createFarmerCropScheduleMulitRow':
                        if 'user' in data:
                            user_data = data['user']
                
                            flat_data = createFarmerCropScheduleMulitRow_fn(user_data)

                            # Insert the flattened user data into the database
                            response = createFarmerCropScheduleMulitRow_db(flat_data)

                            return (response)
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
        # -------------------------------------------------------------------------------------------------------------------------- 
                    elif operation == 'deleteFarm':
                        if ('user' in data and
                            'profileId' in data['user'] and
                            'farmId' in data['user'] ):

                            user = data['user']
                            profileId = user['profileId']
                            farmId = user['farmId']

                            response = deleteFarm_fn(profileId,farmId)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'}) 
        # ----------------------------------------------------------------------------------------------------------------------
                    elif operation == 'deleteFarmerCropSchedule':
                        if ('user' in data and
                            'profileId' in data['user'] and
                            'farmId' in data['user'] and
                            'cropName' in data['user'] 
                        ):

                            user = data['user']
                            profileId = user['profileId']
                            farmId = user['farmId']
                            cropName = user['cropName']

                            response = deleteFarmerCropSchedule_fn(profileId,farmId, cropName)
                            return JsonResponse(response,safe=False)
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
        #----------------------------------------------------------------------------------- 

                    elif operation == 'getCrops':
                        if ('state' in data and
                            'district' in data
                        ):

                            state = data['state']
                            district = data['district']
                            response = getCrops_fn(state, district)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})
        # -----------------------------------------------------------------------------------------
                    elif operation == 'getCropSchedule':
                        if ('state' in data and
                            'district' in data and
                            'cropName' in data
                            ):

                            state = data['state']
                            district = data['district']
                            cropName = data['cropName']

                            response = getCropSchedule_fn(
                                state, district,cropName)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})  
        # -----------------------------------------------------------------------------------------
                    elif operation == 'getFarmDetails':
                        if ('profileId' in data ):

                            profileId = data['profileId']

                            response = getFarmDetails_fn(profileId)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'}) 

        #-------------------------------------------------------------------------------------------
                    elif operation == 'getFarmerCropSchedule':
                        if ('profileId' in data and
                            'farmId' in data and
                            'cropName' in data):

                            profileId = data['profileId']
                            farmId = data['farmId']
                            cropName = data['cropName']

                            response = getFarmerCropSchedule_fn(profileId, farmId,cropName)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameters'})                     
        # ---------------------------------------------------------------------------------------------------------------
                    
                    elif operation == 'updateFarmerCropSchedule' and 'user' in data:

                        users = data['user']

                        flattened_data1 = updateFarmerCropSchedule_fn(users)
                        response = updateFarmerCropSchedule_db(flattened_data1)
                        
                        return response
 # ---------------------------------------------------------------------------------------------------------------                   
                    elif operation == 'updateFarmDetails':
                        if (    
                            'user' in data and
                            'farmId' in data['user'] and
                            'profileId' in data['user'] and 
                            'farmName' in data['user'] and
                            'farmType' in data['user'] and
                            'soilType' in data['user'] and
                            'farmStatus' in data['user'] and
                            'farmSizeInAcre' in data['user'] and
                            'farmElectricity' in data['user'] and
                            'waterPHValue' in data['user'] and
                            'farmWaterSource' in data['user']):
                            
                            user = data['user']
                            farmId = user['farmId']
                            profileId = user['profileId']
                            farmName = user['farmName']
                            farmType = user['farmType']
                            soilType = user['soilType']
                            farmStatus = user['farmStatus']
                            farmSizeInAcre = user['farmSizeInAcre']
                            farmElectricity = user['farmElectricity']
                            waterPHValue = user['waterPHValue']
                            farmWaterSource = user['farmWaterSource']

                            response = updateFarmDetails_fn(farmId,profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                else:
                    return JsonResponse({'message': 'Invalid operation'})
            else:
                return JsonResponse({'message': 'Missing reqest'})
        return JsonResponse({'Message: Success'})

    # -----------------------------------------------------------------------------------------------