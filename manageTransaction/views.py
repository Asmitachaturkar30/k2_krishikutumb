from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .managTransationFunction import *


@api_view(['POST'])
def transation_api(request):
    if request.method == 'POST':
        if request.data:
            data = request.data

            if 'operation' in data:
                operation = data['operation']

                if operation == 'registerAvailabilityDemand':
                    if (
                        'user' in data and
                        'mobileNumber' in data['user'] and
                        'demandType' in data['user'] and
                        'demandPrimaryFunction' in data['user'] and
                        'demandSecondaryFunction' in data['user'] and
                        'demandTertiaryFunction' in data['user'] and
                        'demandTertiaryFunctionVarity' in data['user'] and
                        'demandFourthFunction' in data['user'] and
                        'demandFourthFunctionVarity' in data['user'] and
                        'demandInUnit' in data['user'] and
                        'demandDate' in data['user'] and
                        'demandNote' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user']
                    ):
                        user = data['user']
                        mobileNumber = user['mobileNumber']
                        demandType = user['demandType']
                        demandPrimaryFunction = user['demandPrimaryFunction']
                        demandSecondaryFunction = user['demandSecondaryFunction']
                        demandTertiaryFunction = user['demandTertiaryFunction']
                        demandTertiaryFunctionVarity = user['demandTertiaryFunctionVarity']
                        demandFourthFunction = user['demandFourthFunction']
                        demandFourthFunctionVarity = user['demandFourthFunctionVarity']
                        demandInUnit = user['demandInUnit']
                        demandDate = user['demandDate']
                        demandNote = user['demandNote']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']


                        response = registerAvailabilityDemand_fn(mobileNumber,demandType,demandPrimaryFunction,demandSecondaryFunction,demandTertiaryFunction,demandTertiaryFunctionVarity,
                                    demandFourthFunction,demandFourthFunctionVarity,demandInUnit,demandDate,demandNote,village,tehsil,district,state)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})        
        #----------------------------------------------------------------------------------- 
        #-------------------------------------------------------------------------------------------
                elif operation == 'doBooking':
                    if (
                        'user' in data and
                        'consumerMobileNumber' in data['user'] and
                        'providerMobileNumber' in data['user'] and
                        'bookingType' in data['user'] and
                        'isBookingExpired' in data['user'] and
                        'bookingStatus' in data['user'] and
                        'bookingPrimaryFunction' in data['user'] and
                        'bookingSecondaryFunction' in data['user'] and
                        'bookingTertiaryFunction' in data['user'] and
                        'bookingTertiaryFunctionVarity' in data['user'] and
                        'bookingFourthFunction' in data['user'] and
                        'bookingFourthFunctionVarity' in data['user'] and
                        'bookingInUnit' in data['user']and
                        'bookingDate' in data['user']and
                        'bookingNote' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user']
                    ):
                        user = data['user']
                        consumerMobileNumber = user['consumerMobileNumber']
                        providerMobileNumber = user['providerMobileNumber']
                        bookingType = user['bookingType']
                        isBookingExpired = user['isBookingExpired']
                        bookingStatus = user['bookingStatus']
                        bookingPrimaryFunction = user['bookingPrimaryFunction']
                        bookingSecondaryFunction = user['bookingSecondaryFunction']
                        bookingTertiaryFunction = user['bookingTertiaryFunction']
                        bookingTertiaryFunctionVarity = user['bookingTertiaryFunctionVarity']
                        bookingFourthFunction = user['bookingFourthFunction']
                        bookingFourthFunctionVarity = user['bookingFourthFunctionVarity']
                        bookingInUnit = user['bookingInUnit']
                        bookingDate = user['bookingDate']
                        bookingNote = user['bookingNote']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']

                        response = doBooking_fn(consumerMobileNumber,providerMobileNumber,bookingType,isBookingExpired,bookingStatus,bookingPrimaryFunction,
                                    bookingSecondaryFunction,bookingTertiaryFunction,bookingTertiaryFunctionVarity,bookingFourthFunction,bookingFourthFunctionVarity,
                                    bookingInUnit,bookingDate,bookingNote,village,tehsil,district,state)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'}) 
        #-------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------

                elif operation == 'getBooking':
                    if(
                        'providerMobileNumber' in data and 
                        'bookingPrimaryFunction' in data and 
                        'bookingSecondaryFunction' in data and 
                        'bookingTertiaryFunction' in data
                    ):
                        providerMobileNumber = data['providerMobileNumber']
                        bookingPrimaryFunction = data['bookingPrimaryFunction']
                        bookingSecondaryFunction = data['bookingSecondaryFunction']
                        bookingTertiaryFunction = data['bookingTertiaryFunction']

                        response = getBooking_fn(providerMobileNumber, bookingPrimaryFunction, bookingSecondaryFunction, bookingTertiaryFunction)
                        
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'}) 
        # ---------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------

                elif operation == 'getTertiaryContacts':
                    if ('primaryFunction' in data and
                        'secondaryFunction' in data and
                        'tertiaryFunction' in data and
                        'tertiaryFunctionVariety' in data and
                        'fourthFunction' in data and
                        'fourthFunctionVariety' in data and
                        'village' in data and
                        'tehsil' in data
                    ):

                        primaryFunction = data['primaryFunction']
                        secondaryFunction = data['secondaryFunction']
                        tertiaryFunction = data['tertiaryFunction']
                        tertiaryFunctionVariety = data['tertiaryFunctionVariety']
                        fourthFunction = data['fourthFunction']
                        fourthFunctionVariety = data['fourthFunctionVariety']
                        village = data['village']
                        tehsil = data['tehsil']

                        response = getTertiaryContacts_fn(primaryFunction, secondaryFunction, tertiaryFunction, tertiaryFunctionVariety, fourthFunction, fourthFunctionVariety, village, tehsil)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'}) 
        # ----------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------

                elif operation == 'getContacts':
                    if ('mobileNumber' in data and
                        'primaryFunction' in data and
                        'secondaryFunction' in data and
                        'village' in data and
                        'tehsil' in data
                    ):

                        mobileNumber = data['mobileNumber']
                        primaryFunction = data['primaryFunction']
                        secondaryFunction = data['secondaryFunction']
                        village = data['village']
                        tehsil = data['tehsil']

                        response = getContacts_fn(mobileNumber, primaryFunction,secondaryFunction,village,tehsil)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'}) 
  # ----------------------------------------------------------------------------------               

                elif operation == 'createDevice':
                    if (
                        'user' in data and
                        'profileId' in data['user'] and
                        'mobileNumber' in data['user'] and
                        'Notes' in data['user'] and
                        'Description' in data['user']
                    ):
                        user = data['user']
                        profileId = user['profileId']
                        mobileNumber = user['mobileNumber']
                        Notes = user['Notes']
                        Description = user['Description']

                        response = createDevice_fn(profileId, mobileNumber, Notes, Description)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                    
  # ----------------------------------------------------------------------------------                   
                elif operation == 'getDeviceDetails':
                    if ('profileId' in data and
                        'mobileNumber' in data
                    ):
                        profileId = data['profileId'] 
                        mobileNumber = data['mobileNumber']
                        response = getDeviceDetails_fn(profileId, mobileNumber)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})

 # ----------------------------------------------------------------------------------       
                elif operation == 'UpdateBooking':
                    if (
                        'user' in data and
                        'bookingId' in data['user'] and
                        'bookingType' in data['user'] and
                        'isBookingExpired' in data['user'] and
                        'bookingStatus' in data['user'] and
                        'bookingInUnit' in data['user']and
                        'bookingDate' in data['user']and
                        'bookingNote' in data['user'] 
                        
                    ):
                        user = data['user']
                        bookingId = user['bookingId']
                        bookingType = user['bookingType']
                        isBookingExpired = user['isBookingExpired']
                        bookingStatus = user['bookingStatus']
                        bookingInUnit = user['bookingInUnit']
                        bookingDate = user['bookingDate']
                        bookingNote = user['bookingNote']
                       
                        response = UpdateBooking_fn(bookingId,bookingType,isBookingExpired,bookingStatus,
                                    bookingInUnit,bookingDate,bookingNote)

                        return JsonResponse(response)
                    else:
                        return JsonResponse({'maffage' : 'invalid parameters'})
# ---------------------------------------------------------------------------------- 
                elif operation == 'doBookingNotific':
                    if (
                        'user' in data and
                        'consumerMobileNumber' in data['user'] and
                        'providerMobileNumber' in data['user'] and
                        'bookingType' in data['user'] and
                        'isBookingExpired' in data['user'] and
                        'bookingStatus' in data['user'] and
                        'bookingPrimaryFunction' in data['user'] and
                        'bookingSecondaryFunction' in data['user'] and
                        'bookingTertiaryFunction' in data['user'] and
                        'bookingTertiaryFunctionVarity' in data['user'] and
                        'bookingFourthFunction' in data['user'] and
                        'bookingFourthFunctionVarity' in data['user'] and
                        'bookingInUnit' in data['user']and
                        'bookingDate' in data['user']and
                        'bookingNote' in data['user'] and
                        'village' in data['user'] and
                        'tehsil' in data['user'] and
                        'district' in data['user'] and
                        'state' in data['user'] and
                        'providerToken' in data['user']
                    ):
                        user = data['user']
                        consumerMobileNumber = user['consumerMobileNumber']
                        providerMobileNumber = user['providerMobileNumber']
                        bookingType = user['bookingType']
                        isBookingExpired = user['isBookingExpired']
                        bookingStatus = user['bookingStatus']
                        bookingPrimaryFunction = user['bookingPrimaryFunction']
                        bookingSecondaryFunction = user['bookingSecondaryFunction']
                        bookingTertiaryFunction = user['bookingTertiaryFunction']
                        bookingTertiaryFunctionVarity = user['bookingTertiaryFunctionVarity']
                        bookingFourthFunction = user['bookingFourthFunction']
                        bookingFourthFunctionVarity = user['bookingFourthFunctionVarity']
                        bookingInUnit = user['bookingInUnit']
                        bookingDate = user['bookingDate']
                        bookingNote = user['bookingNote']
                        village = user['village']
                        tehsil = user['tehsil']
                        district = user['district']
                        state = user['state']
                        providerToken = user['providerToken']

                        response = doBookingNotific_fn(consumerMobileNumber,providerMobileNumber,bookingType,isBookingExpired,bookingStatus,bookingPrimaryFunction,
                                    bookingSecondaryFunction,bookingTertiaryFunction,bookingTertiaryFunctionVarity,bookingFourthFunction,bookingFourthFunctionVarity,
                                    bookingInUnit,bookingDate,bookingNote,village,tehsil,district,state,providerToken)
                        return response
                    print("Response from create_device:", response)

                    # if response['result'] == 'success':
                    #     if "Device created" in response.get("message", ""):
                    #         print("Condition met for device creation. Proceeding to notification.")
                    #         notification_result = send_notification(providerToken, "New Device Created", "Your new device is ready!", response)
                    #         print("Notification result:", notification_result)

                    #         if notification_result and notification_result.get('success'):
                    #             print("Notification success. Returning success response.")
                    #             return JsonResponse({'result': 'success', 'message': 'Device created, and notification sent successfully'})
                    #         else:
                    #             print("Notification failed. Returning failure response.")
                    #             return JsonResponse({'result': 'failure', 'message': 'Device created, but failed to send notification'})
                    #     elif "Device updated" in response.get("message", ""):
                    #         print("Condition met for device update. Returning success response.")
                    #         return JsonResponse({'result': 'success', 'message': 'Device updated successfully'})
                    #     else:
                    #         print("Unexpected response message. Returning original response.")
                    #         return JsonResponse(response)
                    # else:
                    #     print("Device creation/update failed. Returning failure response.")
                    #         return JsonResponse(response)
                    # else:
                    #     return JsonResponse({'result': 'failure','message': 'Missing parameter'}) 
        #-------------------------------------------------------------------------------------------
                elif operation == 'getContactsNearby':
                    if ('mobileNumber' in data and
                        'primaryFunction' in data and
                        'secondaryFunction' in data and
                        'village' in data and
                        'tehsil' in data and 
                        'nearbyRange' in data and
                        'latitude' in data and
                        'longitude' in data 
                    ):

                        mobileNumber = data['mobileNumber']
                        primaryFunction = data['primaryFunction']
                        secondaryFunction = data['secondaryFunction']
                        village = data['village']
                        tehsil = data['tehsil']
                        nearbyRange = data['nearbyRange']
                        latitude =data['latitude']
                        longitude =data['longitude']

                        response = getContactsNearby_fn(mobileNumber, primaryFunction, secondaryFunction, village, tehsil, nearbyRange,
                                                        latitude,longitude)
                        return JsonResponse(response)
                    else:
                        return JsonResponse({'message': 'Invalid parameters'})
                else:
                    return JsonResponse({'message': 'Invalid operation'})                
            else:
                return JsonResponse({'message': 'Missing operation'})
        else:
                return JsonResponse({'message': 'Missing request'})
    return JsonResponse({'Message: Success'})
