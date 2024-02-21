from .myGovermentFunction import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def myGoverment_api(request):
        if request.method == 'POST':
            if request.data:
                data = request.data

                if 'operation' in data:
                    operation = data['operation']

                    if operation == 'createGroup':
                        if (
                            'user' in data and
                            'groupName' in data['user'] and
                            'groupOwnerFirstName' in data['user'] and
                            'groupOwnerLastName' in data['user'] and
                            'groupOwnerMobile' in data['user'] and
                            'groupType' in data['user'] and
                            'groupActivity' in data['user'] and
                            'groupStatus' in data['user'] and
                            'groupNote' in data['user'] and
                            'village' in data['user'] and
                            'district' in data['user'] and
                            'state' in data['user'] and
                            'tehsil' in data['user'] and
                            'policyId' in data['user'] 
                        ):
                            user = data['user']
                            groupName = user['groupName']
                            groupOwnerFirstName = user['groupOwnerFirstName']
                            groupOwnerLastName = user['groupOwnerLastName']
                            groupOwnerMobile = user['groupOwnerMobile']
                            groupType = user['groupType']
                            groupActivity = user['groupActivity']
                            groupStatus = user['groupStatus']
                            groupNote = user['groupNote']
                            village = user['village']
                            district = user['district']
                            state = user['state']
                            tehsil = user['tehsil']
                            policyId = user['policyId']
    
                            response = createGroup_fn(groupName, groupOwnerFirstName, groupOwnerLastName, groupOwnerMobile,
                                                      groupType, groupActivity, groupStatus, groupNote, village, district, state, tehsil, policyId)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# ---------------------------------------------------------------------------------------------
                    elif operation == 'createMember':
                        if (
                            'user' in data and
                            'memberProfileId' in data['user'] and
                            'memberFirstName' in data['user'] and
                            'memberLastName' in data['user'] and
                            'memberMobile' in data['user'] and
                            'groupName' in data['user'] and
                            'groupId' in data['user'] and
                            'memberStatus' in data['user'] and
                            'village' in data['user'] and
                            'tehsil' in data['user'] and
                            'district' in data['user'] and
                            'state' in data['user']
                        ):
                            user = data['user']
                            memberProfileId = user['memberProfileId']
                            memberFirstName = user['memberFirstName']
                            memberLastName = user['memberLastName']
                            memberMobile = user['memberMobile']
                            groupName = user['groupName']
                            groupId = user['groupId']
                            memberStatus = user['memberStatus']
                            village = user['village']
                            tehsil = user['tehsil']
                            district = user['district']
                            state = user['state']
    
                            response = createMember_fn(memberProfileId, memberFirstName, memberLastName,memberMobile, groupName, groupId, memberStatus, village, tehsil, district, state)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# ---------------------------------------------------------------------------------------------
                    elif operation == 'getGroup':
                        if ('memberProfileId' in data and
                            'state' in data  and
                            'district'in data
                            ):
    
                            memberProfileId = data['memberProfileId']
                            state = data['state']
                            district = data['district']
                            response = getGroup_fn(state,district,memberProfileId)
                            
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})
# ---------------------------------------------------------------------------------------------
                    elif operation == 'getGroupByPolicy':
                        if ('policyId' in data ):
    
                            policyId = data['policyId']
                           
                            response = getGroupByPolicy_fn(policyId)
                            
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})
    #-------------------------------------------------------------------------------------------
                    elif operation == 'getGroupActivities':
                        if ('groupId' in data):

                            groupId = data['groupId']

                            response = getGroupActivities_fn(groupId)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})

    #-------------------------------------------------------------------------------------------
                    elif operation == 'getGroupDemandAvailability':
                        if ('groupId' in data):

                            groupId = data['groupId']

                            response = getGroupDemandAvailability_fn(groupId)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})                              
# ---------------------------------------------------------------------------------------------
                    elif operation == 'getPolicy':
                
                        if ('policyType' in data and
                            'state' in data and
                            'district' in data
                            ):
                                policyType = data['policyType'] 
                                state = data['state']
                                district = data['district'] 
                                
                                response = getPolicy_fn(policyType,state,district)
                                return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})
# ---------------------------------------------------------------------------------------------
                    elif operation == 'getMember':
                
                        if ('groupId' in data):
                                groupId = data['groupId']
                                response = getMember_fn(groupId)
                                return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})
# ------------------------------------------------------------------------------------------
                    elif operation == 'getDocument':
    
                        if ('policyId' in data):
    
                            policyId = data['policyId']
                            response = getDocument_fn(policyId)
                            return JsonResponse(response)
                        else:
                            return JsonResponse({'message': 'Invalid parameter'})
# ------------------------------------------------------------------------------------------

                    # elif operation == 'createBudget':
                    #     if (
                    #         'user' in data and
                    #         'profileId' in data['user'] and
                    #         'note' in data['user'] and
                    #         'date' in data['user'] and
                    #         'primaryFunction' in data['user'] and
                    #         'secondaryFunction' in data['user'] and
                    #         'amountType' in data['user'] and
                    #         'amountTypeFunction' in data['user'] and
                    #         'amount' in data['user'] 
                    #     ):
                    #         user = data['user']
                    #         profileId = user['profileId']
                    #         note = user['note']
                    #         date = user['date']
                    #         primaryFunction = user['primaryFunction']
                    #         secondaryFunction = user['secondaryFunction']
                    #         amountType = user['amountType']
                    #         amountTypeFunction = user['amountTypeFunction']
                    #         amount = user['amount']
    
                    #         response = createBudget_fn(profileId, note, date, primaryFunction,
                    #                                   secondaryFunction, amountType, amountTypeFunction, amount)
                    #         return JsonResponse(response)
                    #     else:
                    #         return ("Wrong JSON data")  
# ---------------------------------------------------------------------------------------------    
                    elif operation == 'deleteGroup':
    
                        if ('groupId' in data):
    
                            groupId = data['groupId']
                            response = deleteGroup_fn(groupId)
                            return response

                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})                  
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------    
                    elif operation == 'deleteMember':
    
                        if ('memberId' in data and
                            'groupId' in data):
    
                            memberId = data['memberId']
                            groupId = data['groupId']
                            response = deleteMember_fn(memberId,groupId)
                            return response

                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})                  
# ---------------------------------------------------------------------------------------------

                    elif operation == 'createUserPolicyDocument':
                        if (
                            'user' in data and
                            'groupOwnerMobileNumber' in data['user'] and
                            'documentId' in data['user'] and
                            'documentName' in data['user'] and
                            'documentType' in data['user'] and
                            'documentStatus' in data['user'] and
                            'documentCriteria' in data['user'] and
                            'documentDetails' in data['user'] and
                            'policyId' in data['user'] and
                            'policyName' in data['user'] and 
                            'last_update_date'in data['user'] and 
                            'DueDate' in data['user']
                        ):
                            user = data['user']
                            groupOwnerMobileNumber = user['groupOwnerMobileNumber']
                            documentId = user['documentId']
                            documentName = user['documentName']
                            documentType = user['documentType']
                            documentStatus = user['documentStatus']
                            documentCriteria = user['documentCriteria']
                            documentDetails = user['documentDetails']
                            policyId = user['policyId']
                            policyName = user['policyName']
                            last_update_date = user['last_update_date']
                            DueDate = user['DueDate']
    
                            response = createUserPolicyDocument_fn(groupOwnerMobileNumber, documentId, documentName,documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'}) 
# ---------------------------------------------------------------------------------------------
                    elif operation == 'getUserPolicyDocument':
                        if ('groupOwnerMobileNumber' in data and 'policyId' in data):
                            groupOwnerMobileNumber = data['groupOwnerMobileNumber']
                            policyId = data['policyId']
                            response = getUserPolicyDocument_fn(groupOwnerMobileNumber, policyId)

                            # Check if the response is a dictionary
                            if isinstance(response, dict):
                                return JsonResponse(response)
                            else:
                                return JsonResponse({'message': 'Invalid parameter'}, safe=False)
# ---------------------------------------------------------------------------------------------
                    elif operation == 'UpdateUserPolicyDocument':
                        if ('user' in data and
                            'groupOwnerMobileNumber' in data['user'] and
                            'documentId' in data['user'] and
                            'documentName' in data['user'] and
                            'documentType' in data['user'] and
                            'documentStatus' in data['user'] and
                            'documentCriteria' in data['user'] and
                            'documentDetails' in data['user'] and
                            'policyId' in data['user'] and
                            'policyName' in data['user'] and 
                            'last_update_date'in data['user'] and 
                            'DueDate' in data['user']
                        ):
                            user = data['user']
                            groupOwnerMobileNumber = user['groupOwnerMobileNumber']
                            documentId = user['documentId']
                            documentName = user['documentName']
                            documentType = user['documentType']
                            documentStatus = user['documentStatus']
                            documentCriteria = user['documentCriteria']
                            documentDetails = user['documentDetails']
                            policyId = user['policyId']
                            policyName = user['policyName']
                            last_update_date = user['last_update_date']
                            DueDate = user['DueDate']

                            response = UpdateUserPolicyDocument_fn(groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)
                            return response
                        else:
                            return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                else:
                    return JsonResponse({'result': 'failure','message': 'Missing operation'})
            else:
                    return JsonResponse({'result': 'failure','message': 'Missing request'})

        return JsonResponse({'Message: Success'})