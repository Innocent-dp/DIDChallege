import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Loading and storing LinkedIn data
file_path = r"temp_datalab_records_linkedin_company.csv"
df = pd.read_csv(file_path)

df['as_of_date'] = pd.to_datetime(df['as_of_date'], infer_datetime_format=True)
df['date_added'] = pd.to_datetime(df['date_added'], infer_datetime_format=True)

df_old = df.copy()
print(df_old.shape)
df.drop_duplicates(subset ="company_name", 
                     keep = 'last', inplace = True)


#Creating and plotting relationship between company and employees on LinkedIn
comp = df['company_name'].values

empl = df['employees_on_platform'].values

sorted_empl_idx = np.argsort(empl)
sorted_empl = empl[sorted_empl_idx]
sorted_comp = comp[sorted_empl_idx]
sorted_comp_idx = np.arange(sorted_comp.shape[0]).reshape(sorted_comp.shape)


plt.plot(sorted_comp_idx, sorted_empl)
plt.show()

print("Companies with highest employees on LinkedIn: \n{}" .format(sorted_comp[-5:]))
print("\nCompanies with lowest employees on LinkedIn: \n{}" .format(sorted_comp[0:5]))


#Creating and plotting relationship between company and followers on LinkedIn
comp = df['company_name'].values
fol = df['followers_count'].values
sorted_fol_idx = np.argsort(fol)
sorted_fol = empl[sorted_fol_idx]
sorted_comp = comp[sorted_fol_idx]
sorted_comp_idx = np.arange(sorted_comp.shape[0]).reshape(sorted_comp.shape)


plt.plot(sorted_comp_idx, sorted_fol)
plt.show()

print("Companies with highest followers: \n{}" .format(sorted_comp[-5:]))
print("\nCompanies with lowest followers: \n{}" .format(sorted_comp[0:5]))
