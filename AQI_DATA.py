import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("data.csv")

df= data.query("index<31")

df = df.dropna()

import matplotlib.patches as mpatches

df.set_index("Day",inplace=True)
df.index= df.index.astype(str)

def get_color(aqi):
    if aqi <= 50:
        return 'green'     
    elif aqi <= 100:
        return 'yellow'     
    elif aqi <= 200:
        return 'orange'    
    elif aqi <= 300:
        return 'Salmon'       
    elif aqi <= 400:
        return 'red'     
    else:
        return 'purple'     
fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(30,21), sharex=True)


for i, month in enumerate(df.columns):
    colors = [get_color(aqi) for aqi in df[month]] 
    axes[i].bar(df.index, df[month], color=colors)
    axes[i].set_title(month)
    axes[i].set_ylabel('AQI')
    axes[i].tick_params(axis='x', rotation=90)  
    

legend_labels = {
    "Good (0-50)": "green",
    "Satisfactory (51-100)": "yellow",
    "Moderate (101-200)": "orange",
    "Poor (201-300)": "Salmon",
    "Very Poor (301-400)": "red",
    "Severe (401-500)": "purple"
}


legend_patches = [mpatches.Patch(color=color, label=label) for label, color in legend_labels.items()]

fig.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, 1.02), ncol=3, fontsize=12)

plt.xlabel('Day')

plt.tight_layout(rect=[0, 0, 1, 0.98])  

plt.show()

