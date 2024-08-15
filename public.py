from  flask import *
from database import*

public=Blueprint('public',__name__)

# public home

@public.route('/')
def home():

    return render_template('home.html')


# login home


@public.route('/user_register',methods=['post','get'])
def user_register():
    if 'submit' in request.form:
       firstname=request.form['firstname']
       lastname=request.form['lastname']
       group=request.form['group']
       gender=request.form['gender']
       age=request.form['age']
       place=request.form['place']
      
       pincode=request.form['pincode']
       phone=request.form['phone']
       email=request.form['email']
       username=request.form['username']
       password=request.form['password']
       qry="insert into login values(null,'%s','%s','donor')"%(username,password)
       res1=insert(qry)

        
       qry1="insert into donors values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res1,firstname,lastname,group,gender,age,place,pincode,phone,email)
       insert(qry1) 
    
    
       return redirect(url_for('public.home'))
    return render_template('user_register.html')
    
@public.route('/login',methods=['post','get']) 
def login():
        if 'submit' in request.form:
      
            username=request.form['username']
            password=request.form['password']
            qry="select * from  login where username='%s' and password='%s'"%(username,password)
            res=select(qry)
         
          
            if  res:
                session['lid']=res[0]['login_id']
                print(session['lid'])
                if  res[0]['usertype']=='admin':
                        return '''<script>alert("welcome admin");window.location="/admin_home"</script>'''
            
                elif res[0]['usertype']=='bank':
                    qry1="select * from bloodbanks where login_id='%s'"%(session['lid'])
                    res1=select(qry1)
                    session['blood']=res1[0]['bank_id']
                    return redirect(url_for('blood.blood_home'))
                
                if res[0]['usertype']=='donor':
                    qry4="select * from donors where login_id='%s'"%(session['lid'])
                    a=select(qry4)
                    if a:
                      session['donor']=a[0]['user_id']
                      print(session['donor'])
           
                    return redirect(url_for('donor.donor_home'))    
            else :
                return '''<script>alert("user not found ");window.location="/login"</script>'''
        return render_template('login.html')



@public.route('/blood_register',methods=['post','get'])
def  blood_registration():
    if 'submit' in request.form:
        name=request.form['name']
        place=request.form['place']
        pincode=request.form['pincode']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        qry1="insert into login values(null,'%s','%s','bank')"%(username,password)
        lid=insert(qry1)
        qry="insert into  bloodbanks values(null,'%s','%s','%s','%s','%s','%s')"%(lid,name,place,pincode,phone,email)
        insert(qry)
        return '''<script>alert("Registration successfully ");window.location="/login"</script>'''
        
    return render_template('blood_register.html')