from .myIotOperations import *
from django.http import JsonResponse


def createIOTdevice_fn(profileid, deviceregisterednumber, devicename, devicetype, devicevendor, devicetypeagriculture, devicestatus,
                    deviceconfig1paraname, deviceconfig1paravalue1, deviceconfig1paravalue2, deviceconfig1paravalue3,
                    deviceconfig2paraname, deviceconfig2paravalue1, deviceconfig2paravalue2, deviceconfig2paravalue3,
                    deviceconfig3paraname, deviceconfig3paravalue1, deviceconfig3paravalue2, deviceconfig3paravalue3,
                    deviceconfig4paraname, deviceconfig4paravalue1, deviceconfig4paravalue2, deviceconfig4paravalue3,
                    deviceconfig5paraname, deviceconfig5paravalue1, deviceconfig5paravalue2, deviceconfig5paravalue3):

    if (
        profileid and deviceregisterednumber and devicename and devicetype and devicevendor and
        devicetypeagriculture and devicestatus and deviceconfig1paraname and deviceconfig1paravalue1 and
        deviceconfig1paravalue2 and deviceconfig1paravalue3 and deviceconfig2paraname and deviceconfig2paravalue1 and
        deviceconfig2paravalue2 and deviceconfig2paravalue3 and deviceconfig3paraname and deviceconfig3paravalue1 and
        deviceconfig3paravalue2 and deviceconfig3paravalue3 and deviceconfig4paraname and deviceconfig4paravalue1 and
        deviceconfig4paravalue2 and deviceconfig4paravalue3 and deviceconfig5paraname and deviceconfig5paravalue1 and
        deviceconfig5paravalue2 and deviceconfig5paravalue3
    ):
        response = createIOTdevice_db(profileid, deviceregisterednumber, devicename, devicetype, devicevendor, devicetypeagriculture, devicestatus,
                                    deviceconfig1paraname, deviceconfig1paravalue1, deviceconfig1paravalue2, deviceconfig1paravalue3,
                                    deviceconfig2paraname, deviceconfig2paravalue1, deviceconfig2paravalue2, deviceconfig2paravalue3,
                                    deviceconfig3paraname, deviceconfig3paravalue1, deviceconfig3paravalue2, deviceconfig3paravalue3,
                                    deviceconfig4paraname, deviceconfig4paravalue1, deviceconfig4paravalue2, deviceconfig4paravalue3,
                                    deviceconfig5paraname, deviceconfig5paravalue1, deviceconfig5paravalue2, deviceconfig5paravalue3)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ------------------------------------------------------------------------------------------
def getMobileIOTDetails_fn(profileid):
    result = getMobileIOTDetails_db(profileid)

    if result:
        user_list = []

        for item in result:
            data = {
                "deviceid": item[0],
                "profileid": str(item[1]),
                "deviceregisterednumber": str(item[2]),
                "devicename": str(item[3]),
                "devicetype": str(item[4]),
                "devicevendor": str(item[5]),
                "devicetypeagriculture": str(item[6]),
                "devicestatus": str(item[7]),
                "deviceconfig1paraname": str(item[8]),
                "deviceconfig1paravalue1": str(item[9]),
                "deviceconfig1paravalue2": str(item[10]),
                "deviceconfig1paravalue3": str(item[11]),
                "deviceconfig2paraname": str(item[12]),
                "deviceconfig2paravalue1": str(item[13]),
                "deviceconfig2paravalue2": str(item[14]),
                "deviceconfig2paravalue3": str(item[15]),
                "deviceconfig3paraname": str(item[16]),
                "deviceconfig3paravalue1": str(item[17]),
                "deviceconfig3paravalue2": str(item[18]),
                "deviceconfig3paravalue3": str(item[19]),
                "deviceconfig4paraname": str(item[20]),
                "deviceconfig4paravalue1": str(item[21]),
                "deviceconfig4paravalue2": str(item[22]),
                "deviceconfig4paravalue3": str(item[23]),
                "deviceconfig5paraname": str(item[24]),
                "deviceconfig5paravalue1": str(item[25]),
                "deviceconfig5paravalue2": str(item[26]),
                "deviceconfig5paravalue3": str(item[27])
            }
            user_list.append(data)

        response = {
            "result": "success",
            "message": "success",
            "userList": user_list
        }

        return response
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response
# ------------------------------------------------------------------------------------------


def getMobileIOTWorkingHistory_fn(profileid, deviceid):
    result = getMobileIOTWorkingHistory_db(profileid, deviceid)

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
                "deviceid": item[1],
                "profileid": item[2],
                "deviceconfig1paraname": item[3],
                "deviceconfig1paravalue": item[4],
                "deviceconfig2paraname": item[5],
                "deviceconfig2paravalue": item[6],
                "deviceconfig3paraname": item[7],
                "deviceconfig3paravalue": item[8],
                "deviceconfig4paraname": item[9],
                "deviceconfig4paravalue": item[10],
                "deviceconfig5paraname": item[11],
                "deviceconfig5paravalue": item[12],
                "last_updated_at": item[13],
            }
            response["userList"].append(data)

        return response
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response
# ---------------------------------------------------------------------------------------


def createIOTworkingdata_fn(deviceid, profileid, deviceconfig1paraname, deviceconfig1paravalue, deviceconfig2paraname, deviceconfig2paravalue, deviceconfig3paraname, deviceconfig3paravalue, deviceconfig4paraname, deviceconfig4paravalue, deviceconfig5paraname, deviceconfig5paravalue):

    if (profileid and deviceid and
            deviceconfig1paraname and deviceconfig1paravalue and
            deviceconfig2paraname and deviceconfig2paravalue and
            deviceconfig3paraname and deviceconfig3paravalue and
            deviceconfig4paraname and deviceconfig4paravalue and
            deviceconfig5paraname and deviceconfig5paravalue
            ):

        response = createIOTworkingdata_db(deviceid, profileid, deviceconfig1paraname, deviceconfig1paravalue, deviceconfig2paraname, deviceconfig2paravalue,
                                         deviceconfig3paraname, deviceconfig3paravalue, deviceconfig4paraname, deviceconfig4paravalue, deviceconfig5paraname, deviceconfig5paravalue)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# -------------------------------------------------------------------------------

