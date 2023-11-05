import requests
import random
from bs4 import BeautifulSoup
import re
import lxml
import json
import pandas as pd
import csv

# headless background execution

tickers_500 = {}

with open("Fortune_1000.csv", mode="r") as f:
    csvFile = csv.reader(f)
    
    for lines in csvFile:
        # print(lines)
        tickers_500[lines[0].upper()] = (lines[1].lower()).replace(" ", "-")

print(tickers_500)
def webscrape_data(ticker, company):
    print(ticker, company)
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
    ]
    # https://www.macrotrends.net/stocks/charts/AAPL/apple/financial-ratios?freq=Q
    url_financial_statements = f'https://www.macrotrends.net/stocks/charts/{ticker}/{company}/financial-statements?freq=Q'
    # url_balance_sheet = f'https://www.macrotrends.net/stocks/charts/{ticker}/{company}/balance-sheet?freq=Q'
    url_cash_flow = f'https://www.macrotrends.net/stocks/charts/{ticker}/{company}/cash-flow-statement?freq=Q'
    url_financial_ratios = f'https://www.macrotrends.net/stocks/charts/{ticker}/{company}/financial-ratios?freq=Q'

    # FINANCIAL SHEET
    html_finance_statements = requests.get(url_financial_statements, headers={"User-Agent": random.choice(agents)}).text
    soup = BeautifulSoup(html_finance_statements, "lxml")

    divs = soup.find_all("script")
    # print("F", html_finance_statements)

    divs = list(divs[24].children) # 24

    tokens = divs[0].split("\r")
    for i in range(len(tokens)):
        if tokens[i].find("var originalData = ") != -1:
            tokens = tokens[i]
            if tokens.index("="):
                tokens = tokens[tokens.index("=") + 2:-1]
                break

    columns = []
    data = []
    tokens = json.loads(tokens)
    for i in range(len(tokens)):
        curr_str = tokens[i]['popup_icon']
        # print("s", curr_str)
        if curr_str.find('data') != -1:
            curr_str = curr_str[curr_str.find("data:") + 6: curr_str.find("<i") - 3]
            category = curr_str[curr_str.find("s: ")+4: curr_str.find(",", curr_str.find("s: "))-1]
            # print("c", category)
            # if category == "revenue":
                # columns.append(category)
            columns.append(category)

            pattern = re.compile("\d{4}-\d{2}-\d{2}")

            curr_str = tokens[i]['popup_icon']
            res = {key: tokens[i][key] if tokens[i][key] != 0 else '0' for key in tokens[i].keys() if pattern.match(key)}
            # print(res)
            data.append(res)

    # print(columns)

    index = 0
    # print(data)
    formatted_data = {"date": [key for key in data[0].keys()]}
    for i in range(len(data)):
        for key in data[i].keys():
            if columns[index] in formatted_data:
                formatted_data[columns[index]].append(data[i][key])
            else:
                formatted_data[columns[index]] = [data[i][key]]
        index += 1

    # CASH FLOW SHEET
    html_cash_flow = requests.get(url_cash_flow, headers={"User-Agent": random.choice(agents)}).text
    soup = BeautifulSoup(html_cash_flow, "lxml")
    divs = soup.find_all("script")
    divs = list(divs[24].children)

    tokens = divs[0].split("\r")
    for i in range(len(tokens)):
        if tokens[i].find("var originalData = ") != -1:
            tokens = tokens[i]
            if tokens.index("="):
                tokens = tokens[tokens.index("=") + 2:-1]
                break

    columns = []
    data = []
    tokens = json.loads(tokens)
    for i in range(len(tokens)):
        curr_str = tokens[i]['popup_icon']
        if curr_str.find('data') != -1:
            curr_str = curr_str[curr_str.find("data:") + 6: curr_str.find("<i") - 3]
            category = curr_str[curr_str.find("s: ")+4: curr_str.find(",", curr_str.find("s: "))-1]
            # columns.append(category)
            # if category == "revenue":
            columns.append(category)

            pattern = re.compile("\d{4}-\d{2}-\d{2}")

            curr_str = tokens[i]['popup_icon']
            res = {key: tokens[i][key] if tokens[i][key] != 0 else '0' for key in tokens[i].keys() if pattern.match(key)}
            data.append(res)

    index = 0
    for i in range(len(data)):
        for key in data[i].keys():
            if columns[index] in formatted_data:
                formatted_data[columns[index]].append(data[i][key])
            else:
                formatted_data[columns[index]] = [data[i][key]]
        index += 1

    # FINANCIAL RATIO SHEET
    html_financial_ratio = requests.get(url_financial_ratios, headers={"User-Agent": random.choice(agents)}).text
    soup = BeautifulSoup(html_financial_ratio, "lxml")
    divs = soup.find_all("script")
    divs = list(divs[24].children)

    tokens = divs[0].split("\r")
    for i in range(len(tokens)):
        if tokens[i].find("var originalData = ") != -1:
            tokens = tokens[i]
            if tokens.index("="):
                tokens = tokens[tokens.index("=") + 2:-1]
                break

    columns = []
    data = []
    tokens = json.loads(tokens)
    for i in range(len(tokens)):
        curr_str = tokens[i]['popup_icon']
        if curr_str.find('data') != -1:
            curr_str = curr_str[curr_str.find("data:") + 6: curr_str.find("<i") - 3]
            category = curr_str[curr_str.find("s: ")+4: curr_str.find(",", curr_str.find("s: "))-1]
            # if category == "revenue":
            columns.append(category)

            pattern = re.compile("\d{4}-\d{2}-\d{2}")

            curr_str = tokens[i]['popup_icon']
            res = {key: tokens[i][key] if tokens[i][key] != 0 else '0' for key in tokens[i].keys() if pattern.match(key)}
            data.append(res)
    # print(columns)

    index = 0
    for i in range(len(data)):
        for key in data[i].keys():
            if columns[index] in formatted_data:
                formatted_data[columns[index]].append(data[i][key])
            else:
                formatted_data[columns[index]] = [data[i][key]]
        index += 1

    # print(formatted_data)
    # for d in formatted_data:
    #     print(len(d))
    df = pd.DataFrame(formatted_data)
    df.insert(1, "ticker", ticker)
    column_to_move = df.pop("eps-earnings-per-share-diluted")
    df.insert(len(df.columns), "eps-earnings-per-share-diluted", column_to_move)
    # print(df)
    past_eps = []

    for i in range(len(df.index)):
        if i == 0:
            continue
        past_eps.append(df['eps-earnings-per-share-diluted'][i])

    past_eps = past_eps[::-1]
    past_eps.insert(0, 0)
    print("Pe", past_eps)
    df.insert(len(df.columns)-1, "past-eps-earnings-per-share-diluted", past_eps[::-1])

    this_filter = df.filter(['cost-goods-sold', 
                'gross-profit', 'research-development-expenses', 'selling-general-administrative-expenses',
                'operating-expenses', 'operating-income', 
                'total-non-operating-income-expense', 
                'pre-tax-income', 
                'total-provision-income-taxes', 
                'income-after-taxes', 
                'income-from-continuous-operations',
                'net-income', 'ebitda',
                'basic-shares-outstanding', 'shares-outstanding',
                'eps-basic-net-earnings-per-share', 'net-income-loss', 
                'total-depreciation-amortization-cash-flow', 'other-non-cash-items', 
                'total-non-cash-items', 'change-in-accounts-receivable', 
                'change-in-inventories', 'change-in-accounts-payable', 
                'change-in-assets-liabilities', 'total-change-in-assets-liabilities',
                'net-change-in-property-plant-equipment', 
                'net-change-in-intangible-assets', 
                'net-acquisitions-divestitures', 
                'net-change-in-short-term-investments', 
                'net-change-in-long-term-investments', 'net-change-in-investments-total', 
                'investing-activities-other', 'cash-flow-from-investing-activities', 
                'net-long-term-debt', 'debt-issuance-retirement-net-total', 'net-common-equity-issued-repurchased', 
                'net-total-equity-issued-repurchased', 'total-common-preferred-stock-dividends-paid', 
                'financial-activities-other', 'cash-flow-from-financial-activities', 'net-cash-flow', 
                'stock-based-compensation', 'common-stock-dividends-paid', 'long-term-debt-capital',
                'income-from-discontinued-operations', 'other-operating-income-expenses', 'net-current-debt',
                'operating-margin', 'ebit-margin', 'pre-tax-profit-margin', 'asset-turnover', 'inventory-turnover', 
                'receiveable-turnover', 'days-sales-in-receivables', 'return-on-tangible-equity', 'roa', 'roi', 'book-value-per-share', 
                'operating-cash-flow-per-share', 'free-cash-flow-per-share'
                ])
    
    df.drop(this_filter, inplace=True, axis=1)

    return df[::-1]
# print(df)

result = []

# tickers_500 = {"XOM": "exxon", "AMZN": "amazon", "WMT": "walmart", "COST": "costco", "CAH": "cardinal-health", "ABT": "abbott-laboratories"}
for key in tickers_500:
    df = webscrape_data(key, tickers_500[key])
    # column_to_move = df.pop("eps-earnings-per-share-diluted")
    # df.insert(len(df.columns), "eps-earnings-per-share-diluted", column_to_move)
    # # print(df)
    # past_eps = []

    # for i in range(len(df.index)):
    #     if i == 0:
    #         continue
    #     past_eps.append(df['eps-earnings-per-share-diluted'][i])

    # past_eps = past_eps[::-1]
    # past_eps.insert(0, 0)
    # print(past_eps)
    # df.insert(len(df.columns)-1, "past-eps-earnings-per-share-diluted", past_eps[::-1])
    result.append(df)

df = pd.concat(result)
# df = df[::-1]
df = df[1:]
# df = pd.DataFrame(df, index=pd.columns)
# df.reset_index(inplace=True, level=['Fee'])
df['ebitda-margin'] = df['ebitda-margin'].fillna(0)

print(df)

df.to_csv("out.csv", sep='\t', encoding='utf-8')