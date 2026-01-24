import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
import numpy as np

# configure default display
pd.options.display.max_rows = 100

# read csv file
df = pd.read_csv("streamworks_user_data.csv")
print(df.head())
# print(df.value_counts())
# information about the csv
df.info()
# check for NAN values
print(f"This are the columns that contain null values \n", df.isnull().sum())

# fill up empty column
# to identity which rows of user_id isnull
print(df[df['user_id'].isna()])


# 2a
# convert signup_date, last_active_date to datetime


def process_dates(df, signup_col='signup_date', last_active_col='last_active_date'):
    """
   Cleans date columns and converts them to DD-MM-YYYY format (datetime).
   Handles mixed date formats like '01-01-2026 and 01/01/2026' .

   Returns:
       df with cleaned date columns
       convert to datetime, try multiple formats, fall back to dateutil
   """

    for col in [signup_col, last_active_col]:
        df[col] = pd.to_datetime(df[col], format='%d-%m-%y', errors='coerce', dayfirst=False).dt.floor('D')
        """ Optional: check for rows that couldn't be parsed 
    parsed :analyse (a string or text) into logical syntactic components."""
        if df[col].isna().sum() > 0:
            print(f"Warning: {df[col].isna().sum()} rows in '{col}' could not be parsed and are set as NaT.")

    return df


print(process_dates(df))
print(df[['signup_date', 'last_active_date']].head())

# using a dict to fill up the values for user_id
print(df[df['user_id'].isna()])
replacements = {56: 1057, 886: 1887}

fill_values = {
    'user_id': replacements,
    'age': df['age'].mean(),
    'gender': 'Male',
    'signup_date': '15-09-23',
    'last_active_date': '13-07-25',
    'country': "USA",
    'subscription_type': 'Premium',
    'average_watch_hours': df['average_watch_hours'].median(),
    'mobile_app_usage_pct': df['mobile_app_usage_pct'].mean(),
    'complaints_raised': df['complaints_raised'].mean(),
    'received_promotions': 'No',
    'referred_by_friend': 'Yes',
    'is_churned': df['is_churned'].median(),
    'monthly_fee': df['monthly_fee'].mean()
}

df = df.fillna(fill_values)
print(df.isnull().sum())
print(df['last_active_date'].dtypes)
# One - Hot Encoding for gender
dummies = pd.get_dummies(df['gender'], prefix='gender', drop_first=False)
dummies = dummies.astype(int)
df = pd.concat([df, dummies], axis=1)
print("datatype: ", df['gender_Male'].dtypes)

# creating Ordinal Encoder()
encoder = OrdinalEncoder(categories=[['Basic', 'Standard', 'Premium']])
df['subscription_type_E'] = encoder.fit_transform(df[['subscription_type']])
print(df[['subscription_type', 'subscription_type_E']].tail())

# creating Label Encoder() for received_promotions
le = LabelEncoder()
values = df['received_promotions'].values
df['received_promotions_L'] = le.fit_transform(values)
print(df[['received_promotions', 'received_promotions_L']].head())

# creating Label Encoder() for referred_by_friend
values = df['referred_by_friend'].values
df['referred_by_friend_l'] = le.fit_transform(values)
print(df[['referred_by_friend', 'referred_by_friend_l']].head())

# creating new features tenure_days
df['tenure_days'] = (df['last_active_date'] - df['signup_date']).dt.days
print(df['tenure_days'].head())

#  Normalization : It puts data on a common scale.
#  watch time per day
df["watch_time"] = df["average_watch_hours"] / df["tenure_days"]

# creating new features is_loyal
df['is_loyal'] = df['tenure_days'] > 180
print(df['is_loyal'].tail())

# creating Label Encoder() for is_loyal
values = df['is_loyal'].values
df['is_loyal_l'] = le.fit_transform(values)
print(df[['is_loyal', 'is_loyal_l']].head())

# Normalization : It puts data on a common scale.
# creating new features watch_per_fee_ratio
df['watch_per_fee_ratio'] = df['average_watch_hours'] / df['monthly_fee']
print(df['watch_per_fee_ratio'].tail())


# creating new features heavy_mobile_user
df['heavy_mobile_user'] = df['mobile_app_usage_pct'] * df['tenure_days']
print(df['heavy_mobile_user'].tail())

# mobile dominant users
# to know if mobile dominant users are more likely to cancel
df['mobile_dominant'] = \
    pd.qcut(df['mobile_app_usage_pct'], q=3, labels=['low', 'medium', 'high'])
print(df.groupby('mobile_dominant', observed=False)['is_churned'].mean())

# Standardization
# Transforming data to common scale with zero mean and unit variance
# Centers and scales the data so that it has mean 0 and standard deviation 1.
scaler = StandardScaler()
df[['watch_per_fee_ratio_S']] = scaler.fit_transform(df[['watch_per_fee_ratio']])
print(df[['watch_per_fee_ratio', 'watch_per_fee_ratio_S']].tail())


# Discretisation / Binding by Age


def Binding_Interaction(dfd):
    # Discretisation / Binding by Age and  watch_per_fee_ratio
    # turn numbers into meaningful groups
    age_bins = [0, 20, 40, 70]
    age_label = ['Teen', 'Adult', 'Old']
    dfd['age group'] = pd.cut(dfd['age'], bins=age_bins, labels=age_label)

    watch_bins = [0, 0.5, 1.0, dfd['watch_per_fee_ratio'].max()]
    watch_labels = ['Low', 'Medium', 'High']
    dfd['watch_time_group'] = pd.cut(dfd['watch_per_fee_ratio'], bins=watch_bins, labels=watch_labels)

    # Interaction Features: when received_promotions and watch_time_group are both true

    dfd['promo_low_watch'] = ((dfd['received_promotions_L'] == 1) & (dfd['watch_time_group'] == 'Low')).astype(int)

    return dfd


df = Binding_Interaction(df)
print(df)

# Drop redundant or low-variance features
Redundant_features = ['watch_per_fee_ratio', 'mobile_app_usage_pct', 'last_active_date', 'signup_date']
df = df.drop(columns=Redundant_features)

# to check if columns what dropped
if 'watch_per_fee_ratio' in df.columns:
    print(df['watch_per_fee_ratio'])
else:
    print("Column was dropped")

# Using chi-square check relationship between
# is_churned and gender
table = pd.crosstab(df['gender'], df['is_churned'])
chi1, p, dof, expected = chi2_contingency(table)
print("Chi_square", chi1)
print("p-value:", p)
# plotting the table for chi_square
table.plot(kind='bar', stacked=True)
plt.title('Gender vs Churn')
plt.xlabel("Gender")
plt.ylabel("churned Users")
plt.legend(title='Churn')
plt.show()

# is_churned and recieved_promotions , referred_by_friend
table1 = pd.crosstab(df['received_promotions'], df['is_churned'])
chi2, p, dof, expected = chi2_contingency(table1)
print("Chi_square", chi2)
print("p-value:", p)

# plotting the table for chi_square
table1.plot(kind='bar', stacked=True)
plt.title('received_promotions vs Churn')
plt.xlabel("received_promotions")
plt.ylabel("churned Users")
plt.legend(title='Churn')
plt.show()

table2 = pd.crosstab(df['referred_by_friend'], df['is_churned'])
chi3, p, dof, expected = chi2_contingency(table2)
print("Chi_square", chi3)
print("p-value:", p)
table2.plot(kind='bar', stacked=True)
plt.title('referred_by_friend  vs Churn')
plt.xlabel("referred_by_friend")
plt.ylabel("churned Users")
plt.legend(title='Churn')
plt.show()

# t-test to check if watch time
# differs significantly between churned and retained users
group_churned = df[df["is_churned"] == 1]['watch_time']
group_retained = df[df["is_churned"] == 0]['watch_time']

t_stat, p_value = ttest_ind(group_churned, group_retained, equal_var=False)

mean_churned = group_churned.mean()
mean_retained = group_retained.mean()
print(f"Average customers that churned , {mean_churned:.2f}")
print(f"Average customers that is Active, {mean_retained:.2f}")
print(f"t_test value:, {t_stat:.2f}")
print(f"Probability of t_test, {p_value:.4f}")

plt.figure(figsize=(6, 4))
sns.boxplot(x='is_churned', y="watch_time", data=df)
plt.xlabel("churn status (0 =Not churned, 1= churned)")
plt.ylabel("watch_time")
plt.title("watch time by Churn Status")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(group_churned, kde=True, label='Is_churned')
sns.histplot(group_retained, kde=True, label='Active')
plt.xlabel("Watch Time")
plt.ylabel("Count")
plt.legend()
plt.show()

# correlation Analysis
numerical_cols = df.select_dtypes(include='number').columns

# Correlation matrix
corr_matrix = df[numerical_cols].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.show()


""" Predicting Analysis - using Logistic Regression & Standardization 
 for binary classification (categories)
"""
# Split the data
x = df[['referred_by_friend_l', 'received_promotions_L', 'subscription_type_E', 'is_loyal_l',
        'gender_Male', 'gender_Female', 'gender_Other', 'complaints_raised']]

y = df['is_churned']

x_train, x_test, y_train, y_test =\
    train_test_split(x, y, test_size=0.2, random_state=42)

# Reason for standardization
# All features have mean = 0, std = 1
# Coefficients(Numbers ) become comparable
scaler = StandardScaler()
# Mean and std come only from training data
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.fit_transform(x_test)

# Logistic Regression
model = LogisticRegression(class_weight='balanced')
# learn this pattern (Train)
model.fit(x_train_scaler, y_train)

# predict unknown labels
Predict = model.predict(x_test_scaler)
# predicted probabilities for the positive class (churned )
Predict_proba = model.predict_proba(x_test_scaler)[:, 1]
print(Predict_proba.max())
print("Binary Classification :", Predict)
print("Binary Classification for Probability :", Predict_proba)

# confusion matrix  show  how well your binary classification model predicted
# the features of  customer churning


confusion_matrixF = confusion_matrix(y_test, Predict)
print("confusion_matrix :", confusion_matrixF)

# give out Precision, Recall , F1-score , Support
print("Classification Report")
print(classification_report(y_test, Predict, zero_division=0))

# ROC - Receiver Operating Characteristic Curve
# this show how well a binary classification model separates
# the two class (churn and not churn)

fpr, tpr, thresholds = roc_curve(y_test, Predict_proba)

auc_score = roc_auc_score(y_test, Predict_proba)
print(f"AUC= Area Under the ROC :{auc_score}")

# plot ROC curve
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

# Train a linear regression model
# to predict tenure_days using monthly_fee

x = df[['subscription_type_E', 'age', "watch_time"]]
y = df['tenure_days']
tran_Y = np.log(y)
print(tran_Y.mean())
model = LinearRegression()
x_train, x_test, y_train, y_test = \
    train_test_split(x, tran_Y, test_size=0.2, random_state=42)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Train a linear regression model:")
print("to predict tenure_days using monthly_fee")
print(y_pred)


# Getting variation in Predicted tenure_days  is explained
# from actual label used to evaluate the model (y_test)

r2 = r2_score(y_test, y_pred)

# Getting the Average size of prediction error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R Squared :", r2)
print("Root Mean Square error:", rmse)

residuals = y_test - y_pred
plt.figure()
plt.scatter(y_pred, residuals)
plt.axhline(y=0)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()






