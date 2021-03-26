# Test Plan
## 1 Introduction

The test plan is created to communicate the test approach to team members. It includes the objectives,
task assignments, problems found during the research phase, risks, severity of source code to be tested,
test approach, and test environment.

### 1.1 Objective

We will test the functionality and usability of the code .cashflow and .quarterly_cashflow in lines 180 to 
186 of "ticker.py" to find potential causes of the errors.

### 1.2 List of Related Issues

```
● Problems with qualitative calls #618
● Missing fundamental data #547 (closed)
● ticker.financials, .cashflow, and .balance_sheet displaying blank data frame #518
● Financial Data not fetched #489
● Empty data frame is returned for earnings, cashflow,balance sheet and financials #475
● Income statement, cash flow, balance sheet data is unavailable #465
● New issues on retrieving financial statement data #423
● Financials information and more attributes are empty #419
● Empty DataFrame for any financial related data #350(closed)
● Empty DataFrame returned #343
● get cashflow null dataframe #338
● Can't get cashflow data back #328
● Please include all the financial information for NSE(Indian stocks ) too #311
● Yahoo Finance URL Change #271
● Unable to get balance sheet and for all tickers -Module down? #254
● ASX Data for financials, cashflow and balance does not appear to be scraped correctly.#250
● Financials data not working with some Brazilian Stocks #240
● Financial statements not working #234
● lxml should be added as a dependency #227
● Fetched data discrepancies #218
● Income Statement, Balance Sheet and Cashflows are coming up as an empty dataframe #191
● Earnings and other financial information now being populated #181
● KeyError: 'financialsChart' #173
● No financial data ver 0.1.54 #158
● Error when using ticker.info #150
● Ticker info gives error #131(closed)
● Intelligent caching of yfinance results not implemented #118
● Financials, Balance Sheets and Cashflows do not work any more #111(closed)
```
### 1.3 List of Related Pull Requests

```
● Update base.py #392 (closed)
● Fixed stock.financials/balance_sheet/cashflow. Added valuation indicators. #321
● Fixes the scrape URL for financial data #246 (closed)
● Bugfix, add _expirations to base #117 (merged)
● Add date localization/fundamentals now properly use datetime columns and data as floats #108 (closed)
● Quarterly/yearly financials/cashflow/bsheet in 1 fetch#104 (closed)
● Fix errors that can occur with partial data #94 (merged)
● Fix the fetching of fundamentals #480 (merged)
```
### 1.4 Team Members

```Resource,   Name Role```
```
Problems with qualitative calls #618, Andi and Junyao
```
```
Financial Data not fetched #489, Maaz and Ali
```
```
ticker.financials, .cashflow, and .balance_sheet displaying blank data frame #518, Farish and Manpreet
```
## 2 Problems Found

a). Based on the manual test for printing out thecash flow and quarterly_cashflow data with different
stock symbols, we found that it can only show up thedata for specified Ticker objects which are MSFT,
GOOG and AAPL. For other stock symbols, it will showthe empty data frame. And this problem is
related to the issues #618.

## 3 List of Planned Test


a). Test if the base url works

b). Test if the scrape url works

c). Test if it gets the cashflow and quarterly cashflowdata successfully

## 4 Risks Involved

```#                   Risk                                           Impact                Trigger                    Mitigation Plan```
```
1. Scope Creep – as testers become more familiar with the tool, they will want more functionality   
High  
Delays in implementation date  
Each iteration, functionality will be closely monitored. Priorities will be set and discussed by stakeholders. Since the driver is functionality and not time, it may be necessary to push the date out 
```
```
2. Changes to the functionality may negate the tests already written and we may lose test cases already written
High 
Loss of all test cases
Export data prior to any upgrade, massage as necessary and re-import after upgrade
```
```
3 Some test may not pass due to the unfixable situation.
High 
Unfixable error
```
## 5 Test Approach

```
The project is using an agile approach, with weeklyiterations.
```
## 6 Test Environment

```
App should run under the following environment:
              python>= 2.7, 3.4+ with multitasking and yfinancemodule installed
```

