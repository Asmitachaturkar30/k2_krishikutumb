from django.http import JsonResponse
from .myFinanceDbOperation import *

def getMsgParamNotEmpty():
    return JsonResponse({'result': 'failure','message': 'JSON Invalid Parameters.'})


def createBudget_fn(profileId, note, date, primaryFunction,
                    secondaryFunction, amountType, amountTypeFunction, amount):
    if (profileId and note and date and primaryFunction and
                    secondaryFunction and amountType and amountTypeFunction and amount):
        response = createBudget_db(profileId, note, date, primaryFunction,secondaryFunction, amountType, amountTypeFunction, amount)

        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response


def getBudgetDetials_fn(profileId):
    result = getBudgetDetials_db(profileId)

    data = []
    if result:
        response = {
                "result": "success",
                "message": "success",
                "userList": []
        }

        for item in result:
            data = {
                "transactionId": item[0],
                "profileId": item[1],
                "note": item[2],
                "date": item[3],
                "primaryFunction": item[4],
                "secondaryFunction": item[5],
                "amountType": item[6],
                "amountTypeFunction": item[7],
                "amount": item[8]
            }
            response["userList"].append(data)

        return response
    else:
        response = JsonResponse({
            "result": "error",
            "message": "No data found"
        })
        return response
    
# ---------------------------------------------------------------------------------------------
def updateBudget_fn(transactionId, profileId, note, date, primaryFunction, secondaryFunction,
                    amountType, amountTypeFunction, amount):
    if transactionId and profileId and note and date and primaryFunction and secondaryFunction and amountType and amountTypeFunction and amount:
        response = updateBudget_db(transactionId, profileId, note, date, primaryFunction, secondaryFunction,
                    amountType, amountTypeFunction, amount)
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
# ---------------------------------------------------------------------------------------------


def deleteBudget_fn(transactionId):
    if transactionId:
        response = deleteBudget_db(transactionId)
        return response
    else:
        response = JsonResponse({
            "result": "failure",
            "message": "User Parameters should not be Null !"
        })
        return response
