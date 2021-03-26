# TEST CASE REPORT

# Quarterly cashflow data fetching test

### GENERAL INFORMATION

Test Stage: 
```
Unit Test
```
Test Date: 
```
2021-03-26
```
Tester: 
```
Andi He
```
Test Case Description:
```
Test if the system get the quarterly cashflow data of different stock symbols successfully
```
Results:  ``fail`` 
### INTRODUCTION
Roles and Responsibilities:
```
Andi He is responsible to write the tests for quarterly cashflow data check
```
Set Up Procedures: 
```
Get quarterly cashflow data of each tinker object
```
Stop Procedures:
```
Either receive empty data or reach the last tinker object
```
### TEST
Test Items and Features: 
```
Items: MSFT, IWO, VFINX, ^GSPC, BTC-USD
```
```
Features: Gets quarterly cashflow data
```
Input Specifications: 
```
No input required
```
Procedural Steps: 
```
Get quarterly cashflow data of each tinker objects one by one
```
Expected Results of Case:
```
The data frame of all objects should be non-empty
```
### ACTUAL RESULTS
Output Specifications: ``Fail``
```
MSFT:     realtime data frame
IWO:      empty data frame
VFINX:    empty data frame
^GSPC:    empty data frame
BTC-USD:  empty data frame
```
