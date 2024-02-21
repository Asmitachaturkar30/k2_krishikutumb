import datetime
from .myFarmDBOperation import *
from django.http import JsonResponse


 # ------------------------------------------------------------------------------------------
def getMsgParamNotEmpty():
    return JsonResponse({'result': 'failure','message': 'JSON Invalid Parameters.'})

 # ------------------------------------------------------------------------------------------
def createFarmDetails_fn(profileId, farmName, farmType, soilType, farmStatus, farmSizeInAcre, farmElectricity,
                         waterPHValue, farmWaterSource):

    if ( profileId and farmName and farmType and soilType and farmStatus and farmSizeInAcre and farmElectricity and
            waterPHValue and farmWaterSource):
                
        response = createFarmDetails_db(profileId, farmName, farmType, soilType, farmStatus, farmSizeInAcre, farmElectricity,
                                      waterPHValue, farmWaterSource)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# ------------------------------------------------------------------------------------------
def createFarmerCropScheduleMulitRow_fn(user_data):
    try:
        flat_data = []
    
        if isinstance(user_data, list):
            for item in user_data:
                # Pass parent_profileId to the recursive call
                child_data = createFarmerCropScheduleMulitRow_fn(item)
                flat_data.extend(child_data)
        elif isinstance(user_data, dict):
            # Get the user data from the current level of the tree
                profileId = user_data.get('profileId')
                farmId = user_data.get('farmId')
                cropStatus = user_data.get('cropStatus')
                cropName = user_data.get('cropName')
                activitySequence = user_data.get('activitySequence')
                activityName = user_data.get('activityName')
                activityNameLocal = user_data.get('activityNameLocal')
                activityExpectedInDays = user_data.get('activityExpectedInDays')
                needHelp = user_data.get('needHelp')
                expenses = user_data.get('expenses')
                doneOrSkip = user_data.get('doneOrSkip')
                activityExpectedStartDate = user_data.get('activityExpectedStartDate')
                activityCompletedDate = user_data.get('activityCompletedDate')
                activityRescheduledDate = user_data.get('activityRescheduledDate')
    
    
                if None in (profileId, farmId, cropStatus, cropName, activitySequence, activityName, activityNameLocal, activityExpectedInDays,
                            needHelp, expenses, doneOrSkip, activityExpectedStartDate, activityCompletedDate, activityRescheduledDate):
                    return []
                    # Append the current user data to the flattened_data list, including the parent_profileId
                activityExpectedStartDate = datetime.strptime(activityExpectedStartDate, '%d-%m-%Y %H:%M:%S %A')
                activityCompletedDate = datetime.strptime(activityCompletedDate, '%d-%m-%Y %H:%M:%S %A')
                activityRescheduledDate = datetime.strptime(activityRescheduledDate, '%d-%m-%Y %H:%M:%S %A')
                    
                flat_data.append((profileId, farmId, cropStatus, cropName, activitySequence, activityName, activityNameLocal, activityExpectedInDays,
                            needHelp, expenses, doneOrSkip, activityExpectedStartDate, activityCompletedDate, activityRescheduledDate))

    
                if 'children' in user_data:
                    children = user_data['children']
                    for child_user_data in children:
                        # Call the function recursively for each child user data with the parent_profileId set to the current user's profileId
                        child_data = createFarmerCropScheduleMulitRow_fn(child_user_data)
                        flat_data.extend(child_data)

        return flat_data
    
    except :
            return ("there must be an error in create function." )
# -------------------------------------------------------------------------------------------


def deleteFarm_fn(profileId,farmId):
    response = deleteFarm_db(profileId,farmId)
    if response:
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response 
# ---------------------------------------------------------------------------------------------

def deleteFarmerCropSchedule_fn(profileId, farmId, cropName):
    if profileId and farmId:
        
        response = deleteFarmerCropSchedule_db(profileId, farmId, cropName)

        return response
    else:
        response = ({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ------------------------------------------------------------------------------------------


# def getCrops_fn(state, district):
#     result = getCrops_db(state, district)

#     data = []
#     if result is not None and isinstance(result, list):
#         if len(result) > 0:
#             response = {
#                 "result": "success",
#                 "message": "success",
#                 "userList": []
#             }

#             for item in result:
#                 data = {
#                     "id": item[0],
#                     "cropType": item[1],
#                     "cropNameEnglish": item[2],
#                     "cropNameHindi": item[3],
#                     "cropImageName": item[4]

#                 }
#                 response["userList"].append(data)

#             return response
#         else:
#             response = JsonResponse({
#                 "result": "error",
#                 "message": "No data found"
#             })
#             return response
#     else:
#         # Handle unexpected or suspicious data
#         return ({"result": "error", "message": "Unexpected data format"})



def getCrops_fn(state, district):
    result = getCrops_db(state, district)

    if result is not None:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            if len(item) >= 5:
                data = {
                    "id": str(item[0]),
                    "cropType": str(item[1]),
                    "cropNameEnglish": str(item[2]),
                    "cropNameHindi": str(item[3]),
                    "cropImageName": str(item[4])
                }
                response["userList"].append(data)
            else:
                # Log a message about the unexpected data format
                return (f"Unexpected data format for item: {item}")

        return response
    else:
        return ({"result": "error", "message": "No data found"})
# ------------------------------------------------------------------------------------------

def getCropSchedule_fn(state, district, cropName):
    result = getCropSchedule_db(state, district, cropName)

    data = []
    if result:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "id": item[0],
                "cropName": item[1],
                "activitySequence": item[2],
                "activityName": item[3],
                "activityNameLocal": item[4],
                "activityExpectedInDays": item[5]

            }
            response["userList"].append(data)

        return response
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response
# ------------------------------------------------------------------------------------------
def getFarmDetails_fn(profileId):
    result = getFarmDetails_db(profileId)

    data = []
    if result:
        response = {
            "result": "success",
            "message": "success",
            "userList": []
        }

        for item in result:
            data = {
                "farmId": item[0],
                "profileId": item[1],
                "farmName": item[2],
                "farmType": item[3],
                "soilType": item[4],
                "farmStatus": item[5],
                "farmSizeInAcre": item[6],
                "farmElectricity": item[7],
                "waterPHValue": item[8],
                "farmWaterSource": item[9],
                "scheduledCropsName": item[10]
            }
            response["userList"].append(data)

        return response
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response

# ------------------------------------------------------------------------------------------------------------
def getFarmerCropSchedule_fn(profileId, farmId, cropName):
    result = getFarmerCropSchedule_db(profileId, farmId, cropName)

    data = []
    if result:
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
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response

# ------------------------------------------------------------------------------------------
# def updateFarmerCropSchedule_fn(users):
#     flattened_data1 = []
#     if isinstance(users, list):
#         for item in users:
#             child = updateFarmerCropSchedule_fn(item)
#             flattened_data1.extend(child)
#     elif isinstance(users, dict):
#         id = users.get('id')
#         profileId = users.get('profileId')
#         farmId = users.get('farmId')
#         needHelp = users.get('needHelp')
#         expenses = users.get('expenses')
#         doneOrSkip = users.get('doneOrSkip')
#         activityExpectedStartDate = users.get('activityExpectedStartDate')
#         activityCompletedDate = users.get('activityCompletedDate')
#         activityRescheduledDate = users.get('activityRescheduledDate')

#         if None in ( needHelp, expenses, doneOrSkip, activityExpectedStartDate, activityCompletedDate, activityRescheduledDate, profileId, farmId, id):
#             return []
            
#         activityExpectedStartDate = datetime.strptime(activityExpectedStartDate, '%d-%m-%Y %H:%M:%S %A')
#         activityCompletedDate = datetime.strptime(activityCompletedDate, '%d-%m-%Y %H:%M:%S %A')
#         activityRescheduledDate = datetime.strptime(activityRescheduledDate, '%d-%m-%Y %H:%M:%S %A')      
        
#         flattened_data1.append(( needHelp, expenses, doneOrSkip,
#                                activityExpectedStartDate, activityCompletedDate, activityRescheduledDate, profileId, farmId, id))
#         if 'children' in users:
#             children = users['children']
#             for child_user_data in children:
#                 child_user_update = updateFarmerCropSchedule_fn(child_user_data)
#                 flattened_data1.extend(child_user_update)
#     return flattened_data1

# --------------------------------------------------------------------------------------------

def updateFarmerCropSchedule_fn(users):
    flattened_data1 = []
    for user in users:
        id = user.get('id')
        profileId = user.get('profileId')
        farmId = user.get('farmId')
        needHelp = user.get('needHelp')
        expenses = user.get('expenses')
        doneOrSkip = user.get('doneOrSkip')
        activityExpectedStartDate = user.get('activityExpectedStartDate')
        activityCompletedDate = user.get('activityCompletedDate')
        activityRescheduledDate = user.get('activityRescheduledDate')

        if None in (id, profileId, farmId, needHelp, expenses, doneOrSkip, activityExpectedStartDate, activityCompletedDate, activityRescheduledDate):
            # Handle the error or skip the user as needed
            print(f"Skipping user with missing or incorrect data: {user}")
            continue

        try:
            activityExpectedStartDate = datetime.strptime(activityExpectedStartDate, '%d-%m-%Y %H:%M:%S %A')
            activityCompletedDate = datetime.strptime(activityCompletedDate, '%d-%m-%Y %H:%M:%S %A')
            activityRescheduledDate = datetime.strptime(activityRescheduledDate, '%d-%m-%Y %H:%M:%S %A')
        except ValueError as e:
            # Handle the error or skip the user as needed
            print(f"Skipping user due to date format error: {user}")
            continue

        flattened_data1.append((needHelp, expenses, doneOrSkip, activityExpectedStartDate, activityCompletedDate, activityRescheduledDate, profileId, farmId, id))

    return flattened_data1




def updateFarmDetails_fn(farmId,profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource):
    if profileId and farmId and farmName and farmType and soilType and farmStatus and farmSizeInAcre and farmElectricity and waterPHValue and farmWaterSource:

        response = updateFarmDetails_db(farmId,profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response






