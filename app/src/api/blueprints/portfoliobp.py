import simplejson as json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Portfolio import Portfolio

portfoliobp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@portfoliobp.route('/get-all-portfolios', methods = ['GET'])
def get_all_portfolios():
    try:
        portfolios = dao.get_all_portfolios()
        if portfolios is None:
            return json.dumps([]), 200
        else:
            return json.dumps([portfolio.__dict__ for portfolio in portfolios]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/get-portfolios-by-account_id/<account_id>', methods = ['GET'])
def get_portfolios_by_acct_id(account_id:int) -> Portfolio:
    try:
        portfolios = dao.get_portfolios_by_acct_id(account_id)
        if portfolios is None:
            return json.dumps([]), 200
        else:
            return json.dumps([portfolio.__dict__ for portfolio in portfolios]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/get-portfolios-by-investor-id/<investor_id>', methods = ['GET'])
def get_portfolios_by_investor_id(investor_id:int) -> Portfolio:
    try:
        portfolios = dao.get_portfolios_by_investor_id(investor_id)
        if portfolios is None:
            return json.dumps([]), 200
        else:
            return json.dumps([portfolio.__dict__ for portfolio in portfolios]), 200
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/buy-stock/<account_id>/<ticker>/<quantity>/<purchase_price>', methods = ['PUT'])
def buy_stock(account_id, ticker, quantity, purchase_price):
    portfolio = Portfolio(account_id,ticker,quantity,purchase_price)
    try:
        dao.buy_stock(portfolio)
        return json.dumps(portfolio.__dict__)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/sell-stock/<account_id>/<ticker>/<quantity>/<purchase_price>', methods = ['PUT'])
def sell_stock(account_id, ticker, quantity, purchase_price):
    portfolio = Portfolio(account_id,ticker,quantity,purchase_price)
    try:
        dao.sell_stock(portfolio)
        return json.dumps(portfolio.__dict__)
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

@portfoliobp.route('/delete/<account_id>/<ticker>', methods = ['DELETE'])
def delete_portfolio(account_id,ticker):
    try:
        dao.delete_portfolio(account_id,ticker)
        return 'ok, deleted'
    except Exception as e:
        return  'Oops, an error occured:' + str(e), 500

