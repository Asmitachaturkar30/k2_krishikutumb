#!/usr/bin/python
from django.db import connection
from datetime import datetime
from django.http import JsonResponse

# --------------------------------------------------------------------------------

def createFarmDetails_db(profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource):
    try:
        cursor = connection.cursor()
    
        sql = """
        insert into d_registerfarms (profileid, farmname, farmtype, soiltype, farmstatus, farmsizeinacre, farmelectricity, waterphvalue, farmwatersource)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        
        cursor.execute(sql, (profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue, farmWaterSource))
    
        connection.commit()
    
        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success','message': 'Farm registered successfully.'})
        else:
            return JsonResponse({'result': 'failure','message': 'Farm is not registered.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------
def createFarmerCropScheduleMulitRow_db(flat_data):
    try:
        
        cursor = connection.cursor()
        
        sql = """insert into d_farmercropschedule (profileid, farmid, cropstatus, cropname, activitysequence, activityname, activitynamelocal, activityexpectedindays, needhelp, expenses, doneorskip, activityexpectedstartdate, activitycompleteddate, activityrescheduleddate) 
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
        cursor.executemany(sql, flat_data)
        connection.commit()
        cursor.close()
        connection.close()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success','message': 'Farmer Crop schedule is created successfully.'})
        else:
            return JsonResponse({'result': 'failure','message': 'Farmer Crop schedule creation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
        
# ----------------------------------------------------------------------------------------------------
# def deleteFarm_db(profileId,farmId):  
#     try:
#         cursor = connection.cursor()

#         sql = """delete from d_registerfarms
#                 where 
#                 profileid = %s
#                 and farmid = %s;"""

#         cursor.execute(sql, (profileId,farmId))
#         connection.commit()

#         if cursor.rowcount > 0:
#             return True
#         else:
#             return False
#     except:
#         return {'result': 'failure','message': 'An error occurred during database Operations:'}
def deleteFarm_db(profileId, farmId):
    try:
        cursor = connection.cursor()

        sql = """delete from d_registerfarms
                where 
                profileid = %s
                and farmid = %s; """

        cursor.execute(sql, (profileId, farmId))
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Registered Farm Deleted successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Registered Farm Not Deleted.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
  
# ------------------------------------------------------------------------------------------------------------------


def deleteFarmerCropSchedule_db(profileId,farmId, cropName):
    try:
        
        cursor = connection.cursor()

        sql = """delete from d_farmercropschedule
                where 
                profileid = %s
                and farmid = %s
                and cropname = %s; """

        cursor.execute(sql, (profileId,farmId, cropName))
        connection.commit()

        if cursor.rowcount > 0:
            return ({'result': 'success','message': 'Registered Farm Deleted successfully.'})
        else:
            return ({'result': 'failure','message': 'Registered Farm Not Deleted.'})
    except Exception as e:
        return ({'result': 'failure','message': f'An error occurred during database Operations: {str(e)}'})

# -------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def getCrops_db(state, district):
    try:
        
        cursor = connection.cursor()

        sql = "select distinct cast(id as varchar) as id, croptype,cropnameenglish,cropnamehindi,cropimagename from r_crops  where activeink2app= 'Yes' and state= %s order by id"

        cursor.execute(sql, (state,))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------

def getCropSchedule_db(state, district,cropName):
    try:
        
        cursor = connection.cursor()

        sql = """ select distinct cast(id as varchar) as id, cropname,activitysequence,activityname,activitynamelocal,activityexpectedindays from r_cropschedule 
		where activeink2app='Yes' and state= %s and cropname= %s  order by id asc"""

        cursor.execute(sql, (state, cropName))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------
def getFarmDetails_db(profileId):
    try:
        cursor = connection.cursor()

        sql = """SELECT
                DISTINCT farmid::text AS farmid,
                profileid,
                farmname,
                farmtype,
                soiltype,
                farmstatus,
                farmsizeinacre,
                farmelectricity,
                waterphvalue,
                farmwatersource,
                CASE 
                WHEN scheduledcropsname is null THEN 'No Crop'
                ELSE scheduledcropsname 
                END as scheduledcropsname
            FROM
                d_registerfarms
            WHERE
                profileid = %s;"""

        cursor.execute(sql, (profileId,))  # Pass profileId as a tuple

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------
def getFarmerCropSchedule_db(profileId, farmId,cropName):
    try:
        
        cursor = connection.cursor()

        sql = """SELECT DISTINCT
            id::text AS id,
            profileid ::text AS profileid,
            farmid ::text AS farmid,
            cropname,
            activitysequence,
            activityname,
            activitynamelocal,
            activityexpectedindays,
            needhelp,
            expenses,
            doneorskip,
            TO_CHAR(activityexpectedstartdate, 'DD-MM-YY HH24:MI:SS D') AS activityexpectedstartdate,
            TO_CHAR(activitycompleteddate, 'DD-MM-YY HH24:MI:SS D') AS activitycompleteddate,
            TO_CHAR(activityrescheduleddate, 'DD-MM-YY HH24:MI:SS D') AS activityrescheduleddate
            FROM
            d_farmercropschedule
            WHERE
            profileid = %s
            AND farmid = %s
            AND cropname = %s
            ORDER BY
            id ASC;
            """

        cursor.execute(sql, (profileId, farmId,cropName))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# -----------------------------------------------------------------------------------
# def updateFarmerCropSchedule_db(flattened_data1):
#     try:
#         cursor = connection.cursor()
#         query = """
#         update d_farmercropschedule 
#         set needhelp = %s,
#         expenses = %s,
#         doneorskip = %s,
#         activityexpectedstartdate = %s,
#         activitycompleteddate = %s,
#         activityrescheduleddate = %s
#         where profileid = %s
#         and farmid = %s
#         and id = %s;"""

#         cursor.executemany(query, flattened_data1)
#         connection.commit()

#         if cursor.rowcount > 0:
#             return JsonResponse({'result': 'success', 'message': 'Farmer Crop schedule is updated successfully.'})
#         else:
#             return JsonResponse({'result': 'failure', 'message': 'Farmer Crop schedule updation is failed.'})
#     except Exception as e:
#         return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------------

def updateFarmerCropSchedule_db(flattened_data1):
    try:
        cursor = connection.cursor()
        query = """
        update d_farmercropschedule 
        set needhelp = %s,
        expenses = %s,
        doneorskip = %s,
        activityexpectedstartdate = %s,
        activitycompleteddate = %s,
        activityrescheduleddate = %s
        where profileid = %s
        and farmid = %s
        and id = %s;"""

        # Print the formatted SQL query for debugging
        for data in flattened_data1:
            formatted_query = cursor.mogrify(query, data)
            print(formatted_query)

        cursor.executemany(query, flattened_data1)
        connection.commit()

        updated_rows = cursor.rowcount
        if updated_rows > 0:
            return JsonResponse({'result': 'success', 'message': f'Updated {updated_rows} records in Farmer Crop schedule successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'No records were updated.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})



def updateFarmDetails_db(farmId,profileId,farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource):
    try:
        cursor = connection.cursor()

        sql = """UPDATE d_registerfarms
            SET 
            farmName = %s,
            farmType = %s,
            soilType = %s,
            farmStatus = %s,
            farmSizeInAcre = %s,
            farmElectricity = %s,
            waterPHValue = %s,
            farmWaterSource = %s
            WHERE 
            farmId = %s AND profileid = %s; """

        cursor.execute(sql, (farmName,farmType,soilType,farmStatus,farmSizeInAcre,farmElectricity,waterPHValue,farmWaterSource,farmId,profileId))
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'User Profile is updated successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'User Profile updation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})











