#!/usr/bin/python
from .myGovermentDbOperation import *
from django.http import JsonResponse


def getMsgParamNotEmpty():
    return JsonResponse({'result': 'failure','message': 'JSON Invalid Parameters.'})
#---------------------------------------------------------------------------------------------

def createGroup_fn(groupName, groupOwnerFirstName, groupOwnerLastName, groupOwnerMobile,
                                                groupType, groupActivity, groupStatus, groupNote, village, tehsil, district, state, policyId):


    if (groupName and groupOwnerFirstName and groupOwnerLastName and groupOwnerMobile and 
        groupType and groupActivity and groupStatus and groupNote and village and tehsil and district and state and policyId):

        response = createGroup_db(groupName, groupOwnerFirstName, groupOwnerLastName, groupOwnerMobile,groupType, groupActivity, groupStatus, groupNote, village, tehsil, district, state, policyId)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ----------------------------------------------------------------------

def createMember_fn(memberProfileId, memberFirstName, memberLastName,memberMobile, groupName, groupId, memberStatus, village, tehsil, district, state):


    if (memberProfileId and memberFirstName and memberLastName and memberMobile and groupName and groupId and memberStatus and village and tehsil and district and state):

        response = createMember_db(memberProfileId, memberFirstName, memberLastName,memberMobile, groupName, groupId, memberStatus, village, tehsil, district, state)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
    
# ----------------------------------------------------------------

def getMember_fn(groupId):
    result = getMember_db(groupId)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "memberId": item[0],
                "memberProfileId": item[1],
                "memberFirstName": item[2],
                "memberLastName": item[3],
                "memberMobile": item[4],
                "groupName": item[5],
                "groupId": item[6],
                "memberStatus": item[7],
                "village": item[8],
                "tehsil": item[9],
                "district": item[10],
                "state": item[11]
            }
            response["userList"].append(data)
            return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response
# ----------------------------------------------------------------

def getPolicy_fn(policyType,state,district):
    result = getPolicy_db(policyType,state,district)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "policyId": item[0],
                "policyName": item[1],
                "policyType": item[2],
                "policyActivity": item[3],
                "policyStatus": item[4],
                "nationalPolicy": item[5],
                "statePolicy": item[6],
                "districtPolicy": item[7],
                "district": item[8],
                "state": item[9]
            }
            response["userList"].append(data)
            return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response
# ----------------------------------------------------------------
def getGroupByPolicy_fn(policyId):
    result = getGroupByPolicy_db(policyId)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
                data = {
                    "groupId": item[0],
                    "allGroup": item[1],
                    "groupName": item[2],
                    "groupOwnerFirstName": item[3],
                    "groupOwnerLastName": item[4],
                    "groupOwnerMobile": item[5],
                    "groupType": item[6],
                    "groupActivity": item[7],
                    "groupStatus": item[8],
                    "groupNote": item[9],
                    "village": item[10],                    
                    "tehsil": item[11],
                    "district": item[12],
                    "state": item[13]
                    
                }
                response["userList"].append(data)
                return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response
      
#---------------------------------------------------------
def getGroup_fn(state,district,memberProfileId):
    result = getGroup_db(state,district,memberProfileId)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
                data = {
                    "groupId": item[0],
                    "allGroup": item[1],
                    "groupName": item[2],
                    "groupOwnerFirstName": item[3],
                    "groupOwnerLastName": item[4],
                    "groupOwnerMobile": item[5],
                    "groupType": item[6],
                    "groupActivity": item[7],
                    "groupStatus": item[8],
                    "groupNote": item[9],
                    "village": item[10],                    
                    "tehsil": item[11],
                    "district": item[12],
                    "state": item[13]
                    
                }
                response["userList"].append(data)
                return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response
        
    
# ------------------------------------------------------------------------------------------

def getDocument_fn(policyId):
    result = getDocument_db(policyId)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "documentId": item[0],
                "documentName": item[1],
                "documentType": item[2],
                "documentStatus": item[3],
                "documentCriteria": item[4],
                "documentDetails": item[5],
                "policyId": item[6],
                "policyName": item[7]
                
            }
            response["userList"].append(data)

        response["userList"].append(data)
        return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    
# ------------------------------------------------------------------------------------------
def deleteGroup_fn(groupId):
    response = deleteGroup_db(groupId)
    if response :
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ------------------------------------------------------------------------------------------
def deleteMember_fn(memberId,groupId):
    response = deleteMember_db(memberId,groupId)

    if response:
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# ------------------------------------------------------------------------------------------------------------
def getGroupActivities_fn(groupId):
    result = getGroupActivities_db(groupId)

    data = []
    if result is not None:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "id": item[0],
                "profileId": item[1],
                "farmId": item[2],
                "cropName": item[3],
                "activitySequence": item[4],
                "activityName": item[5],
                "activityNameLocal": item[6],
                "activityExpectedInDays": item[7],
                "needHelp": item[8],
                "expenses": item[9],
                "doneOrSkip": item[10],
                "activityExpectedStartDate": item[11],
                "activityCompletedDate": item[12],
                "activityRescheduledDate": item[13]
            }
            response["userList"].append(data)
            return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response

# ------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
def getGroupDemandAvailability_fn(groupId):
    result = getGroupDemandAvailability_db(groupId)

    data = []
    if result is not None:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "profileId": item[0],
                "firstName": item[1],
                "lastName": item[2],
                "primaryFunction": item[3],
                "secondaryFunction": item[4],				
                "mobileNumber": item[5],
                "village": item[6],
                "priority": item[7],
                "demandType": item[8]
            }
            response["userList"].append(data)

        response["userList"].append(data)
        return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    					
# -----------------------------------------------------------------------------------



def createUserPolicyDocument_fn( groupOwnerMobileNumber, documentId, documentName, documentType,
                                                  documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate):

    if (groupOwnerMobileNumber and documentId and documentName and documentType and 
        documentStatus and documentCriteria and documentDetails and policyId and policyName and last_update_date and DueDate):

        response = createUserPolicyDocument_db( groupOwnerMobileNumber, documentId, documentName, documentType,documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

#--------------------------------------------------------	
		
def getUserPolicyDocument_fn(groupOwnerMobileNumber, PolicyId):
    result = getUserPolicyDocument_db(groupOwnerMobileNumber, PolicyId)
    
    data = []
    if result is not None:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "groupOwnerMobileNumber" : item[0],
				"documentId" : item[1],
				"documentName" : item[2],
				"documentType" : item[3],
				"documentStatus" : item[4],
				"documentCriteria" : item[5],
				"documentDetails" : item[6],
				"policyId" : item[7],
				"policyName" : item[8],
                "last_update_date" : item[9],
                "DueDate" : item[10]
            }
            response["userList"].append(data)
            return response 
        
    elif result is None:
        Jresponse = {
            "result": "failure",
            "message": "No data found"
        }
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }
        return response
    return response

#--------------------------------------------------------

def UpdateUserPolicyDocument_fn(groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate):
    if groupOwnerMobileNumber and documentId and documentName and documentType and documentStatus and documentCriteria and documentDetails and policyId and policyName and last_update_date and DueDate:
        response = UpdateUserPolicyDocument_db(groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response