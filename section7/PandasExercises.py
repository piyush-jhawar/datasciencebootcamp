import pandas as pd

# sal = pd.read_csv('san-francisco-2011.csv')
# sal = pd.read_csv('Salaries.csv')
# print(sal.head())
# print(sal.info())
# print()
# print(sal['BasePay'].mean())
# print(sal['OvertimePay'].max())
# print(sal[sal.EmployeeName=='JOSEPH DRISCOLL']['JobTitle'])
# print(sal[sal.EmployeeName=='JOSEPH DRISCOLL']['TotalPayBenefits'])
# print(sal[sal.TotalPayBenefits==sal['TotalPayBenefits'].max()])
# print(sal[sal.TotalPayBenefits==sal['TotalPayBenefits'].min()])
# print(sal.groupby('Year')['BasePay'].mean())
# print(sal['JobTitle'].nunique())
# print()
# print(sal['JobTitle'].value_counts().head())
# saljobtitle2013 = sal[(sal['Year']==2013)]['JobTitle']
# # print((saljobtitle2013.value_counts()==1).index)
# # print(sum((saljobtitle2013.value_counts()==1).values))
# # print(sum(saljobtitle2013.value_counts()==1))
# # def chief_string(title):
# #     # print(title)
# #     if 'chief' in title.lower():
# #         return True
# #     else:
# #         return False
# #
# # # print(sum(sal['JobTitle'].apply(chief_string)))
# # print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))
#
# # def chief_string(title):
# #     if 'chief' in title.lower():
# #         return True
# #     else:
# #         return False
# #
# # print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))
#
# sal['title_len'] = sal['JobTitle'].apply(len)
# print(sal[['title_len','TotalPayBenefits']].corr())

ecom = pd.read_csv('Ecommerce Purchases.csv')
print(ecom.head())
print(ecom.info())
print(ecom['Purchase Price'].mean())
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())
# print(ecom[ecom['Language'] =='en'].count())
# print(ecom[ecom['Job'] =='Lawyer'].info())
print()
print(ecom.groupby('AM or PM').count())
print(ecom['Job'].value_counts().head())
print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])
print(ecom[ecom['Credit Card']==4926535242672853]['Email'])
print(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price'] > 95)].count())

def date_split(x):
    a,b = x.split('/')
    if int(b) == 25:
        return True

ecom['exp'] = ecom['CC Exp Date'].apply(date_split)
print(ecom['exp'].sum())
print()
print()
print()
print(ecom['Email'].apply(lambda x : x.split('@')[1]).value_counts().head())