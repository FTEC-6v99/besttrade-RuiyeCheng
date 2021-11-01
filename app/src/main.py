import app.src.db.dao as dao
from app.src.domain.Account import Account
from app.src.domain.Investor import Investor


def main():
    # investors = dao.get_all_investor()
    # print('test get_all_investor()')
    # for investor in investors:
    #     print(f'{investor.name},{investor.status},{investor.id}')

    # investor = dao.get_investor_by_id(2)
    # print('test get_investor_by_id()')
    # if investor == None:
    #     print('id does not exist')
    # else:
    #     print(f'{investor.name},{investor.status},{investor.id}')

    # investors = dao.get_investors_by_name('John Doe')
    # print('test get_investors_by_name()')
    # if investors == None:
    #     print('account number does not exist')
    # else:
    #     for investor in investors:
    #         print(f'{investor.name},{investor.status},{investor.id}')

    # dao.create_investor(Investor("Jo JO","Active",None))
    # print('test create_investor')
    # investors = dao.get_all_investor() 
    # for investor in investors:
    #     print(f'{investor.name},{investor.status},{investor.id}')

    # dao.delete_investor(4)
    # print('test delete_investor')
    # investors = dao.get_all_investor() 
    # for investor in investors:
    #     print(f'{investor.name},{investor.status},{investor.id}')

    # account = dao.get_account_by_account_number(1)
    # print('get_account_by_account_number()')
    # if account == None:
    #     print('account number does not exist')
    # else:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # accounts = dao.get_all_accounts()
    # print('test get_all_accounts()')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # accounts = dao.get_accounts_by_investor_id(2)
    # print('test get_accounts_by_investor_id')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # dao.create_account(Account(None,2,90000))
    # accounts = dao.get_all_accounts()
    # print('test create accounts()')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # dao.delete_account(5)
    # accounts = dao.get_all_accounts()
    # print('test delete accounts()')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # dao.update_acct_balance(2,13000.0)
    # accounts = dao.get_all_accounts()
    # print('test update_acct_balance()')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    # dao.get_all_portfolios()
    # portfolios = dao.get_all_portfolios()
    # print('test get_all_portfolios')
    # for portfolio in portfolios:
    #     print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')

    # portfolios = dao.get_portfolios_by_acct_id(1)
    # print('test get_portfolios_by_acct_id')
    # for portfolio in portfolios:
    #     print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')

    # portfolios = dao.get_portfolios_by_investor_id(2)
    # print('test get_portfolios_by_investor_id')
    # for portfolio in portfolios:
    #     print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')

    # dao.delete_portfolio(3,"JPM")
    # portfolios = dao.get_all_portfolios()
    # print('test delete stock')
    # for portfolio in portfolios:
    #     print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')

    # dao.buy_stock(1,"FB",5,10000)
    # portfolios = dao.get_all_portfolios()
    # print('test buy stock')
    # for portfolio in portfolios:
    #     print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')
    # accounts = dao.get_all_accounts()
    # print('test get_all_accounts()')
    # for account in accounts:
    #     print(f'{account.account_number},{account.balance},{account.investor_id}')

    dao.sell_stock(1,"FB",1,20)
    portfolios = dao.get_all_portfolios()
    print('test sell stock')
    for portfolio in portfolios:
        print(f'{portfolio.ccount_id},{portfolio.purchase_price},{portfolio.quantity},{portfolio.ticker}')
    accounts = dao.get_all_accounts()
    print('test get_all_accounts()')
    for account in accounts:
        print(f'{account.account_number},{account.balance},{account.investor_id}')


####Please comment other functions while testing a function    
if __name__ == '__main__':
    main()