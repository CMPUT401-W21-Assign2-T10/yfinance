# TEST CASE REPORT

# Cashflow fethcing dataframe

### GENERAL INFORMATION

Test Stage: 
```
Unit Test
```
Test Date: 
```
2021-03-27
```
Tester: 
```
Maaz Siddique & Ali Reza
```
Test Case Description:
```
Test if the system gets an empty dataframe or realtime data frame for the cashflow data of different stock symbols
```
Results:  ``fail`` 
### INTRODUCTION
Roles and Responsibilities:
```
Maaz Siddique and Ali Reza are responsible to write the tests for cashflow dataframe check
```
Set Up Procedures: 
```
Get cashflow dataframe of each tinker object
```
Stop Procedures:
```
Either receive empty dataframe cashflow or get the realtime data frame
```
### TEST
Test Items and Features: 
```
Items: 'MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD', 'BMW', "TSLA"
```
```
Features: Gets cashflow dataframe
```
Input Specifications: 
```
No input required
```
Procedural Steps: 
```
Get cashflow dataframe of each tinker objects one by one
```
Expected Results of Case:
```
The data frame of all objects should be empty
```
### ACTUAL RESULTS
Output Specifications: ``Fail``
```
MSFT:     realtime data frame
IWO:      empty data frame
VFINX:    empty data frame
^GSPC:    empty data frame
BTC-USD:  empty data frame
BMW:      empty data frame
SPY:      empty data frame
RIOT:     realtime data frame
TSLA:     realtime data frame
```
