import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
import seaborn as sns
from datetime import date
from datetime import datetime

def dataframe():
    df = pd.read_csv('coffee-shop-sales-revenue.csv')
    transaction_id = []
    transaction_date = []
    transaction_time =[] 
    transaction_qty =[]
    store_id =[]
    store_location =[]
    product_id =[]
    unit_price =[]
    product_category =[]
    product_type =[]
    product_detail =[]

    for i in range(0,df.shape[0]):
        l = df.iloc[i,0].split("|")
        transaction_id.append(l[0])
        transaction_date.append(l[1])
        transaction_time.append(l[2])
        transaction_qty.append(l[3])
        store_id.append(l[4])
        store_location.append(l[5])
        product_id.append(l[6])
        unit_price.append(l[7])
        product_category.append(l[8])
        product_type.append(l[9])
        product_detail.append(l[10])


    dic = {
        "transaction_id" :transaction_id,
        "transaction_date" :transaction_date,
        "transaction_time" :transaction_time,
        "transaction_qty" :transaction_qty,
        "store_id" :store_id,
        "store_location" :store_location,
        "product_id" :product_id,
        "unit_price" :unit_price,
        "product_category" :product_category,
        "product_type" :product_type,
        "product_detail" :product_detail
    }

    df = pd.DataFrame(dic)

    ## Transforming Date and time column

    df['transaction_time']= pd.to_datetime(df['transaction_time'], format='%H:%M:%S')
    df['transaction_date']=pd.to_datetime(df['transaction_date'])

    ## Year month and day


    df['transaction_day'] = df['transaction_date'].dt.day_name()
    df['transaction_month'] = df['transaction_date'].dt.month
    df['transaction_year'] = df['transaction_date'].dt.year

    ## hours minutes and seconds

    df['transaction_hour'] = df['transaction_time'].dt.hour
    df['transaction_minute'] = df['transaction_time'].dt.minute
    df['transaction_second'] = df['transaction_time'].dt.second

    ## Total revenue per transaction

    df['transaction_qty']=df['transaction_qty'].apply(float)
    df['unit_price']=df['unit_price'].apply(float)

    df['Total_revenue'] = df['transaction_qty'] * df['unit_price']
    return df

df= dataframe()

## Transactions by day and Months

def transactions_and_items_sold_per_location():

    items_sold_per_loc=df.groupby('store_location')['transaction_qty'].sum()
    transactions_per_loc=df['store_location'].value_counts()
    return transactions_per_loc,items_sold_per_loc

def revenu_by_store_location():
    total_revenu_per_loc=df.groupby("store_location")['Total_revenue'].sum()
    return total_revenu_per_loc


def top_product_categories():
    quantity_per_category=df.groupby("product_category")['transaction_qty'].sum().sort_values(ascending=False)
    transaction_per_category = df['product_category'].value_counts()
    return quantity_per_category,transaction_per_category

def top_product_type():
    quantity_per_type=df.groupby("product_type")['transaction_qty'].sum().sort_values(ascending=False)[:9]
    transaction_per_type = df['product_type'].value_counts()[:9]
    return quantity_per_type,transaction_per_type


def product_cat_quant_sold_per_loc():
    categorywise_locwise_quantSold = df.groupby(['store_location','product_category'])['transaction_qty'].sum().reset_index().sort_values(['store_location', 'transaction_qty'], ascending=[True, False])
    return categorywise_locwise_quantSold

def expensive_product():
    product_price=df.groupby("product_type")['unit_price'].mean().sort_values(ascending=False)
    return product_price

def revenue_by_product_category():
    revenue_by_category=df.groupby('product_category')['Total_revenue'].sum().sort_values(ascending=False)
    return revenue_by_category

def revenue_by_product_type():
    revenue_by_type=df.groupby('product_type')['Total_revenue'].sum().sort_values(ascending=False)
    return revenue_by_type

def revenue_by_category_per_location():
    rev=df.groupby(["store_location","product_category"])['Total_revenue'].sum().reset_index().sort_values(['store_location','Total_revenue'],ascending=[True,False])
    return rev
def hourly_revenue_in_each_location():
    hourly_revenue=df.groupby(["transaction_hour","store_location"])['Total_revenue'].sum().reset_index().sort_values(['store_location','Total_revenue'],ascending=[True,False])
    return hourly_revenue

def total_revenue_trend():
    revenu_trend=df.groupby('transaction_date')['Total_revenue'].sum().reset_index()
    return revenu_trend

def correlation():
    corr = df[['transaction_qty', 'unit_price', 'Total_revenue']].corr(method='spearman')
    return corr