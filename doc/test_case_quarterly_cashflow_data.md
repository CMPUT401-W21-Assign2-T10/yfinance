# System Test Case:

# Quarterly cashflow data fetching test

```
Purpose: Test if the system gets the quarterly cashflow data of different stock symbols successfully
```
```
Test Run Info:
Tester Name: Andi He
Date(s) of Test: 2021-03-26
```
```
TEST SCRIPT STEPS/RESULT:

STEP | TEST STEP/INPUT   |  EXPECTED RESULT  |  ACTUAL RESULTS  | PASS/FAIL
----------------------------------------------------------------------------
1    | Input MSFT ticker | Realtime stock    | Realtime stock   | Pass
     | object and get    | data              | data             |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
2    | Input IWO ticker  | Realtime stock    | Empty data frame | Fail
     | object and get    | data              |                  |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
3    | Input VFINX ticker| Realtime stock    | Empty data frame | Fail
     | object and get    | data              |                  |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
4    | Input ^GSPC       | Realtime stock    | Empty data frame | Fail
     | ticker object and | data              |                  |
     | get the data frame|                   |                  |
     | of  quarterly     |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
5    | Input BTC-USD     | Realtime stock    | Empty data frame | Fail
     | ticker object and | data              |                  |
     | get the data frame|                   |                  |
     | of  quarterly     |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
```

