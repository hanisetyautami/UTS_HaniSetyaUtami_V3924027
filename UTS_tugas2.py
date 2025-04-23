#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Membaca dataset ---
df = pd.read_excel("loan_data_set.xlsx", sheet_name="loan_data_set")

# --- 2. Visualisasi Distribusi (Bagian A) ---
sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# a. Status Pernikahan
sns.countplot(data=df, x='Married', ax=axes[0, 0], palette='pastel')
axes[0, 0].set_title('Distribusi Berdasarkan Status Pernikahan')

# b. Jumlah Tanggungan
sns.countplot(data=df, x='Dependents', ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Distribusi Berdasarkan Jumlah Tanggungan')

# c. Wilayah Properti
sns.countplot(data=df, x='Property_Area', ax=axes[1, 0], palette='muted')
axes[1, 0].set_title('Distribusi Berdasarkan Wilayah Properti')

# d. Pendapatan Pemohon
sns.histplot(df['ApplicantIncome'], bins=30, ax=axes[1, 1], kde=True, color='skyblue')
axes[1, 1].set_title('Distribusi Pendapatan Pemohon')

plt.tight_layout()
plt.show()

# --- 3. Probabilitas Persetujuan Pinjaman berdasarkan Pendidikan (Bagian B) ---
edu_loan_status = pd.crosstab(df['Education'], df['Loan_Status'], normalize='index')

edu_loan_status.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(8,6))
plt.title("Probabilitas Persetujuan Pinjaman berdasarkan Jenis Pendidikan")
plt.ylabel("Proporsi")
plt.xlabel("Pendidikan")
plt.legend(title="Status Pinjaman", labels=["Ditolak (N)", "Disetujui (Y)"])
plt.tight_layout()
plt.show()


# In[ ]:




