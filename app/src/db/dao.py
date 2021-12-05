# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete
import typing as t
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection
import config
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio

def get_cnx() -> MySQLConnection:
    return connect(**config.dbparams)

'''
    Investor DAO functions
'''

def get_all_investor() -> list[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors

def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    v_id = id
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ("select * from investor where id = %s"%(v_id))
    cursor.execute(sql)
    row = cursor.fetchone()
    if cursor.rowcount == 0:
        return None
    else:
        investor = Investor(row['name'], row['status'], row['id'])
        return investor 

def get_investors_by_name(name: str) -> t.Optional[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where name = "%s";'%(name)
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors


def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()

def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s;'%(id)
    cursor.execute(sql)
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = ("update investor set name = '%s' where id = %s"%(name,id))
    cursor.execute(sql)
    db_cnx.commit()
    db_cnx.close()
    pass

def update_investor_status(id: int, status: str) -> None:
    '''
        Update the inestor status [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = "update investor set status = '%s' where id = %s"%(status,id)
    cursor.execute(sql)
    db_cnx.commit()
    db_cnx.close()
    pass

'''
    Account DAO functions
'''
def get_all_accounts() -> list[Account]:
    # Code goes here
    accounts: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from account'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        accounts.append(Account(row['account_number'], row['investor_id'], row['balance']))
    db_cnx.close()
    return accounts

def get_account_by_account_number(account_number: int) -> Account:
    # Code goes here
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ("select * from account where account_number = %s"%(account_number))
    cursor.execute(sql)
    row = cursor.fetchone()
    if cursor.rowcount == 0:
        return None
    else:
        account = Account(row['account_number'], row['investor_id'], row['balance'])
        return account 




def get_accounts_by_investor_id(investor_id: int) -> list[Account]:
    # Code goes here
    accounts: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ('select * from account where investor_id = %s'%(investor_id))
    cursor.execute(sql)
    rows:list[dict] = cursor.fetchall()
    for row in rows:
        accounts.append(Account(row['account_number'], row['investor_id'], row['balance']))
    db_cnx.close()
    return accounts
    pass

def delete_account(account_number: int) -> None:
    # Code goes here
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()
    pass

def update_acct_balance(account_number: int, balance: float) -> None:
    # Code goes here
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = ('update account set balance = %s where account_number = %s'%(balance,account_number))
    cursor.execute(sql)
    db_cnx.commit()
    db_cnx.close()

    pass

def create_account(account: Account) -> None:
    # Code goes here
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (investor_id, balance) values (%s, %s)'
    cursor.execute(sql, (account.investor_id, account.balance))
    db_cnx.commit()
    db_cnx.close()
    pass

'''
    Portfolio DAO functions
'''
def get_all_portfolios() -> list[Portfolio]:
    # code goes here
    portfolios: list[Portfolio] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from portfolio'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        portfolios.append(Portfolio(row['account_id'], row['ticker'], row['quantity'],row['purchase_price']))
    db_cnx.close()
    return portfolios


def get_portfolios_by_acct_id(account_id: int) -> list[Portfolio]:
    # code goes here
    portfolios: list[Portfolio] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ('select * from portfolio where account_id = %s;'%(account_id))
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        portfolios.append(Portfolio(row['account_id'], row['ticker'], row['quantity'],row['purchase_price']))
    db_cnx.close()
    return portfolios

def get_portfolios_by_investor_id(investor_id: int) -> list[Portfolio]:
    # code goes here
    portfolios: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ('select * from portfolio left join account on account.account_number = portfolio.account_id where investor_id = %s;'%(investor_id))
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        portfolios.append(Portfolio(row['account_id'], row['ticker'], row['quantity'],row['purchase_price']))
    db_cnx.close()
    return portfolios
    

def delete_portfolio(account_id: int, ticker:str) -> None:
    # code goes here
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = ('delete from portfolio where account_id = %s and ticker = "%s"'%(account_id,ticker))
    cursor.execute(sql)
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()
    pass

def buy_stock(portfolio:Portfolio) -> None:

    v_account_id,v_ticker,v_quantity,v_purchase_price = portfolio.account_id,portfolio.ticker,portfolio.quantity,portfolio.purchase_price
    # code goes here

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = ('select * from account where account_number =%s;'%(v_account_id)) # look for current_bal respect to account_id
    cursor.execute(sql) 
    row = cursor.fetchone()
    current_bal = row[2]
    db_cnx.close()

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    used_money = float(v_quantity)*float(v_purchase_price)
    updated_bal = float(current_bal) - float(used_money)
    if updated_bal < 0:
        print('You have not enough money!')
        return None
    sql = 'update account set balance = %s where account_number = %s'%(updated_bal,v_account_id)#update the account balance
    cursor.execute(sql)
    db_cnx.commit()

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = 'select * from portfolio where account_id = %s and ticker = "%s"'%(v_account_id,v_ticker)
    cursor.execute(sql)
    a = cursor.fetchone()
    if a == None:
        db_cnx = get_cnx()
        cursor = db_cnx.cursor()
        sql: str = 'insert into portfolio (account_id, ticker, quantity, purchase_price) values (%s, "%s", %s, %s)'%(v_account_id,v_ticker,v_quantity,v_purchase_price)#create portfolio
        cursor.execute(sql)
        db_cnx.commit()
        db_cnx.close()

    else:
        current_quantity = a[2]
        new_quantity = float(current_quantity) + float(v_quantity)
        db_cnx = get_cnx()
        cursor = db_cnx.cursor()
        sql: str = ('update portfolio set portfolio.quantity= %s where account_id = %s and ticker = "%s";'%(new_quantity,v_account_id,v_ticker))
        cursor.execute(sql)
        db_cnx.commit()

        db_cnx = get_cnx()
        cursor = db_cnx.cursor()
        sql: str = ('update portfolio set portfolio.purchase_price= %s where account_id = %s and ticker = "%s";'%(v_purchase_price,v_account_id,v_ticker))
        cursor.execute(sql)
        db_cnx.commit()
        db_cnx.close()
        
    pass

def sell_stock(portfolio:Portfolio) -> None:
    # 1. update quantity in portfolio table
    # 2. update the account balance:
    # Example: 10 APPL shares at $1/share with account balance $100
    # event: sale of 2 shares for $2/share
    # output: 8 APPLE shares at $1/share with account balance = 100 + 2 * (12 - 10) = $104


    v_account_id,v_ticker,v_quantity,v_sale_price = portfolio.account_id,portfolio.ticker,portfolio.quantity,portfolio.purchase_price
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = ('select * from portfolio where account_id = %s and ticker = "%s";'%(v_account_id,v_ticker))
    cursor.execute(sql)
    row_p = cursor.fetchone()
    if row_p == 0:
        return None
    else:
        current_quantity = row_p['quantity']

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql: str = ('select * from account where account_number =%s;'%(v_account_id)) # look for current_bal respect to account_id
    cursor.execute(sql) 
    row_a = cursor.fetchone()
    current_bal = row_a[2]

    saled_money = float(v_quantity)*float(v_sale_price)
    updated_bal = float(current_bal) + float(saled_money)
    updated_quantity = float(current_quantity) - float(v_quantity)
    if updated_quantity < 0:
        print('Your have not enough stocks to sell')
        return None

    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update portfolio set quantity= %s where account_id = %s and ticker = "%s";'%(updated_quantity,v_account_id,v_ticker)
    cursor.execute(sql)
    db_cnx.commit()
    
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance = %s where account_number = %s;'%(updated_bal,v_account_id)
    cursor.execute(sql)
    db_cnx.commit()

    db_cnx.close()
    pass

