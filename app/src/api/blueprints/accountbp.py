import simplejson as json
from flask import Blueprint, request
import app.src.db.dao as dao
from app.src.domain.Account import Account

accountbp = Blueprint('account', __name__, url_prefix='/account')

@accountbp.route('/get-all-accounts', methods = ['GET'])
def get_all_accounts():
    try:
        accounts = dao.get_all_accounts()
        if accounts is None:
            return json.dumps([]), 200
        else:
            return json.dumps([account.__dict__ for account in accounts]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/get-account-by-account_number/<account_number>', methods = ['GET'])
def get_account_by_account_number(account_number:int) -> Account:
    try:
        account = dao.get_account_by_account_number(account_number)
        if account is None:
            return json.dumps([]), 200
        else:
            return json.dumps(account.__dict__), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/get-accounts-by-investor_id/<investor_id>', methods = ['GET'])
def get_accounts_by_investor_id(investor_id:int) -> Account:
    try:
        accounts = dao.get_accounts_by_investor_id(investor_id)
        if accounts is None:
            return json.dumps([]), 200
        else:
            return json.dumps([account.__dict__ for account in accounts]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/create/<investor_id>/<balance>', methods = ['POST'])
def create_account(investor_id,balance):
    account = Account(None,investor_id,balance)
    try:
        dao.create_account(account)
        return json.dumps(account.__dict__)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/delete/<account_number>', methods = ['DELETE'])
def delete_account(account_number):
    try:
        dao.delete_account(account_number)
        return 'ok, deleted'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@accountbp.route('/update-acct_balance/<account_number>/<balance>', methods = ['PUT'])
def update_acct_balance(account_number ,balance):
    try:
        dao.update_acct_balance(account_number,balance)
        return 'ok, updated'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

