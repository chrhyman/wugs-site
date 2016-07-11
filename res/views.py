from flask import Blueprint

mod_res = Blueprint('res', __name__, url_prefix='/games')

@mod_res.route('/res', methods=['GET'])
def res():
    return 'Hi'
