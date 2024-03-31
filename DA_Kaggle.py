import pandas as pd
import matplotlib as plt


#讀入csv
data_df = pd.read_csv("./DA Kaggle 專案/US_Accidents_Dec21_updated.csv")
print(data_df.info())

"""
#刪除沒用column
invoice_data_df = invoice_data_df.drop("Unnamed: 9" ,axis=1).drop('Unnamed: 10',axis=1)

#刪除Na值
invoice_data_df =invoice_data_df.dropna()

#將年的資料型態改成int
invoice_data_df["年"] = invoice_data_df["年"].astype("int")

#刪除重複值
invoice_data_df = invoice_data_df.drop_duplicates()

#確認年份正確
invoice_data_df = invoice_data_df.drop(invoice_data_df[invoice_data_df["年"]>2021].index)
invoice_data_df = invoice_data_df.drop(invoice_data_df[invoice_data_df["年"]<2018].index)

#確認月份正確
invoice_data_df = invoice_data_df.drop(invoice_data_df[invoice_data_df["月"]<1].index)
invoice_data_df = invoice_data_df.drop(invoice_data_df[invoice_data_df["月"]>12].index)


#離群值檢驗
data_amount = invoice_data_df["電子發票張數"].to_numpy()
data_total = invoice_data_df["電子發票金額"].to_numpy()
q1_amount,q3_amount = np.percentile(data_amount, (25, 75))
IQR_amount = q3_amount - q1_amount
q1_total,q3_total = np.percentile(data_total, (25, 75), interpolation='midpoint')
IQR_total = q3_total - q1_total
amount_MAX = q3_amount + 1.5 * IQR_amount
amount_min = q1_amount - 1.5 * IQR_amount
total_MAX = q3_total + 1.5 * IQR_total
total_min = q1_total - 1.5 * IQR_total

print(invoice_data_df["電子發票張數"].sort_values(ascending=False,ignore_index=True).head(20))
print(invoice_data_df["電子發票金額"].sort_values(ascending=False,ignore_index=True).head(20))
"""
#讀入行業別對照
industry_category_data = pd.read_csv("./DA幹部專案/industry_category.csv")

#合併
final_data = pd.merge(invoice_data_df, industry_category_data,on="行業別")

#輸出
final_data.to_csv("final_data.csv")

#print(invoice_data_df.head())
print(invoice_data_df.info())