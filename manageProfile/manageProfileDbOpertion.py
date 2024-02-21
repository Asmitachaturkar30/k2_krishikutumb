from django.db import connection
from datetime import datetime
from django.http import JsonResponse


# def registerData_db(profileid, firstname, lastname, mobilenumber, village, primaryfunction, secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state):
#     # try:
#         cursor = connection.cursor()

#         sql = """
#         INSERT INTO d_profilePriSecData
#         (profileid, firstname, lastname, mobilenumber, village, primaryfunction, secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """

#         cursor.execute(sql, (profileid, firstname, lastname, mobilenumber, village, primaryfunction,
#                        secondaryfunction, funtionunit, volume, minimumrequirement, tehsil, district, state))

#         connection.commit()

#         if cursor.rowcount > 0:
#             return True
#         else:
#             return False
    # except:
    #     response = {
    #         'message': 'An error occurred during database connection: '}
    #     return JsonResponse(response), 500


def createTertiaryProfile_db(prisecid, profileid, firstname, lastname, mobilenumber,
                             tertiaryfunction, fourthfunction, tertiaryfunctionvariety,
                             fourthfunctionvariety, functionUnit, volume, minimumrequirement,
                             village, tehsil, district, state):
    try:
        cursor = connection.cursor()

        sql = """INSERT INTO d_profileTertFourData (prisecid, profileid, firstname, lastname, mobilenumber, tertiaryfunction,
                fourthfunction, tertiaryfunctionvariety, fourthfunctionvariety, functionUnit, volume, minimumrequirement,
                village, tehsil, district, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (
            prisecid, profileid, firstname, lastname, mobilenumber, tertiaryfunction, fourthfunction,
            tertiaryfunctionvariety, fourthfunctionvariety, functionUnit, volume, minimumrequirement,
            village, tehsil, district, state
        ))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'TertiaryProfile is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'TertiaryProfile create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


def createProfile_db(firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude):
    try:
        cursor = connection.cursor()

        sql = """
        INSERT INTO d_userProfile
        ( firstname, lastname, mobilenumber, village, tehsil, district, state,latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Profile is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Profile create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


def deleteProfile_db(mobilenumber, primaryfunction, secondaryfunction):
    try:
        cursor = connection.cursor()

        sql = """ DELETE FROM d_profileprisecdata  WHERE mobilenumber= %s AND primaryfunction= %s AND secondaryfunction= %s"""

        cursor.execute(sql, (mobilenumber, primaryfunction, secondaryfunction))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Profile is Delete successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Profile Delete is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------

# def getUserData_db(mobileNumber):
#     try:
#         cursor = connection.cursor()

        # sql = """SELECT DISTINCT cast(t1.id as varchar) as id, t1.profileid, t1.priSecId, t1.firstname,
        #     t1.lastname, t1.mobilenumber, t1.village, t1.tehsil, t1.primaryfunction, t1.secondaryfunction,
        #     t1.district, t1.state, cast(t1.latitude as varchar) as latitude, 
        #         cast(t1.longitude as varchar) as longitude 
        #     FROM d_profileprisecdata t1 WHERE mobilenumber = %s;"""
        # cursor.execute(sql, (mobileNumber,))

#         response = cursor.fetchall()

#         cursor.close()
#         connection.close()

#         if response:
#             return response
#         else:
#             return None
#     except Exception as e:
#         # DB_ERROR = {"DB-ERROR":f"{str(e)}"}
#         # print(DB_ERROR)
#         # return DB_ERROR
#         return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

def getUserData_db(mobileNumber):
    try:
        cursor = connection.cursor()
        sql = """SELECT DISTINCT cast(t1.id as varchar) as id, t1.profileid, t1.priSecId, t1.firstname,
            t1.lastname, t1.mobilenumber, t1.village, t1.tehsil, t1.primaryfunction, t1.secondaryfunction,
            t1.district, t1.state, cast(t1.latitude as varchar) as latitude, 
                cast(t1.longitude as varchar) as longitude 
            FROM d_profileprisecdata t1 WHERE mobilenumber = %s;"""
        cursor.execute(sql, (mobileNumber,))
        response = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"success": True, "data": response} if response else {"success": False, "message": "No data found"}
    except Exception as e:
        return {"success": False, "message": f"Database error: {str(e)}"}
# -----------------------------------------------------------------------------------

def getProfileData_DB(mobileNumber):
    try:
        cursor = connection.cursor()

        sql = """SELECT DISTINCT cast(profileid as varchar) as profileid
                FROM d_userprofile WHERE mobilenumber = %s;"""

        cursor.execute(sql, (mobileNumber,))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        return {"success": True, "data": response} if response else {"success": False, "message": "No data found"}
    except Exception as e:
        return {"success": False, "message": f"Database error: {str(e)}"}
# -----------------------------------------------------------------------------------


def insertData(flattened_data):
    try:
        cursor = connection.cursor()

        query = """INSERT INTO d_profileprisecdata (profileid, priSecId, firstname, lastname, mobilenumber, village, state, primaryfunction,
                secondaryfunction, tehsil, district, latitude, longitude)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s);"""
        cursor.executemany(query, flattened_data)
        connection.commit()
        cursor.close()
        connection.close()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'MultipleProfile is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'MultipleProfile create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------------
def updateProfile_db(firstName, lastName, mobileNumber, village, tehsil, district, state, latitude, longitude):
    try:
        # Convert latitude and longitude to float
        latitude = float(latitude)
        longitude = float(longitude)

        cursor = connection.cursor()

        sql = """UPDATE d_userprofile
                SET firstname = %s,
                lastname = %s,
                village = %s,
                tehsil = %s,
                district = %s,
                state = %s,
                latitude = %s,
                longitude = %s
                WHERE 
                mobilenumber = %s; """

        cursor.execute(sql, (firstName, lastName, village, tehsil, district, state, latitude, longitude, mobileNumber))
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'User Profile is updated successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'User Profile updation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


# --------------------------------------------------------------------------------------   

def getTertiaryProfile_db(profileId):
    try:
        cursor = connection.cursor()
        sql = """
                SELECT DISTINCT
            prisecid ::TEXT,
            profileid::TEXT,
            firstname,
            lastname,
            mobilenumber,
            tertiaryfunction,
            fourthfunction,
            tertiaryfunctionvariety,
            fourthfunctionvariety,
            functionUnit,
            volume,
            minimumrequirement,
            village,
            tehsil,
            district,
            state
        FROM d_profiletertfourdata
        WHERE profileid = %s;
                        """
        cursor.execute(sql, (profileId,))
        response = cursor.fetchall()
        cursor.close()
        connection.close()
        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})