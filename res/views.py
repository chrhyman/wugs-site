#import json

from flask import Blueprint, render_template#, make_response

mod_res = Blueprint('res', __name__, url_prefix='/games/res')

#from models import User

@mod_res.route('/', methods=['GET'])
def index():
    return render_template('res.html')

'''
@mod_res.route('/room/<room>', methods=['GET', 'POST'])
def resroom(room):
    room = int(room)
    # room handler

@mod_res.route('/room/<room>/json', methods=['GET'])
def jsn(room):
    json_list = [{'name':x.username,'pw':x.password} for x in User.query.all()]
    json_list = json.dumps(json_list)
    response = make_response(json_list)
    response.headers['Content-Type'] = 'application/json'
    return response
    pass
'''