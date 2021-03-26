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
1.0  | Loop over the     | Information of a  | Information of a | Pass
     | list of tinker    | single tinker     | single tinker    |
     | objects and get   | object            | object           |
     | their infos       |                   |                  |
----------------------------------------------------------------------------
2.0  | Input MSFT tinker | Realtime stock    | Realtime stock   | Pass
     | object and get    | data              | data             |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
2.1  | Input IWO tinker  | Realtime stock    | Empty data frame | Fail
     | object and get    | data              |                  |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
2.2  | Input VFINX tinker| Realtime stock    | Empty data frame | Fail
     | object and get    | data              |                  |
     | the data frame of |                   |                  |
     | quarterly cashflow|                   |                  |
----------------------------------------------------------------------------
2.3  | Input ^GSPC       | Realtime stock    | Empty data frame | Fail
     | tinker object and | data              |                  |
     | get the data frame|                   |                  |
     | of  quarterly     |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
2.3  | Input BTC-USD     | Realtime stock    | Empty data frame | Fail
     | tinker object and | data              |                  |
     | get the data frame|                   |                  |
     | of  quarterly     |                   |                  |
     | cashflow          |                   |                  |
----------------------------------------------------------------------------
```

