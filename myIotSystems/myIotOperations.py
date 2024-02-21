from django.db import connection
from datetime import datetime
from django.http import JsonResponse

def createIOTdevice_db(profileid, deviceregisterednumber, devicename, devicetype, devicevendor,devicetypeagriculture, devicestatus,
                       deviceconfig1paraname, deviceconfig1paravalue1,deviceconfig1paravalue2, deviceconfig1paravalue3, 
                       deviceconfig2paraname, deviceconfig2paravalue1,deviceconfig2paravalue2, deviceconfig2paravalue3, 
                       deviceconfig3paraname, deviceconfig3paravalue1,deviceconfig3paravalue2, deviceconfig3paravalue3,
                       deviceconfig4paraname, deviceconfig4paravalue1,deviceconfig4paravalue2, deviceconfig4paravalue3, 
                       deviceconfig5paraname,deviceconfig5paravalue1,deviceconfig5paravalue2, deviceconfig5paravalue3):
    try:
        cursor = connection.cursor()
    
        sql = """INSERT INTO d_registermobileiot (
                            profileid, deviceregisterednumber, devicename, devicetype, devicevendor,devicetypeagriculture, devicestatus,
                           deviceconfig1paraname, deviceconfig1paravalue1,deviceconfig1paravalue2, deviceconfig1paravalue3, 
                           deviceconfig2paraname, deviceconfig2paravalue1,deviceconfig2paravalue2, deviceconfig2paravalue3, 
                           deviceconfig3paraname, deviceconfig3paravalue1,deviceconfig3paravalue2, deviceconfig3paravalue3,
                           deviceconfig4paraname, deviceconfig4paravalue1,deviceconfig4paravalue2, deviceconfig4paravalue3, 
                           deviceconfig5paraname,deviceconfig5paravalue1,deviceconfig5paravalue2, deviceconfig5paravalue3)
        values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
     
        cursor.execute(sql, ( profileid, deviceregisterednumber, devicename, devicetype, devicevendor,devicetypeagriculture, devicestatus,
                           deviceconfig1paraname, deviceconfig1paravalue1,deviceconfig1paravalue2, deviceconfig1paravalue3, 
                           deviceconfig2paraname, deviceconfig2paravalue1,deviceconfig2paravalue2, deviceconfig2paravalue3, 
                           deviceconfig3paraname, deviceconfig3paravalue1,deviceconfig3paravalue2, deviceconfig3paravalue3,
                           deviceconfig4paraname, deviceconfig4paravalue1,deviceconfig4paravalue2, deviceconfig4paravalue3, 
                           deviceconfig5paraname,deviceconfig5paravalue1,deviceconfig5paravalue2, deviceconfig5paravalue3
                         ))
    
        connection.commit()
    
        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success','message': 'Device Registered Successfully!'})
        else:
            return JsonResponse({'result': 'failure','message': 'Device Registeration is failed!.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -----------------------------------------------------------------------------------

def getMobileIOTDetails_db(profileid):
    try:
        cursor = connection.cursor()

        # sql = """SELECT DISTINCT cast(deviceid as char) as deviceid , cast(profileid as char) as profileid,
        #             	cast(deviceregisterednumber as char) deviceregisterednumber,devicename,devicetype,devicevendor,devicetypeagriculture,devicestatus,
        #             	deviceconfig1paraname,deviceconfig1paravalue1,deviceconfig1paravalue2,deviceconfig1paravalue3,
        #             	deviceconfig2paraname,deviceconfig2paravalue1,deviceconfig2paravalue2,deviceconfig2paravalue3,
        #             	deviceconfig3paraname,deviceconfig3paravalue1,deviceconfig3paravalue2,deviceconfig3paravalue3,
        #             	deviceconfig4paraname,deviceconfig4paravalue1,deviceconfig4paravalue2,deviceconfig4paravalue3,
        #             	deviceconfig5paraname,deviceconfig5paravalue1,deviceconfig5paravalue2,deviceconfig5paravalue3
        #             FROM d_registermobileiot
        #              WHERE profileid = %s order by deviceid;"""
        sql="""SELECT DISTINCT
    CAST(deviceid AS VARCHAR) AS deviceid,
    CAST(profileid AS VARCHAR) AS profileid,
    CAST(deviceregisterednumber AS VARCHAR) AS deviceregisterednumber,
    CAST(devicename AS VARCHAR) AS devicename,
    CAST(devicetype AS VARCHAR) AS devicetype,
    CAST(devicevendor AS VARCHAR) AS devicevendor,
    CAST(devicetypeagriculture AS VARCHAR) AS devicetypeagriculture,
    CAST(devicestatus AS VARCHAR) AS devicestatus,
    CAST(deviceconfig1paraname AS VARCHAR) AS deviceconfig1paraname,
    CAST(deviceconfig1paravalue1 AS VARCHAR) AS deviceconfig1paravalue1,
    CAST(deviceconfig1paravalue2 AS VARCHAR) AS deviceconfig1paravalue2,
    CAST(deviceconfig1paravalue3 AS VARCHAR) AS deviceconfig1paravalue3,
    CAST(deviceconfig2paraname AS VARCHAR) AS deviceconfig2paraname,
    CAST(deviceconfig2paravalue1 AS VARCHAR) AS deviceconfig2paravalue1,
    CAST(deviceconfig2paravalue2 AS VARCHAR) AS deviceconfig2paravalue2,
    CAST(deviceconfig2paravalue3 AS VARCHAR) AS deviceconfig2paravalue3,
    CAST(deviceconfig3paraname AS VARCHAR) AS deviceconfig3paraname,
    CAST(deviceconfig3paravalue1 AS VARCHAR) AS deviceconfig3paravalue1,
    CAST(deviceconfig3paravalue2 AS VARCHAR) AS deviceconfig3paravalue2,
    CAST(deviceconfig3paravalue3 AS VARCHAR) AS deviceconfig3paravalue3,
    CAST(deviceconfig4paraname AS VARCHAR) AS deviceconfig4paraname,
    CAST(deviceconfig4paravalue1 AS VARCHAR) AS deviceconfig4paravalue1,
    CAST(deviceconfig4paravalue2 AS VARCHAR) AS deviceconfig4paravalue2,
    CAST(deviceconfig4paravalue3 AS VARCHAR) AS deviceconfig4paravalue3,
    CAST(deviceconfig5paraname AS VARCHAR) AS deviceconfig5paraname,
    CAST(deviceconfig5paravalue1 AS VARCHAR) AS deviceconfig5paravalue1,
    CAST(deviceconfig5paravalue2 AS VARCHAR) AS deviceconfig5paravalue2,
    CAST(deviceconfig5paravalue3 AS VARCHAR) AS deviceconfig5paravalue3
FROM d_registermobileiot
WHERE profileid = %s
ORDER BY deviceid;"""


        cursor.execute(sql, (profileid,))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return JsonResponse({'result': 'failure', 'message':'Get request is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})  
# -----------------------------------------------------------------------------------


def getMobileIOTWorkingHistory_db(profileid,deviceid):
    try:
        cursor = connection.cursor()

        sql = """SELECT DISTINCT cast(id as varchar) as id, cast(deviceid as char) as deviceid , cast(profileid as char) as profileid,
                    	deviceconfig1paraname,deviceconfig1paravalue,deviceconfig2paraname,deviceconfig2paravalue,
                    	deviceconfig3paraname,deviceconfig3paravalue,deviceconfig4paraname,deviceconfig4paravalue,
                    	deviceconfig5paraname,deviceconfig5paravalue,last_updated_at
                    FROM d_iotdeviceworkingdata 
                     WHERE profileid = %s and deviceid= %s order by id desc """

        cursor.execute(sql, (profileid,deviceid))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return JsonResponse({'result': 'failure', 'message':'Get request is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# -------------------------------------------------------------------------------------------------
import traceback  # Import the traceback module

def createIOTworkingdata_db(deviceid, profileid, deviceconfig1paraname, deviceconfig1paravalue, deviceconfig2paraname, deviceconfig2paravalue, deviceconfig3paraname, deviceconfig3paravalue, deviceconfig4paraname, deviceconfig4paravalue, deviceconfig5paraname, deviceconfig5paravalue):
    try:
        cursor = connection.cursor()

        sql = """INSERT INTO d_iotdeviceworkingdata (deviceid, profileid, deviceconfig1paraname, deviceconfig1paravalue, deviceconfig2paraname, deviceconfig2paravalue, deviceconfig3paraname, deviceconfig3paravalue, deviceconfig4paraname, deviceconfig4paravalue, deviceconfig5paraname, deviceconfig5paravalue)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (deviceid, profileid, deviceconfig1paraname, deviceconfig1paravalue, deviceconfig2paraname, deviceconfig2paravalue, deviceconfig3paraname, deviceconfig3paravalue, deviceconfig4paraname, deviceconfig4paravalue, deviceconfig5paraname, deviceconfig5paravalue))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Device Live Data is created successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Device Live Data creation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

#------------------------------------------------------------------------------