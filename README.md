## Data Description
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

#### EDA Observations:
1. The default payment is maximum for credit limit below 370000 
2. The default payment is generally seen after 2.5 years for any maaximum of cases 
3. Maximum default payment along with bill payment is found in the region within 500000
4. Age group of above 24 yrs and below 40 yrs have maximum default with average count of 300
5. Highest default happend for credit limit of 50k

## 1. TRAINING MODEL: LOGISTIC REGRESSION / RANDOM FOREST / XGBOOST 
## 2. HYPER PARAMETER TUNNING USING GRID SEARCHCV
## 3. AUC/ROC CURVE AND SCORES

Penalty and Solver
solver: {‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’}, default=’lbfgs’ Algorithm to use in the optimization problem. Default is ‘lbfgs’. To choose a solver, you might want to consider the following aspects:

For small datasets, ‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones;

For multiclass problems, only ‘newton-cg’, ‘sag’, ‘saga’ and ‘lbfgs’ handle multinomial loss;

‘liblinear’ is limited to one-versus-rest schemes.

‘newton-cholesky’ is a good choice for n_samples >> n_features, especially with one-hot encoded categorical features with rare categories. Note that it is limited to binary classification and the one-versus-rest reduction for multiclass classification. Be aware that the memory usage of this solver has a quadratic dependency on n_features because it explicitly computes the Hessian matrix.

Warning The choice of the algorithm depends on the penalty chosen.

Supported penalties by solver:

‘lbfgs’ - [‘l2’, None]

‘liblinear’ - [‘l1’, ‘l2’]

‘newton-cg’ - [‘l2’, None]

‘newton-cholesky’ - [‘l2’, None]

‘sag’ - [‘l2’, None]

‘saga’ - [‘elasticnet’, ‘l1’, ‘l2’, None]

penalty{‘l1’, ‘l2’, ‘elasticnet’, None}, default=’l2’ Specify the norm of the penalty:

None: no penalty is added;

'l2': add a L2 penalty term and it is the default choice;

'l1': add a L1 penalty term;

'elasticnet': both L1 and L2 penalty terms are added.

![conf-1](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/0c9b2d4e-11aa-4d84-883d-53763ac69a31)


## Other models analysed:
*1. Random Forest*
*2. XbBoost*
*3. CatBoost*

### Best Model
**best_model= XGBoost**

**Accuracy= 0.8205**

**F1-score=0.45797684952189227**

##  roc_curve and roc_auc_scores

#### ROC: Receiver Operator Characteristic 
###### ROC_CURVE: Basically, ROC curve is a graph that shows the performance of a classification model at all possible thresholds( threshold is a particular value beyond which you say a point belongs to a particular class). The curve is plotted between two parameters TRUE POSITIVE RATE(TPR) and FALSE POSITIVE RATE(FPR) 

#### AUC: Area Under Curve
##### ROC_AUC_SCORES: AUC measures how well a model is able to distinguish between classes. ROC_AUC_SCORES defines the amount of tries to measure if the rank ordering of classifications is correct it does not take into account actually predicted probabilities

#### Precision_Recall_Curve
###### Precision is the proportion of correct positive classifications (true positive) divided by the total number of predicted positive classifications that were made (true positive + false positive). Recall is the proportion correct positive classifications (true positive) divided by the total number of the truly positive classifications (true positive + false negative).

######    A PR curve is simply a graph with Precision values on the y-axis and Recall values on the x-axis. In other words, the PR curve contains TP/(TP+FP) on the y-axis and TP/(TP+FN) on the x-axis.


![aoc-roc](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/3bc056e1-a2c6-497f-8116-5c04be4c3541)



### FPR = TP/(TN+FP)
### TPR / Recall = TP/(TP+FN)
###  Precision = TP/(TP+FP)

##### ROC-AUC does not work well under severe imbalance in the dataset because Denominator of FPR has a True Negatives as one factor since Negative Class is in majority the denominator of FPR is dominated by True Negatives which makes FPR less sensitive to any changes in minority class predictions. To overcome this, Precision-Recall Curves are used instead of ROC and then the AUC is calculated


## Result and Discussions
1. The target dataset is completely imbalanced which again proves the call for precision/recall.
2. There are number of client who are/may default next month are not considered. 
3. After cosidering f-1 score in grid search cv, we have increased value of FP and FN and also decreased TN.
4. Decrease in TN shows that number of minority class has been predicted correctly into FP or FP.


## Architecture
**Model Training / Validation Workflows**

![image](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/391d30d5-64c5-4a3a-905a-63d8f2f6c17d)

**User I/O Workflow**

![image](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/50a40d63-692c-4814-b99d-a0b56c7d11a4)

# DEPLOYMENT LINKS:
**Welcome Page**
http://54.210.37.138:5000

**Prediction/ Result Page**
http://54.210.37.138:5000/predictdata

## Wireframes
**Index/Welcome Page**

This page will provide the index, necessary information like meta-data, other details can be mentioned about the project. We don’t have any option for user input here.
The page will look like following:

![image](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/b8a2ee7b-aa74-47fb-a687-7615763c7264)

**Home Page**

On proceeding to the home page, we will encounter a form which will request to fill the necessary input or select from the drop down from the user. The form will also guide to different types of values and their imitations.
The home page will be in following format:

![image](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/ee07538b-cdc2-456b-9c4e-f91c85362741)

On click of Submission or Predict Default button in home page after filling the details it will provide the predicted result. 

![image](https://github.com/ayan-zz/credit-card-vr0.0.2/assets/64850346/d20d4b26-5a19-4fab-a093-aa2cc5d4e99d)
