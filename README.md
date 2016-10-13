# Apriori-Implementation
Brute Force Implementation 
of Apriori Algorithm 
for Association Rule Mining 
for Market Basket Analysis 
using Freuquent Data Item Set 
given Minimum Support Count and Minimum acceptable Confidence.

There are two files.

###Apriori.py
This file contains the code for accepting number of transactions, number of items, input, generating the frequent item dataset 
as per the defined minimum support count in the input
and generate the respective association rules that satisfy the condition of minimum confidence defined in the input.

###IP.txt
Line 1 - Number of Items

Line 2 - Number of Transactions

Line 3 - Minimum Support Count

Line 4 - Minimum Confidence Threshold

Line 5 to 49 - The input in the form of 0s and 1s.*

*The input is entered for each item in each transaction. If the item exists in the given transaction, the input is entered as 1.
The input defined is for the following example:-

| TID | List of Items |
| --- | --- |
| T100 | I1, I2, I5 |
| T200 | I2, I4 |
| T300 | I2, I3 |
| T400 | I1, I2, I4 |
| T500 | I1, I3 |
| T600 | I2, I3 |
| T700 | I1, I3 |
| T800 | I1, I2 , I3, I5 |
| T900 | I1, I2, I3 |

Minimum Support Count : 2

Confidence : 0.7
