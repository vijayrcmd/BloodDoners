from flask import *
from public import *
from admin import*
from bloodbanks import *
from donor import *

app=Flask(__name__)
app.secret_key='7676'
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(blood)
app.register_blueprint(donor)
app.run(debug=True)