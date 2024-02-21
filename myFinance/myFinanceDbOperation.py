from django.db import connection
from datetime import datetime
from django.http import JsonResponse

# def createBudget_db(profileId, note, date, primaryFunction,secondaryFunction, amountType, amountTypeFunction, amount):
#     try:
#         cursor = connection.cursor()

#         sql = """
#         insert into d_budgetmanagement (profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)
#         values (%s, %s, %s, %s, %s, %s, %s, %s)"""
#         values = ( profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)
    
#         cursor.execute(sql, values)

#         connection.commit()

#         if cursor.rowcount > 0:
#             return JsonResponse({'result': 'success', 'message': 'Budget Management is create successfully.'})
#         else:
#             return JsonResponse({'result': 'failure', 'message': 'Budget Management create is failed.'})
#     except Exception as e:
#         return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
def createBudget_db(profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount):
    try:
        cursor = connection.cursor()

        sql = """
        INSERT INTO d_budgetmanagement (profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)
        VALUES (%s, %s, TO_TIMESTAMP(%s, 'DD-MM-YYYY HH24:MI:SS Day'), %s, %s, %s, %s, %s)
        """
        values = (profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)

        cursor.execute(sql, values)
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Budget Management is created successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Budget Management creation failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})


# ---------------------------------------------------------------------

def getBudgetDetials_db(profileId):
    try:
        cursor = connection.cursor()
        query = """SELECT DISTINCT CAST(Id AS varchar) AS transactionId, CAST(profileId AS varchar) AS profileId, note, to_char(date, 'DD-MM-YY HH:MI:SS D') as date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount
                    FROM d_budgetManagement
                    WHERE profileId = %s
                    ORDER BY profileId;"""

        cursor.execute(query,(profileId,))

        response = cursor.fetchall()
        cursor.close()
        connection.close()
        if response:
            return response
        else:
            return JsonResponse({'result': 'failure', 'message':'Get request is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# -------------------------------------------------------------------------------------- 
def updateBudget_db(transactionId, profileId, note, date, primaryFunction, secondaryFunction,
                    amountType, amountTypeFunction, amount):
    try:
        cursor = connection.cursor()

        sql = """
            UPDATE d_budgetManagement
            SET profileId = %s,
                note = %s,
                date = TO_TIMESTAMP(%s, 'DD-MM-YYYY HH24:MI:SS Day'),
                primaryFunction = %s,
                secondaryFunction = %s,
                amountType = %s,
                amountTypeFunction = %s,
                amount = %s
            WHERE id = %s;
        """

        cursor.execute(sql, (profileId, note, date, primaryFunction, secondaryFunction,
                            amountType, amountTypeFunction, amount, transactionId))
        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Budget Management is updated successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Budget Management updation is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})

# -------------------------------------------------------------------------------------- 


def deleteBudget_db(transactionId):
    try:
        cursor = connection.cursor()

        sql = """ DELETE FROM d_budgetManagement WHERE id = %s;"""

        cursor.execute(sql,(transactionId,))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Budget Management is DELETE successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Budget Management DELETE is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database operations: {str(e)}'})
