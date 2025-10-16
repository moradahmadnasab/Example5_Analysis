import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Original data
data2 = {
    'Problem size': ['50','100','150','200','250', '300'],
    '$N^{OSDR1}$': [12,11,16,12,10,13],
    '$N^{RSSEP1}$': [8,10,10,14,11,10],
    '$N^{OSDR2}$': [5,14,17,13,18,18],
    '$N^{RSSEP2}$': [9,14,11,17,17,15],
    '$N^{CQR}$': [5,7,8,8,8,8],
    '$N^{QZ}$': [25,8,2,0,0,0]
}

df2 = pd.DataFrame(data2)
print("Original table:")
print(df2)

# Unpivot (melt)
df_unpivot2 = pd.melt(df2, id_vars='Problem size', 
                      var_name='Method', value_name='Value')
print("\nUnpivoted table:")
print(df_unpivot2)

# Visualization
sns.barplot(data=df_unpivot2, x='Problem size', y='Value', hue='Method')
plt.title("Comparison of Iteration Counts for Different Methods")
plt.tight_layout()
plt.show()
