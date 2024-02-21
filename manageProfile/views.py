from .manageProfileFunction import *
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def manageProfile(request):
    if request.method == 'POST':
        if request.data:
            data = request.data

            if 'operation' in data:
                operation = data['operation']

                # if operation == 'register':
                #     if (
                #         'user' in data and
                #         'profileid' in data['user'] and
                #         'firstname' in data['user'] and
                #         'lastname' in data['user'] and
                #         'mobilenumber' in data['user'] and
                #         'village' in data['user'] and
                #         'primaryfunction' in data['user'] and
                #         'secondaryfunction' in data['user'] and
                #         'tehsil' in data['user'] and
                #         'district' in data['user'] and
                #         'state' in data['user'] and
                #         'funtionunit' in data['user'] and
                #         'volume' in data['user'] and
                #         'minimumrequirement' in data['user']


                #     ):
                #         user = data['user']
                #         profileid = user['profileId']
                #         firstname = user['firstName']
                #         lastname = user['lastName']
                #         mobilenumber = user['mobileNumber']
                #         village = user['village']
                #         primaryfunction = user['primaryFunction']
                #         secondaryfunction = user['secondaryFunction']
                #         tehsil = user['tehsil']
                #         district = user['district']
                #         state = user['state']
                #         funtionunit = user['funtionUnit']
                #         volume = user['volume']
                #         minimumrequirement = user['minimumRequirement']

                #         response = registerUser_fn(profileid, firstname, lastname, mobilenumber,
                #                                    village, primaryfunction, secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state)
                #         return JsonResponse(response)

                #     else:
                #         return "Wrong JSON data"
    # ------------------------------------------------------------------------------------------------
                if operation == 'createTertiaryProfile':
                    if (
                        'user' in data and
                        'priSecId' in data['user'] and
                        'profileId' in data['user'] and
                        'firstName' in data['user'] and
                        'lastName' in data['user'] and
                        'mobileNumber' in data['user'] and
                        'tertiaryFunction' in data['user'] and
                        'fourthFunction' in data['user'] and
                        'tertiaryFunctionVariety' in data['user'] and
                        'fourthFunctionVariety' in data['user'] and
                        'functionUnit' in data['user'] and
                        'volume' in data['user'] and
                        'minimumRequirement' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user']
                    ):
                        user = data['user']
                        prisecid = user['priSecId']
                        profileid = user['profileId']
                        firstname = user['firstName']
                        lastname = user['lastName']
                        mobilenumber = user['mobileNumber']
                        tertiaryfunction = user['tertiaryFunction']
                        fourthfunction = user['fourthFunction']
                        tertiaryfunctionvariety = user['tertiaryFunctionVariety']
                        fourthfunctionvariety = user['fourthFunctionVariety']
                        functionUnit = user['functionUnit']
                        volume = user['volume']
                        minimumrequirement = user['minimumRequirement']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']

                        response = createTertiaryProfile_fn(
                            prisecid, profileid, firstname, lastname, mobilenumber,
                            tertiaryfunction, fourthfunction, tertiaryfunctionvariety,
                            fourthfunctionvariety, functionUnit, volume, minimumrequirement,
                            village, tehsil, district, state
                        )

                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
    # -------------------------------------------------------------------------------
                elif operation == 'createProfile':
                    if (
                        'user' in data and
                        'firstName' in data['user'] and
                        'lastName' in data['user'] and
                        'mobileNumber' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user'] and 
                        'latitude' in data['user'] and 
                        'longitude' in data['user']
                    ):
                        user = data['user']
                        firstName = user['firstName']
                        lastName = user['lastName']
                        mobileNumber = user['mobileNumber']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']
                        latitude = user['latitude']
                        longitude = user['longitude']
                        response = createProfile_db(firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude)

                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})

# --------------------------------------------------------------------------------
                elif operation == 'deleteProfile':
                    if (
                        'user' in data and
                        'mobileNumber' in data['user'] and
                        'primaryFunction' in data['user'] and
                        'secondaryFunction' in data['user']
                    ):
                        user = data['user']
                        mobilenumber = user['mobileNumber']
                        primaryfunction = user['primaryFunction']
                        secondaryfunction = user['secondaryFunction']

                        response = deleteProfile_fn(mobilenumber, primaryfunction, secondaryfunction)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# ------------------------------------------------------------------
                elif operation == 'getProfile':
                    if 'mobileNumber' in data:
                        mobileNumber = data['mobileNumber']
                        response = getProfile_fn(mobileNumber)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})


# --------------------------------------------------------------------------------
                    
                elif operation == 'getUserData':
                    if 'mobileNumber' in data :
                        mobileNumber = data['mobileNumber']
                        response = getUserData_fn(mobileNumber)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})

# --------------------------------------------------------------------------------
                elif operation == 'createMultipleProfile' and 'user' in data:
                    users_data = data['user']

                    # Flatten the JSON tree structure into a list of user data
                    flattened_data = flatten_json_tree(users_data)

                    # Insert the flattened user data into the database
                    response = insertData(flattened_data)

                    if response:
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# --------------------------------------------------------------------------------
                elif operation == 'updateProfile':
                    if ('user' in data and
                        'firstName' in data['user'] and
                        'lastName' in data['user'] and
                        'mobileNumber' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user'] and
                        'latitude' in data['user'] and
                        'longitude' in data['user'] 
                        ):
                        user = data['user']
                        firstName = user['firstName']
                        lastName = user['lastName']
                        mobileNumber = user['mobileNumber']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']
                        latitude = user['latitude']
                        longitude = user['longitude']
                        response = updateProfile_fn(firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude)

                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# -----------------------------------------------------------------------------------------
            
                elif operation == 'getTertiaryProfile':
                    if 'profileId' in data:

                        profileId = data['profileId']

                        response = getTertiaryProfile_fn(profileId)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({"message": "Invalid parameters"})
                else:
                        return JsonResponse({'message': 'Invalid operation'})  
            else:
                return JsonResponse({'message': 'Missing operation'})
        else:
                return JsonResponse({'message': 'Missing request'})
    return JsonResponse({'Message: Success'})
# -------------------------------------------------------------------------------------------
