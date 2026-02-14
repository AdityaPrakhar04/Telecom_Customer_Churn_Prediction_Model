import streamlit as st
import pandas as pd
import pickle
from feature_engineering import FeatureEngineering

st.set_page_config(page_title="Churn Prediction App",layout="centered")
st.title("Churn Prediction App")
st.write("Predict whether the customer will churn or not by providing the customer details below-->")

def load_model():
    return pickle.load(open("churn_model.pkl","rb"))
model=load_model()

with st.form("Customer Form"):
    gender=st.selectbox("Gender",["Male","Female"])
    age=st.number_input("Age",min_value=18,max_value=100)
    married=st.selectbox("Married",["Yes","No"])
    number_of_dependents=st.number_input("Number of Dependents",min_value=0)
    zip_code=st.number_input("Zip Code")
    latitude=st.number_input("Latitude")
    longitude=st.number_input("Longitude")
    number_of_referrals=st.number_input("Number Of Referrals")
    tenure_in_months=st.number_input("Tenure In Months")
    offer=st.selectbox("Offer",["Offer A","Offer B","Offer C","Offer D","Offer E"])
    phone_service=st.selectbox("Phone Service",["Yes","No"])
    avg_monthly_long_distance_charges=st.number_input("Avg Monthly Long Distance Charges")
    multiple_lines=st.selectbox("Multiple Lines",["Yes","No"])
    internet_service=st.selectbox("Internet Service",["Yes","No"])
    internet_type=st.selectbox("Internet Type",["Fiber Optic","DSL","Cable"])
    average_monthly_gb_download=st.number_input("Avg Monthly GB Download")
    online_security=st.selectbox("Online Security",["Yes","No"])
    online_backup=st.selectbox("Online Backup",["Yes","No"])
    device_protection_plan=st.selectbox("Device Protection Plan",["Yes","No"])
    premium_tech_support=st.selectbox("Premium Tech Support",["Yes","No"])
    streaming_tv=st.selectbox("Streaming TV",["Yes","No"])
    streaming_movies=st.selectbox("Streaming Movies",["Yes","No"])
    streaming_music=st.selectbox("Streaming Music",["Yes","No"])
    unlimited_data=st.selectbox("Unlimited Data",["Yes","No"])
    contract=st.selectbox("Contract",["Month-to-Month","One Year","Two Year"])
    paperless_billing=st.selectbox("Paperless Billing",["Yes","No"])
    payment_method=st.selectbox("Payment Method",["Bank Withdrawal","Credit Card","Mailed Check"])
    monthly_charge=st.number_input("Monthly Charge")
    total_charges=st.number_input("Total Charges")
    total_refunds=st.number_input("Total Refunds")
    total_extra_data_charges=st.number_input("Total Extra Data Charges")
    total_long_distance_charges=st.number_input("Total Long Distance Charges")
    total_revenue=st.number_input("Total Revenue")

    submit=st.form_submit_button("Predict")

if submit:
    input_df=pd.DataFrame([{"Gender":gender,"Age":age,"Married":married,"Number of Dependents":number_of_dependents,"Zip Code":zip_code,"Latitude":latitude,"Longitude":longitude,"Number of Referrals":number_of_referrals,"Tenure in Months":tenure_in_months,"Offer":offer,"Phone Service":phone_service,"Avg Monthly Long Distance Charges":avg_monthly_long_distance_charges,"Multiple Lines":multiple_lines,"Internet Service":internet_service,"Internet Type":internet_type,"Avg Monthly GB Download":average_monthly_gb_download,"Online Security":online_security,"Online Backup":online_backup,"Device Protection Plan":device_protection_plan,"Premium Tech Support":premium_tech_support,"Streaming TV":streaming_tv,"Streaming Movies":streaming_movies,"Streaming Music":streaming_music,"Unlimited Data":unlimited_data,"Contract":contract,"Paperless Billing":paperless_billing,"Payment Method":payment_method,"Monthly Charge":monthly_charge,"Total Charges":total_charges,"Total Refunds":total_refunds,"Total Extra Data Charges":total_extra_data_charges,"Total Long Distance Charges":total_long_distance_charges,"Total Revenue":total_revenue}])
    
    prediction=model.predict(input_df)[0]

    if prediction == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is not likely to Churn")
