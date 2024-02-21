from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .myFinanceFunction import *
# Create your views here.
@api_view(['POST'])
def myFinance_api(request):
    if request.method == 'POST':
        if request.data:
            data = request.data

            if 'operation' in data:
                operation = data['operation']

                if operation == 'createBudget':
                    if (
                        'user' in data and
                        'profileId' in data['user'] and
                        'note' in data['user'] and
                        'date' in data['user'] and
                        'primaryFunction' in data['user'] and
                        'secondaryFunction' in data['user'] and
                        'amountType' in data['user'] and
                        'amountTypeFunction' in data['user'] and
                        'amount' in data['user'] 
                    ):
                        user = data['user']
                        profileId = user['profileId']
                        note = user['note']
                        date = user['date']
                        primaryFunction = user['primaryFunction']
                        secondaryFunction = user['secondaryFunction']
                        amountType = user['amountType']
                        amountTypeFunction = user['amountTypeFunction']
                        amount = user['amount']

                        response = createBudget_fn(profileId, note, date, primaryFunction,
                                                    secondaryFunction, amountType, amountTypeFunction, amount)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# ---------------------------------------------------------------------------------------------                        

                elif operation == 'getBudgetDetials':
                        if ('profileId' in data):
                            profileId = data['profileId']
                            response = getBudgetDetials_fn(profileId)
                            return JsonResponse(response)
                        else:
                            return getMsgParamNotEmpty()
# ---------------------------------------------------------------------------------------------     
                elif operation == 'updateBudget':
                    if ('user' in data and
                        'transactionId' in data['user'] and
                        'profileId' in data['user'] and
                        'note' in data['user'] and
                        'date' in data['user'] and
                        'primaryFunction' in data['user'] and
                        'secondaryFunction' in data['user'] and
                        'amountType' in data['user'] and
                        'amountTypeFunction' in data['user'] and
                        'amount' in data['user']
                        ):
                        user = data['user']
                        transactionId = user['transactionId']
                        profileId = user['profileId']
                        note = user['note']
                        date = user['date']
                        primaryFunction = user['primaryFunction']
                        secondaryFunction = user['secondaryFunction']
                        amountType = user['amountType']
                        amountTypeFunction = user['amountTypeFunction']
                        amount = user['amount']

                        response = updateBudget_fn(transactionId, profileId, note, date, primaryFunction, secondaryFunction,
                            amountType, amountTypeFunction, amount)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
# ---------------------------------------------------------------------------------------------
                elif operation == 'deleteBudget':
                    if (
                    'user' in data and
                    'transactionId' in data['user']
                    ):
                        user = data['user']
                        transactionId = user['transactionId']

                        response = deleteBudget_fn(transactionId)
                        return response
                    else:
                        return JsonResponse({'result': 'failure','message': 'Missing parameter'})
                else:
                        return getMsgParamNotEmpty()
            else:
                return JsonResponse({'message': 'Missing operation parameter'})
        else:
            return JsonResponse({'message': 'Missing request data'})
    
    return JsonResponse({'message': 'Success'})

