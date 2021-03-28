# System Test Case:

# Cashflow dataframe fetching test

```
Purpose: Test if the system gets an empty dataframe from the cashflow successfully
```
```
Test Run Info:
Tester Name: Maaz Siddque & Ali Reza
Date(s) of Test: 2021-03-27
```
```
TEST SCRIPT STEPS/RESULT:

STEP | TEST STEP/INPUT   |  EXPECTED RESULT  |  ACTUAL RESULTS  | PASS/FAIL
----------------------------------------------------------------------------
1    | Input MSFT ticker | Empty DataFrame   | Realtime stock   | Fail
     | object and get    | (no Data)         | data             |
     | the data frame of |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
2    | Input IWO ticker  | Empty DataFrame   | Empty data frame | Pass
     | object and get    | (no Data)         |                  |
     | the data frame of |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
3    | Input VFINX ticker| Empty DataFrame   | Empty data frame | Pass
     | object and get    | (no Data)         |                  |
     | the data frame of |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
4    | Input ^GSPC       | Empty DataFrame   | Empty data frame | Pass
     | ticker object and | (no Data)         |                  |
     | get the data frame|                   |                  |
     | of cashflow       |                   |                  |
----------------------------------------------------------------------------
5    | Input BTC-USD     | Empty DataFrame   | Empty data frame | Pass
     | ticker object and | (no Data)         |                  |
     | get the data frame|                   |                  |
     | of cashflow       |                   |                  |
----------------------------------------------------------------------------
6    | Input BMW         | Empty DataFrame   | Empty data frame | Pass
     | ticker object and | (no Data)         |                  |
     | get the data frame|                   |                  |
     | of cashflow       |                   |                  |
----------------------------------------------------------------------------
7    | Input TSLA        | Empty DataFrame   | Realtime stock   | Fail
     | ticker object and | (no Data)         | data             |
     | get the data frame|                   |                  |
     | of cashflow       |                   |                  |
----------------------------------------------------------------------------
```

