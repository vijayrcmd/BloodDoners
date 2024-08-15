from  flask import *
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

    return render_template('admin_home.html')

@admin.route('/manage_blood_grp',methods=['post','get'])
def  manage_blood_group():
    data={}
    qry2="select * from bloodgroups"
    data['blood']=select(qry2)
  
    if 'submit' in request.form:
        group_name=request.form['group_name']
        group_des=request.form['desc']
        qry="insert into bloodgroups values(null,'%s','%s')"%(group_name,group_des)
        insert(qry)
        return '''<script>alert("Added blood group");window.location="/manage_blood_grp"</script>'''
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if  action=='delete':
        qry3="delete from bloodgroups where group_id='%s'"%(id)
        delete(qry3)
        return redirect(url_for('admin.manage_blood_group'))
    if action=='update':
        qry4="select * from bloodgroups where group_id='%s'"%(id)
        data['up']=select(qry4)
    if 'update' in request.form:
        group_name=request.form['group_name']
        group_des=request.form['desc']
        qry5="update bloodgroups set  group_name='%s',group_description='%s' where group_id=%s "%(group_name,group_des,id)
        update(qry5)
        
        
    return render_template('ad_manage_blood_group.html',data=data)

@admin.route('/view_blood_banks')
def view_blood_banks():
    data={}
    qry="select * from bloodbanks"
    data['bank']=select(qry)
    return render_template('ad_view_blood_banks.html',data=data)

@admin.route('/view_donors')
def view_donors():
    data={}
    qry="SELECT * FROM donors INNER JOIN bloodgroups USING(group_id) INNER JOIN STATUS USING(user_id) WHERE donation_availability_status='okey' GROUP BY user_id"
    data['donors']=select(qry)
    return render_template('ad_view_donors.html',data=data)


@admin.route('/view_recivers')
def view_recivers():
    data={}
    qry="SELECT * FROM donors INNER JOIN bloodgroups USING(group_id) INNER JOIN requests USING(user_id) GROUP BY user_id"
    data['rec']=select(qry)
    return render_template('ad_view_recivers.html',data=data)

@admin.route('/view_request')
def view_request():
    data={}
    qry="select * from requests inner join bloodgroups using(group_id) inner join donors using(user_id)"
    data['req']=select(qry)
    return render_template('ad_view_request.html',data=data)

@admin.route('/view_blood_banks_col_rep')
def view_blood_banks_col_rep():
    data={}
    qry="select * from collection inner join bloodbanks using(bank_id) inner join bloodgroups using(group_id) inner join donors using(user_id)"
    data['coll']=select(qry)
    return render_template('ad_view_blood_banks_col_rep.html',data=data)