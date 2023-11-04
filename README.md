Data Description
The first group of variables contains information about the client personal information: 
1. ID: ID of each client, categorical variable 
2. LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit) 
3. SEX: Gender, categorical variable (1=male, 2=female) 
4. EDUCATION: level of education, categorical variable (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown) 
5. MARRIAGE: Marital status, categorical variable (1=married, 2=single, 3=others) 
6. AGE: Age in years, numerical variable 

The following attributes contains information about the delay of the past payment referred to a specific month: 
1. PAY_0: Repayment status in September 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) 
2. PAY_2: Repayment status in August 2005 (same scale as before) 
3. PAY_3: Repayment status in July 2005 (same scale as before) 
4. PAY_4: Repayment status in June 2005 (same scale as before) 
5. PAY_5: Repayment status in May 2005 (same scale as before) 
6. PAY_6: Repayment status in April 2005 (same scale as before)

Other variables instead consider the information related to the amount of bill statement (i.e. a monthly report that credit card companies issue to credit card holders in a specific month): 
1. BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar) 
2. BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar) 
3. BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar) 
4. BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar) 
5. BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar) 
6. BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar) 

The following variables instead consider the amount of previous payment in a specific month: 
1. PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar) 
2. PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar) 
3. PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar) 
4. PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar) 
5. PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar) 
6. PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar) 

The last variable is the one to be predicted:

default.payment.next.month: indicate whether the credit card holders are defaulters or non-defaulters 
1=yes, 
0=no
