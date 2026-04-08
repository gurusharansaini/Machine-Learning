import streamlit as st
import helper
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("Sales Tredn Analysis")


st.sidebar.markdown("""
- [GitHub](https://github.com/gurusharansaini/Machine-Learning/blob/main/ML%20PROJECTS/PROJECT%203/Untitled.ipynb)
- [1. Transactions by Hour](#1)
- [2. Items Sold per Month](#2)
- [3. Transactions and Items sold per Store Location](#3)
- [4. Total Revenue by Store Location](#4)
- [5. Top Product Categories: Transactions vs Quantity Sold](#5)
- [6. Top Product Types: Transactions vs Quantity Sold](#6)
- [7. Product Category Quantity Sold per Store Location](#7)
- [8. Product Revenue Analysis](#8)
- [     8.1 Most Expensive Products on Average](#8.1)
- [     8.2 Revenue by product category](#8.2)
- [     8.3 Revenue by product type](#8.3)
- [     8.4 Revenue by product category in each store location](#8.4)
- [     8.5 Top 10 Products by: Revenue, Quantity Sold and Transactions](#8.5)
- [     8.6 Hourly Revenue in each Store Location](#8.6)
- [     8.7 Trend of Total Revenue Over Time](#8.7)
- [9. Relationship Between Unit Price, Transaction Quantity, and Total Revenue](#9)
""")

# Transaction by Houres ----------------------------------------------------------------------

st.markdown("<h1>1. Transactions by Hour </h1> <span id='1'></span>",unsafe_allow_html=True)

fig,ax= plt.subplots()

sns.countplot(data=helper.df,x="transaction_hour",color="deepskyblue",ax=ax)
st.pyplot(fig)

# 2. Items Sold per Month ----------------------------------------------------------------------

st.markdown("<h1>2. Items Sold per Month </h1> <span id='2'></span>",unsafe_allow_html=True)

fig,ax= plt.subplots()
a = sns.countplot(data=helper.df,x='transaction_month',color="deepskyblue",ax=ax)

a.set_xticks(range(6))
a.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun'])
st.pyplot(fig)



# 3. Transactions and Items sold per Store Location ----------------------------------------------------------------------
st.markdown("<h1>3. Transactions and Items sold per Store Location </h1> <span id='3'></span>",unsafe_allow_html=True)

transactions_per_loc,items_sold_per_loc =   helper.transactions_and_items_sold_per_location()

fig,ax= plt.subplots()
a=sns.barplot(x=transactions_per_loc.index,y=transactions_per_loc,color="deepskyblue",ax=ax)
# a.title("Transactions Per Stroe Location")
st.pyplot(fig)




fig,ax= plt.subplots()
a=sns.barplot(x=items_sold_per_loc.index,y=items_sold_per_loc,color="deepskyblue",ax=ax)
# a.title("Items sold Each store location")
st.pyplot(fig)

# 4. Total Revenue by Store Location ----------------------------------------------------------------------
st.markdown("<h1>4. Total Revenue by Store Location </h1> <span id='4'></span>",unsafe_allow_html=True)
total_revenu_per_loc = helper.revenu_by_store_location()

fig,ax= plt.subplots()
a=sns.barplot(x=total_revenu_per_loc.index,y=total_revenu_per_loc,color="deepskyblue",ax=ax)
st.pyplot(fig)

# 5. Top Product Categories: Transactions vs Quantity Sold ----------------------------------------------------------------------
st.markdown("<h1>5. Top Product Categories: Transactions vs Quantity Sold </h1> <span id='5'></span>",unsafe_allow_html=True)
quantity_per_category,transaction_per_category = helper.top_product_categories()

fig,ax= plt.subplots()
aa=sns.barplot(x=quantity_per_category.index,y=quantity_per_category,color="deepskyblue",ax=ax)
aa.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.title("Quantity sold per category")
st.pyplot(fig)

fig,ax= plt.subplots()
a=sns.barplot(x=transaction_per_category.index,y=transaction_per_category,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title("Transactions per category")
st.pyplot(fig)

# 6. Top Product Types: Transactions vs Quantity Sold ----------------------------------------------------------------------
st.markdown("<h1>6. Top Product Types: Transactions vs Quantity Sold </h1> <span id='6'></span>",unsafe_allow_html=True)
quantity_per_type,transaction_per_type = helper.top_product_type()

fig,ax= plt.subplots()
a=sns.barplot(x=quantity_per_type.index,y=quantity_per_type,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title("Quantity sold per Product Type")
st.pyplot(fig)


fig,ax= plt.subplots()
a=sns.barplot(x=transaction_per_type.index,y=transaction_per_type,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title("Transactions per Product Type")
st.pyplot(fig)

# 7. Product Category Quantity Sold per Store Location ----------------------------------------------------------------------
st.markdown("<h1>7. Product Category Quantity Sold per Store Location </h1> <span id='8.7'></span>",unsafe_allow_html=True)
categorywise_locwise_quantSold = helper.product_cat_quant_sold_per_loc()
fig,ax= plt.subplots()
sns.barplot(x='store_location', y='transaction_qty', data=categorywise_locwise_quantSold, hue='product_category', palette='Blues',ax=ax)
st.pyplot(fig)

# 8. Product Revenue Analysis ----------------------------------------------------------------------
# 8.1 Expensive Products on Average ----------------------------------------------------------------------
st.markdown("<h1>8.1 Expensive Products on Average </h1> <span id='8.1'></span>",unsafe_allow_html=True)
product_price = helper.expensive_product()
fig,ax= plt.subplots()
a=sns.barplot(x=product_price.index,y=product_price,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(),rotation=90)
st.pyplot(fig)
# 8.2 Revenue by product category ----------------------------------------------------------------------
st.markdown("<h1>8.2 Revenue by product category </h1> <span id='8.2'></span>",unsafe_allow_html=True)
revenue_by_category = helper.revenue_by_product_category()
fig,ax= plt.subplots()
a=sns.barplot(x=revenue_by_category.index,y=revenue_by_category,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(),rotation=90)
st.pyplot(fig)

# 8.3 Revenue by product type----------------------------------------------------------------------
st.markdown("<h1>8.3 Revenue by product type </h1> <span id='8.3'></span>",unsafe_allow_html=True)
revenue_by_type = helper.revenue_by_product_type()
fig,ax= plt.subplots()
a=sns.barplot(x=revenue_by_type.index,y=revenue_by_type,color="deepskyblue",ax=ax)
a.set_xticklabels(ax.get_xticklabels(),rotation=90)
st.pyplot(fig)


# 8.4 Revenue by product category in each store location ----------------------------------------------------------------------
st.markdown("<h1>8.4 Revenue by product category in each store location </h1> <span id='8.4'></span>",unsafe_allow_html=True)
rev= helper.revenue_by_category_per_location()
fig,ax= plt.subplots()
sns.barplot(data=rev,x="store_location",y="Total_revenue",hue="product_category",palette='Purples',ax=ax)
st.pyplot(fig)



# 8.5 Top 10 Products by: Revenue, Quantity Sold and Transactions----------------------------------------------------------------------

# st.markdown("8.5 Top 10 Products by: Revenue, Quantity Sold and Transactions")


# 8.6 Hourly Revenue in each Store Location----------------------------------------------------------------------
st.markdown("<h1>8.6 Hourly Revenue in each Store Location </h1> <span id='8.6'></span>",unsafe_allow_html=True)
hourly_revenue = helper.hourly_revenue_in_each_location()
fig,ax= plt.subplots()
sns.barplot(x='transaction_hour', y='Total_revenue', hue='store_location', data=hourly_revenue, palette='Blues',ax=ax)
st.pyplot(fig)



# 8.7 Trend of Total Revenue Over Time----------------------------------------------------------------------
# st.markdown("8.7 Trend of Total Revenue Over Time")

st.markdown(
    "<h1>8.7 Trend of Total Revenue Over Time </h1> <span id='8.7'></span>",
    unsafe_allow_html=True
)
revenu_trend = helper.total_revenue_trend()
fig,ax= plt.subplots()
sns.lineplot(data=revenu_trend,x="transaction_date",y="Total_revenue",ax=ax)
st.pyplot(fig)




# 9. Relationship Between Unit Price, Transaction Quantity, and Total Revenue----------------------------------------------------------------------


st.markdown("<h1>9. Relationship Between Unit Price, Transaction Quantity, and Total Revenue</h1><span id='9'></span>",unsafe_allow_html=True)
corr = helper.correlation()
fig,ax= plt.subplots()
sns.heatmap(corr,cmap='Blues', fmt=".2f",annot=True)


st.pyplot(fig)

   