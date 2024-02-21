# from k2appPolicy.phase2operation import *
from .manageProfileDbOpertion import *
from django.http import JsonResponse


# def registerUser_fn(profileid, firstname, lastname, mobilenumber, village, primaryfunction, secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state):

#     if (
#         profileid and firstname and lastname and mobilenumber and village and primaryfunction and secondaryfunction and funtionunit and volume and minimumrequirement and tehsil and district and state
#     ):
#         result = registerData_db(profileid, firstname, lastname, mobilenumber, village, primaryfunction,
#                                  secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state)
#         if result:
#             response = {
#                 "result": "success",
#                 "message": "User Registered Successfully !"
#             }
#             return response
#         else:
#             response = {
#                 "result": "failure",
#                 "message": "Registration Failure"
#             }
#             return response
#     else:
#         response = {
#             "result": "failure",
#             "message": "User Parameters should not be empty !"
#         }
#         return response
# ---------------------------------------------------------------------------------------------------------


def createTertiaryProfile_fn(prisecid, profileid, firstname, lastname, mobilenumber,
                             tertiaryfunction, fourthfunction, tertiaryfunctionvariety,
                             fourthfunctionvariety, functionUnit, volume, minimumrequirement,
                             village, tehsil, district, state):
    if (
        prisecid and
        profileid and
        firstname and
        lastname and
        mobilenumber and
        tertiaryfunction and
        fourthfunction and
        tertiaryfunctionvariety and
        fourthfunctionvariety and
        functionUnit and
        volume and
        minimumrequirement and
        village and
        tehsil and
        district and
        state
    ):

        response = createTertiaryProfile_db(
            prisecid, profileid, firstname, lastname, mobilenumber,
            tertiaryfunction, fourthfunction, tertiaryfunctionvariety,
            fourthfunctionvariety, functionUnit, volume, minimumrequirement,
            village, tehsil, district, state
        )

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# -------------------------------------------------------------------------------------------------


def createProfile_fn( firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude):

    if (
        firstName and lastName and mobileNumber and village and tehsil and district and state and latitude and longitude
    ):
        response = createProfile_db(
             firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude)
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# -----------------------------------


def deleteProfile_fn(mobilenumber, primaryfunction, secondaryfunction):
    response = deleteProfile_db(
        mobilenumber, primaryfunction, secondaryfunction)

    if response:
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# ________----------------------------------------------------------

# def getUserData_fn(mobileNumber):
#         result = getUserData_db(mobileNumber)

#         if result is not None:

#             response = {
#                 "result": "success",
#                 "message": "success",
#                 "userList": []
#             }

#             for item in result:
                
#                 data = {
#                     "id": item[0],
#                     "profileId": item[1],
#                     "priSecId": item[2],
#                     "firstName": item[3],
#                     "lastName": item[4],
#                     "mobileNumber": item[5],
#                     "village": item[6],
#                     "tehsil": item[7],
#                     "primaryFunction": item[8],
#                     "secondaryFunction": item[9],
#                     "district": item[10],
#                     "state": item[11],
#                     "latitude": item[12],
#                     "longitude": item[13]
#                 }
#                 response["userList"].append(data)

#             return response

#         elif result is None:
#             Jresponse = {
#                 "result": "failure",
#                 "message": "No data found for the provided mobile number"
#             }
#             return Jresponse
#         return response
def getUserData_fn(mobileNumber):
    db_response = getUserData_db(mobileNumber)
    
    if db_response.get("success"):
        response = {
            "result": "success",
            "message": "success",
            "userList": [
                {   
                    "id": item[0],
                    "profileId": item[1],
                    "priSecId": item[2],
                    "firstName": item[3],
                    "lastName": item[4],
                    "mobileNumber": item[5],
                    "village": item[6],
                    "tehsil": item[7],
                    "primaryFunction": item[8],
                    "secondaryFunction": item[9],
                    "district": item[10],
                    "state": item[11],
                    "latitude": item[12],
                    "longitude": item[13]
                } for item in db_response["data"]
            ]
        }
        return response
    else:
        # This is where you handle the error
        return {
            "result": "failure",
            "message": db_response.get("message", "An unknown error occurred")
        }
# ------------------------------------------------------------------------------------------

def getProfile_fn(mobileNumber):
    result = getProfileData_DB(mobileNumber)
    
    
    if result.get("success"):
        response = {
            "result": "success",
            "message": "success",
            "userList": [{"profileId": item[0]}for item in result["data"]]
        }

        return response
    else:
        # This is where you handle the error
        return {
            "result": "failure",
            "message": result.get("message", "An unknown error occurred")
        }

# ------------------------------------------------------------------------------------------


def flatten_json_tree(user_data, parent_profileId=None):
    flattened_data = []

    if isinstance(user_data, list):
        # If the user_data is a list, call the function recursively for each item in the list
        for item in user_data:
            child_data = flatten_json_tree(item, parent_profileId)
            flattened_data.extend(child_data)
    elif isinstance(user_data, dict):
        # Get the user data from the current level of the tree
        profileid = user_data.get('profileId')
        priSecId = user_data.get('priSecId')
        firstname = user_data.get('firstName')
        lastname = user_data.get('lastName')
        mobilenumber = user_data.get('mobileNumber')
        village = user_data.get('village')
        state = user_data.get('state')
        primaryfunction = user_data.get('primaryFunction')
        secondaryfunction = user_data.get('secondaryFunction')
        tehsil = user_data.get('tehsil')
        district = user_data.get('district')
        latitude = user_data.get('latitude')
        longitude = user_data.get('longitude')

        

        if None in (profileid, firstname, lastname, mobilenumber, village, state, primaryfunction, secondaryfunction, tehsil, district, latitude, longitude):
            # Invalid data in the current node, handle accordingly (e.g., log error, skip, etc.)
            return []

        # Append the current user data to the flattened_data list
        flattened_data.append((profileid, priSecId, firstname, lastname, mobilenumber,
                              village, state, primaryfunction, secondaryfunction, tehsil, district, latitude, longitude))
        # Check if the current user data has children
        if 'children' in user_data:
            children = user_data['children']
            for child_user_data in children:
                # Call the function recursively for each child user data with the parent_profileId set to the current user's profileId
                child_data = flatten_json_tree(child_user_data, profileid)
                flattened_data.extend(child_data)

    return flattened_data


# ------------------------------------------------------------------------------------------

def updateProfile_fn(firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude):
    if firstName and lastName and mobileNumber and village and tehsil and district and state and latitude and longitude:

        response = updateProfile_db(
            firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response

# ---------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------


def getTertiaryProfile_fn(profileId):
    result = getTertiaryProfile_db(profileId)

    response = {}  # Create an empty response dictionary

    if result is not None:
        user_list = [] 
        for item in result:
            data = {
                'priSecId': str(item[0]),
                'profileId': str(item[1]),
                'firstName': str(item[2]),
                'lastName': str(item[3]),
                'mobileNumber': str(item[4]),
                'tertiaryFunction': str(item[5]),
                'fourthFunction': str(item[6]),
                'tertiaryFunctionVariety': str(item[7]),
                'fourthFunctionVariety': str(item[8]),
                'functionUnit': str(item[9]),
                'volume': str(item[10]),
                'minimumRequirement': str(item[11]),
                'village': str(item[12]),
                'tehsil': str(item[13]),
                'district': str(item[14]),
                'state': str(item[15])
            }
            user_list.append(data)  # Append the data to the user_list

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list  # Set the user list in the response
        }
    elif result is None:
        Jresponse = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return Jresponse
    else:
        response = {
            "result": "failure",
            "message": "Get Request Failure"
        }

    return response