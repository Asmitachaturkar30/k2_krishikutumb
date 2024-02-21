#!/usr/bin/python
from django.db import connection
from datetime import datetime
from django.http import JsonResponse

# ---------------------------------------------------------------------------------
def getPrimarySecondaryFunctions_db(state, district):
    try:

        cursor = connection.cursor()
    
        sql = '''
        select distinct cast(prisecid as varchar) as prisecid , primaryfunction, secondaryfunction, primaryfunctionimagename, secondaryfunctionimagename,
        canregister,candemandsecondaryfunction, isavailablesecondaryfunction, arefunctioninuse, primaryfunctionlocal, secondaryfunctionlocal, functionUnit, functionType
        from r_primarysecondaryfunctions
        where state = %s
        order by prisecid
        '''
    
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

def getLanguages_db(language, k2Type):
    with connection.cursor() as cursor:
        sql = '''
            SELECT
            English AS englishName,
            CASE 
                WHEN UPPER(%s) = 'HINDI' THEN Hindi
                WHEN UPPER(%s) = 'ENGLISH' THEN English
                WHEN UPPER(%s) = 'MARATHI' THEN Marathi
                WHEN UPPER(%s) = 'TELUGU' THEN Telugu
                WHEN UPPER(%s) = 'BANGLA' THEN Bangla
                WHEN UPPER(%s) = 'KANNADA' THEN Kannada
                WHEN UPPER(%s) = 'TAMIL' THEN Tamil
                WHEN UPPER(%s) = 'PUNJABI' THEN Punjabi
                WHEN UPPER(%s) = 'GUJARATI' THEN Gujarati
                WHEN UPPER(%s) = 'ODIA' THEN Odia
                WHEN UPPER(%s) = 'MALAYALAM' THEN Malayalam
                WHEN UPPER(%s) = 'HARYANVI' THEN Haryanvi
                WHEN UPPER(%s) = 'ASSAMESE' THEN Assamese
                ELSE English
            END AS localName
            FROM r_locallanguage
            WHERE k2type = %s;
        '''
        cursor.execute(sql, (language, language, language, language, language, language, language, language, language, language, language, language,language, k2Type))
        response = cursor.fetchall()

    if response:
        return response
    else:
        return None

# -------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def getk2support_db(state,district):
    try:

        cursor = connection.cursor()

        sql = """select distinct cast(id as varchar) as id , vediolink,vediotype,vediok2page,vediolinkhindi,vediolinklocal from r_k2support 
		            where activeink2app='Yes' and state= %s order by id asc;"""

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
def getStateDistrictList_db():
    try:

        cursor = connection.cursor()

        sql = """select distinct cast(id as varchar) as id, state,state_hindi,district,district_hindi,cast(latitude as varchar) as latitude,
        cast(longitude as varchar) as longitude from r_statedistrict where activeink2app= 'Yes' order by id asc;"""

        cursor.execute(sql)

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# ---------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def getVillageList_db(state, district):
    try:

        cursor = connection.cursor()

        sql = """select distinct cast(id as varchar) as id , tehsil,village,tehsil_hindi,village_hindi, 
                cast(latitude as varchar) as latitude,
                cast(longitude as varchar) as longitude
                from r_districttehsilvillage  where state= %s and district= %s order by id"""

        cursor.execute(sql, (state, district))

        response = cursor.fetchall()

        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
# ---------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
def getTertiaryFourthFunctions_db(priSecId):
    try:
        cursor = connection.cursor()

        sql = """select distinct cast(id as varchar) as id , cast(prisecid as varchar) as prisecid,tertiaryfunction,fourthfunction,
				tertiaryfunctionvariety,fourthfunctionvariety,
				tertiaryfunctionimagename,fourthfunctionimagename,
				tertiaryfunctionlocal,fourthfunctionlocal,
				tertiaryfunctionvarietylocal,fourthfunctionvarietylocal,
				candemandtertiaryfunction,isavailabletertiaryfunction,
				arefunctioninuse,functionUnit,description
		 		from r_tertiaryfourthfunctions 
				where prisecid= %s order by id;"""

        cursor.execute(sql, (priSecId,))
        response = cursor.fetchall()
        cursor.close()
        connection.close()
        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})
    

# --------------------------------------------------------------------------------------