#!/usr/bin/python
from django.db import connection
from datetime import datetime
from django.http import JsonResponse


def createGroup_db(groupName, groupOwnerFirstName, groupOwnerLastName, groupOwnerMobile,groupType, groupActivity, groupStatus, groupNote, village, district, state, tehsil, policyId):
    try:
        cursor = connection.cursor()

        sql = """insert into d_group (groupname, groupownerfirstname, groupownerlastname, groupownermobile,grouptype, groupactivity, groupstatus, groupnote, village, district, state, tehsil, policyId)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (groupName, groupOwnerFirstName, groupOwnerLastName, groupOwnerMobile,groupType, groupActivity, groupStatus, groupNote, village, district, state, tehsil, policyId)
    
        cursor.execute(sql, values)

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Group is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Group create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# ---------------------------------------------------------------------
def createMember_db(memberProfileId, memberFirstName, memberLastName, memberMobile, groupName, groupId, memberStatus, village, tehsil, district, state):
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO d_member (memberprofileid, memberfirstname, memberlastname, membermobile, groupname, groupid, memberstatus, village, tehsil, district, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (memberProfileId, memberFirstName, memberLastName, memberMobile, groupName, groupId, memberStatus, village, tehsil, district, state)
 
        cursor.execute(sql, values)

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Member is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Member create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


# ------------------------------------------------------------------------
    
def getGroup_db(state,district,memberProfileId):
    try:
        cursor = connection.cursor()

        query = """
            select distinct cast(t1.groupid as varchar) as groupid, 'myGroup' as allgroup, t1.groupname, t1.groupownerfirstname, t1.groupownerlastname, t1.groupownermobile, t1.grouptype, t1.groupactivity, t1.groupstatus, t1.groupnote, t1.village, t1.tehsil, t1.district, t1.state 
            from d_group t1
            where t1.state = 'Madhya Pradesh'
            and exists (
                select 1
                from d_member d1
                where d1.memberprofileid = '1'
                and cast(d1.groupid as varchar) = cast(t1.groupid as varchar)
            )
            Union all
                    select distinct cast(t1.groupid as varchar) as groupid, 'allGroup' as allgroup, t1.groupname, t1.groupownerfirstname, t1.groupownerlastname, t1.groupownermobile, t1.grouptype, t1.groupactivity, t1.groupstatus, t1.groupnote, t1.village, t1.tehsil, t1.district, t1.state 
            from d_group t1
            where t1.state = 'Madhya Pradesh'
            and not exists (
                select 1
                from d_member d1
                where d1.memberprofileid = '1'
                and cast(d1.groupid as varchar) = cast(t1.groupid as varchar))
            order by 2;
            """
        cursor.execute(query, (state,memberProfileId))

        response = cursor.fetchall()
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


# ---------------------------------------------------------------
def getGroupByPolicy_db(policyId):
    try:
        cursor = connection.cursor()
        query = """
            select distinct cast(t1.groupid as varchar) as groupid, 'allgroup' as allgroup, t1.groupname, t1.groupownerfirstname, t1.groupownerlastname, t1.groupownermobile, t1.grouptype, t1.groupactivity, t1.groupstatus, t1.groupnote, t1.village, t1.tehsil, t1.district, t1.state 
            from d_group t1
            where t1.policyId = %s
            order by 2;
            """
        cursor.execute(query, (policyId,))

        response = cursor.fetchall()
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

#-------------------------------------------
def getMember_db(groupId):
    try:
        cursor = connection.cursor()

        query = """select distinct cast(memberid as varchar) as memberid,memberprofileid,memberfirstname,memberlastname,membermobile,groupname,groupid,memberstatus,village,tehsil,district,state 
                from d_member
                where groupid = %s order by memberid; """

        cursor.execute(query,(groupId,))

        response = cursor.fetchall()
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# ---------------------------------------------------------------

   
def getPolicy_db(policyType,state,district):

    try:
        cursor = connection.cursor()

        query = """select distinct cast(policyid as varchar) as policyid ,policyname,policytype,policyactivity,policystatus,nationalpolicy,statepolicy,districtpolicy,district,state 
                    from r_policy
                    where policytype = %s and state = %s order by policyid; """

        cursor.execute(query,(policyType,state))

        response = cursor.fetchall()
        cursor.close()
        connection.close()

        if response:
            return response
        else:
            return None
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})


# -------------------------------------------------------------------------------

  
def getDocument_db(policyId):

    try: 
        cursor = connection.cursor()

        query = """select distinct cast(documentid as varchar) as documentid,documentname, documenttype, documentstatus, documentcriteria, documentdetails, policyid, policyname
        from r_policydocuments
        where policyid = %s order by policyid; """

        cursor.execute(query, (policyId,))

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
# def createBudget_db(profileId, note, date, primaryFunction,secondaryFunction, amountType, amountTypeFunction, amount):

#     cursor = connection.cursor()

#     sql = """
#     insert into d_budgetmanagement (profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)
#     values (%s, %s, %s, %s, %s, %s, %s, %s)"""
#     values = ( profileId, note, date, primaryFunction, secondaryFunction, amountType, amountTypeFunction, amount)
 
#     cursor.execute(sql, values)

#     connection.commit()

#     if cursor.rowcount > 0:
#         return True
#     else:
#         return False
# # ---------------------------------------------------------------------
def deleteGroup_db(groupId):
    try: 
        cursor = connection.cursor()

        sql = """ DELETE FROM d_group WHERE groupId = %s;"""

        cursor.execute(sql,(groupId,))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Group is DELETE successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Group DELETE is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# # ---------------------------------------------------------------------

def deleteMember_db(memberId,groupId):
    try:
        cursor = connection.cursor()

        sql = """ DELETE FROM d_member WHERE memberId=%s and groupId = %s;"""

        cursor.execute(sql,(memberId,groupId))

        connection.commit()

        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'Member is DELETE successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'Member DELETE is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# # ---------------------------------------------------------------------

# -----------------------------------------------------------------------------------
def getGroupActivities_db(groupId):
    try:
        cursor = connection.cursor()

        sql = """SELECT DISTINCT
            f1.id::text AS id,
            f1.profileid ::text AS profileid,
            f1.farmid ::text AS farmid,
            f1.cropname,
            f1.activitysequence,
            f1.activityname,
            f1.activitynamelocal,
            f1.activityexpectedindays,
            f1.needhelp,
            f1.expenses,
            f1.doneorskip,
            TO_CHAR(f1.activityexpectedstartdate, 'DD-MM-YY HH24:MI:SS D') AS activityexpectedstartdate,
            TO_CHAR(f1.activitycompleteddate, 'DD-MM-YY HH24:MI:SS D') AS activitycompleteddate,
            TO_CHAR(f1.activityrescheduleddate, 'DD-MM-YY HH24:MI:SS D') AS activityrescheduleddate
            FROM
            d_farmercropschedule f1, d_group g1, d_member m1
            WHERE
            f1.profileid = m1.memberprofileid
			and  cast(g1.groupid as varchar)  = cast(m1.groupid as varchar)
			and f1.activityexpectedstartdate 
			BETWEEN CURRENT_TIMESTAMP - INTERVAL '5 day' AND CURRENT_TIMESTAMP + INTERVAL '12 day'
			and g1.groupid=%s
            ORDER BY
            id ASC;
            """

        cursor.execute(sql, (groupId,))

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

def getGroupDemandAvailability_db(groupId):
    try:

        cursor = connection.cursor()

        sql = """SELECT DISTINCT CAST(p1.profileid AS varchar) AS profileId ,p1.firstname,p1.lastname,p1.primaryfunction,p1.secondaryFunction,p1.mobilenumber,p1.village,
					   '1' AS priority,d1.demandtype AS demandtype
					FROM d_profileprisecdata p1 , d_demand d1, d_group g1, d_member m1
					WHERE d1.mobilenumber = p1.mobilenumber
					and p1.profileid = m1.memberprofileid
					and  cast(g1.groupid as varchar)  = cast(m1.groupid as varchar)
					and g1.groupid=%s
					and p1.primaryfunction in ('Worker','Machine','Market','Wholesale')
					AND d1.isdemandexpired IS NULL
			UNION ALL
				SELECT DISTINCT CAST(p1.profileid AS varchar) AS profileId ,p1.firstname,p1.lastname,p1.primaryfunction,p1.secondaryFunction,p1.mobilenumber,p1.village,
						'2' AS priority,'Available' AS demandtype
					FROM d_profileprisecdata p1, d_group g1, d_member m1
					WHERE p1.profileid = m1.memberprofileid
					and  cast(g1.groupid as varchar)  = cast(m1.groupid as varchar)
					and p1.primaryfunction in ('Worker','Machine','Market','Wholesale')
					and g1.groupid=%s
                ORDER BY priority;"""

        cursor.execute(sql, (groupId,groupId))

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



def createUserPolicyDocument_db(groupOwnerMobileNumber, documentId, documentName, documentType,documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate):
    try:
        cursor = connection.cursor()

        sql = """
        insert into d_userPolicyDocuments (groupOwnerMobileNumber, documentId, documentName, documentType,documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (groupOwnerMobileNumber, documentId, documentName, documentType,documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate)
    
        cursor.execute(sql, values)

        connection.commit()
    
        if cursor.rowcount > 0:
            return JsonResponse({'result': 'success', 'message': 'UserPolicyDocument is create successfully.'})
        else:
            return JsonResponse({'result': 'failure', 'message': 'UserPolicyDocument create is failed.'})
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

# -----------------------------------------------------------------------------------
def getUserPolicyDocument_db(groupOwnerMobileNumber, PolicyId):
    try:
        cursor = connection.cursor()

        query = """select distinct cast(groupOwnerMobileNumber as varchar) as groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails,
                cast(PolicyId as char) as PolicyId,
                policyName, last_update_date, DueDate
                from d_userPolicyDocuments
                where groupOwnerMobileNumber = %s and PolicyId = %s; """

        cursor.execute(query, (groupOwnerMobileNumber, PolicyId))

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
def UpdateUserPolicyDocument_db(groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate):
    try:
        cursor = connection.cursor()

        query = """UPDATE d_userPolicyDocuments
                    SET groupOwnerMobileNumber = %s,
                        documentId = %s,
                        documentName = %s,
                        documentType = %s,
                        documentStatus = %s,
                        documentCriteria = %s,
                        documentDetails = %s,
                        policyId = %s,
                        policyName = %s,
                        last_update_date = %s,
                        DueDate = %s
                    WHERE groupOwnerMobileNumber = %s and PolicyId = %s;
                """

        cursor.execute(query, (groupOwnerMobileNumber, documentId, documentName, documentType, documentStatus, documentCriteria, documentDetails, policyId, policyName, last_update_date, DueDate, groupOwnerMobileNumber, policyId))
        connection.commit()

        if cursor.rowcount > 0:
            return {'result': 'success', 'message': 'UserPolicyDocument is updated successfully.'}
        else:
            return {'result': 'failure', 'message': 'UserPolicyDocument updation is failed.'}
    except Exception as e:
        return JsonResponse({'result': 'failure', 'message': f'An error occurred during database Operations: {str(e)}'})

