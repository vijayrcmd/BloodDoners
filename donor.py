from  flask import *
from database import*

donor=Blueprint('donor',__name__)

@donor.route( '/donor_home' , methods = [ 'GET','POST'])
def donor_home():
    return render_template('donor_home.html')

@donor.route('/dn_view_req_msg')
def  dn_view_req_msg():
    qry="SELECT * FROM requrement_message INNER JOIN bloodgroups USING(group_id) INNER JOIN donors USING(user_id) INNER JOIN STATUS USING(message_id) INNER JOIN bloodbanks USING(bank_id) WHERE donors.user_id = '%s'"%(session['donor']); 
    data={}
    data['req']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='okey':
        qry2="update status set donation_availability_status='okey' where message_id='%s'"%(id)
        update(qry2)
        return redirect(url_for('donor.dn_view_req_msg'))
        
    
    if action=='no':
        qry3="update status set donation_availability_status='no' where message_id='%s'"%(id)
        update(qry3)
        return redirect(url_for('donor.dn_view_req_msg'))
        
    
    return render_template('dn_view_req_msg.html',data=data)

@donor.route('/dn_donated_details')
def dn_donated_details():
    data={}
    qry="SELECT * FROM donors INNER JOIN STATUS USING(user_id)  INNER JOIN requrement_message USING(message_id) WHERE donation_availability_status='okey' AND donors.user_id='%s'"%(session['donor'])
    data['don']=select(qry)
    return render_template('dn_donated_details.html',data=data)


@donor.route("/dn_request_for_blood",methods=["POST","get"])
def dn_request_for_blood():
    # qry=" SELECT * FROM requests  INNER JOIN `bloodgroups` USING(group_id) INNER JOIN donors USING(user_id) "
    # data={}
    # data['req']=select(qry)
    data={}
    qry="select * from bloodgroups"
    qry2="select * from requests where user_id='%s'"%(session['donor']) 
    data['req']=select(qry2)
       
    data['blood']=select(qry)
    if 'request' in request.form:
        group=request.form['group']
        unit=request.form['unit']
        pin=request.form['pincode']
        qry1="insert into requests values(null,'%s','%s',curdate(),'%s','%s','pending')"%(session['donor'],group,unit,pin)
        insert(qry1)
        return '''<script>alert("Blood Requested... ");window.location="/dn_request_for_blood"</script>'''
        
    
    return render_template('dn_request_for_blood.html',data=data)