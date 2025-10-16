# ==============================================================
# Full Analysis: Best Performance Counts
# ==============================================================
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Data (number of times each method was best)
# -----------------------------
data2 = {
    'Problem size': ['50','100','150','200','250','300'],
    '$N^{OSDR1}$':[12,11,16,12,10,13],
    '$N^{RSSEP1}$':[8,10,10,14,11,10],
    '$N^{OSDR2}$':[5,14,17,13,18,18],
    '$N^{RSSEP2}$': [9,14,11,17,17,15],
    '$N^{CQR}$': [5,7,8,8,8,8],
    '$N^{QZ}$': [25,8,2,0,0,0]
}
df2 = pd.DataFrame(data2)

# -----------------------------
# 2. Ensure figures folder exists
# -----------------------------
os.makedirs('figures', exist_ok=True)

# -----------------------------
# 3. Global percentage across all problem sizes
# -----------------------------
method_totals = df2.drop(columns='Problem size').sum()
total_all = method_totals.sum()
percent_global = 100 * method_totals / total_all

# --- Bar chart: global percentage ---
plt.figure(figsize=(7,4))
sns.barplot(x=percent_global.index, y=percent_global.values)
plt.ylabel('Percentage of Best Performances (%)')
plt.xlabel('Method')
plt.title('Global Share of Best Performances Across All Problem Sizes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('figures/global_best_percentages.png', dpi=300, bbox_inches='tight')
plt.show()

print("=== Global percentage of best performances ===")
print(percent_global.round(2))

# -----------------------------
# 4. Per problem size percentage
# -----------------------------
df_percent = df2.copy()
cols = df_percent.columns[1:]  # method columns
df_percent[cols] = df_percent[cols].div(df_percent[cols].sum(axis=1), axis=0) * 100

# --- Stacked bar chart: per problem size ---
ax = df_percent.set_index('Problem size')[cols].plot(
    kind='bar',
    stacked=True,
    figsize=(8,5),
    colormap='tab20'
)
plt.ylabel('Percentage of Best Performances (%)')
plt.title('Distribution of Best Performances per Problem Size')
plt.legend(title='Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# --- Save the stacked chart ---
plt.savefig('figures/best_percent_per_size.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n=== Per problem size percentages ===")
print(df_percent.round(2))
