import json
from flask import Blueprint, request
import app.src.db.dao as dao
from app.src.domain.Investor import Investor



investorbp = Blueprint('investor', __name__, url_prefix='/investor')

@investorbp.route('/get-investor-by-id/<id>', methods = ['GET'])
def get_investor_by_id(id:int) -> Investor:
    try:
        investor = dao.get_investor_by_id(id)
        if investor is None:
            return json.dumps([]), 200
        else:
            return json.dumps(investor.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500


@investorbp.route('/get-all-investor', methods = ['GET'])
def get_all_investors():
    try:
        investors = dao.get_all_investor()
        if investors is None:
            return json.dumps([]), 200
        else:
            return json.dumps([investor.__dict__ for investor in investors]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/get-investor-by-name/<name>', methods = ['GET'])
def get_investor_by_name(name:str) -> Investor:
    try:
        investors = dao.get_investors_by_name(name)
        if investors is None:
            return json.dumps([]), 200
        else:
            return json.dumps([investor.__dict__ for investor in investors]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route("/create/<name>", methods = ['POST'])
def create_investor(name):
    query_params = request.args
    status = 'ACTIVE'
    if 'status' in query_params:
        status = query_params.get('status')
    investor = Investor(name,status,None)
    try:
        dao.create_investor(investor)
        return json.dumps(investor.__dict__)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/delete/<id>', methods = ['DELETE'])
def delete_investor(id):
    try:
        dao.delete_investor(id)
        return 'ok, deleted'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/update-investor-name/<id>/<name>', methods = ['PUT'])
def update_investor_name(id ,name):
    try:
        dao.update_investor_name(id,name)
        return 'ok, updated'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@investorbp.route('/update_investor_status/<id>/<status>', methods = ['PUT'])
def update_investor_status(id ,status):
    try:
        dao.update_investor_status(id ,status)
        return 'ok, updated'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

