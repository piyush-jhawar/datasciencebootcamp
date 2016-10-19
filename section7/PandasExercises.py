import pandas as pd

# sal = pd.read_csv('san-francisco-2011.csv')
sal = pd.read_csv('Salaries.csv')
print(sal.head())
print(sal.info())
print()
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal.EmployeeName=='JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal.EmployeeName=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal.TotalPayBenefits==sal['TotalPayBenefits'].max()])
print(sal[sal.TotalPayBenefits==sal['TotalPayBenefits'].min()])
print(sal.groupby('Year')['BasePay'].mean())
print(sal['JobTitle'].nunique())
print()
print(sal['JobTitle'].value_counts().head())
print()
print()
print()
print()
saljobtitle2013 = sal[(sal['Year']==2013)]['JobTitle']
# print((saljobtitle2013.value_counts()==1).index)
# print(sum((saljobtitle2013.value_counts()==1).values))
# print(sum(saljobtitle2013.value_counts()==1))