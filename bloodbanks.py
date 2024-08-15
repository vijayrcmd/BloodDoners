from flask import *
from database import *

blood=Blueprint('blood',__name__)

@blood.route('/blood_home')
def  blood_home():
    return render_template('blood_home.html')

@blood.route('/bl_manage_donation_col',methods=['post','get'])
def bl_manage_donation():
    data={}
    qry="select * from donors"
    qry2="select * from bloodgroups"
    qry3="SELECT * FROM `collection` INNER JOIN `bloodbanks` USING(bank_id) INNER JOIN `bloodgroups` USING(group_id) INNER JOIN donors USING(user_id) where bank_id='%s'"%(session['blood'])
    data['coll']=select(qry3)
    data['group']=select(qry2)
    data['don']=select(qry)
    if 'submit' in request.form:
        group=request.form['group']
        unit=request.form['unit']
        user=request.form['user']
        qry="insert into  collection values(null,'%s','%s',curdate(),'%s','%s')" %(session['blood'],group,unit,user)
        insert(qry)
        return '''<script>alert("Added... ");window.location="/bl_manage_donation_col"</script>'''
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry4="delete from  collection where collection_id='%s'" % (id)
        delete(qry4)
        return redirect(url_for('blood.bl_manage_donation'))
        
    if action=='update':
        qry5="select * from  collection where collection_id='%s'" % (id)
        data['up']=select(qry5)
    if 'update' in request.form:
        group=request.form['group']
        unit=request.form['unit']
        user=request.form['user']
        qry6="update collection set   group_id='%s',unit_collected='%s',user_id='%s' where collection_id=%s" % (group,unit,user,id)
        update(qry6)
        return '''<script>alert("Updated... ");window.location="/bl_manage_donation_col"</script>'''
        
         
        

    return render_template('bl_manage_donation.html',data=data)

@blood.route('/bl_manage_distribution',methods=['post','get'])
def bl_manage_distribution():
    data={}
    qry="select * from donors"
    qry1="select * from  bloodgroups"
    qry2="SELECT * FROM distribution  INNER JOIN bloodgroups USING(group_id) INNER JOIN donors USING(user_id)"
    data['don']=select(qry)
    data['group']=select(qry1)
    data['dis']=select(qry2)
    
    if 'submit' in request.form:
        user=request.form['user']
        group=request.form['group']
        unit=request.form['unit']
        qry="insert into distribution  values(null,'%s','%s','%s',curdate())" % (user,group,unit)
        insert(qry)
        return '''<script>alert("Added Successfully... ");window.location="/bl_manage_distribution"</script>'''
        
    if 'action' in  request.args :
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry6="delete from  distribution where distribution_id='%s'"%(id)
        delete(qry6)
        return redirect(url_for('blood.bl_manage_distribution'))
    if  action=='update':
        qry7="select * from  distribution where distribution_id='%s'"%(id)
        data['up']=select(qry7)
    if 'update' in request.form:
        user=request.form['user']
        group=request.form['group']
        unit=request.form['unit']
        
        qry="update  distribution set user_id='%s' ,group_id='%s', unit_distributed='%s' where distribution_id='%s' "%(user,group,unit,id)
        update(qry)
        return '''<script>alert("Updated... ");window.location="/bl_manage_distribution"</script>'''
        
        
    return render_template('bl_manage_distribution.html',data=data)

@blood.route('/bl_send_requirement',methods=['post','get'])
def bl_send_requirement():
    data={}
    qry="select * from donors"
    qry1="select * from bloodgroups"
    data['group']=select(qry1)
    data['user']=select(qry)
    
    if 'submit' in request.form:
        user=request.form['user']
        group=request.form['group']
        unit=request.form['unit']
        desc=request.form['desc']
        qry2="insert into requrement_message values(null,'%s','%s','%s','%s','%s')"%(session['blood'],user,group,unit,desc)
        ms=insert(qry2)
        qry3="insert into status values(null,'%s','%s',curdate(),'%s')"%(user,'pending',ms)
        insert(qry3)
        return '''<script>alert("Send Successfully. ");window.location="/bl_send_requirement"</script>'''
        
    
    
    return render_template('bl_send_requirement.html',data=data)

@blood.route('/bl_requests',methods=['post','get'])
def  bl_requests():
    data={}
    qry="select * from requests  "
    data['req']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='confirm':
        qry1="update requests set  status='Confirmed' where request_id='%s'" %(id)
        update(qry1)
        return redirect(url_for('blood.bl_requests'))
    
    
    return render_template('bl_requests.html',data=data)