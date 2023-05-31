# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# import plotly.express as px
import numpy as np

############### Load eIF2a-p and OPP data ################
ImageInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/Image.csv')
ImageInfo_short = ImageInfo[['ImageNumber', 'Metadata_Site']]
ImageInfo_short.sort_values(by=['Metadata_Site'], inplace = True)
Time = [0, 0.5, 1, 2, 3] * 3
Time.sort()
Time = Time*3
ImageInfo_short['Metadata_time'] = Time
TimeNumber = [1, 2, 3, 4, 5] * 3
TimeNumber.sort()
TimeNumber = TimeNumber*3
ImageInfo_short['TimeNumber'] = TimeNumber


# Red cytoplasm and OPP cytoplasm share the same nucleus
CytRedIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/Red_Cytoplasm.csv')
CytRedIntensityInfo_short = CytRedIntensityInfo[['ImageNumber', 'Parent_Nuclei', 'Intensity_IntegratedIntensity_Red']]

TotOPPIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/OPP_whole_cell.csv')
TotOPPIntensityInfo_short = TotOPPIntensityInfo[['ImageNumber','Parent_Nuclei', 'Intensity_IntegratedIntensity_OPP']]

plt.rcParams['font.size'] = '21'
plt.rcParams.update({'font.family':'Helvetica'})
colors = ["#C3D9EE", "#87BDDC", "#4694C7", "#1460A7", "#07316E"]
my_cmap = mpl.colors.ListedColormap(colors, name="my_cmap")
norm = mpl.colors.Normalize(vmin=1, vmax=5)
############# Scatter plot of eIF2a-P and OPP (single cell) ###############
plt.figure(1)

RedOPP = CytRedIntensityInfo_short.merge(TotOPPIntensityInfo_short, how="left", on= ["ImageNumber", 'Parent_Nuclei'])
RedOPP = ImageInfo_short.merge(RedOPP, how="left", on= ["ImageNumber"])
x1 = RedOPP['Intensity_IntegratedIntensity_Red']
y1 = RedOPP['Intensity_IntegratedIntensity_OPP']

# https://matplotlib.org/stable/tutorials/colors/colorbar_only.html#sphx-glr-tutorials-colors-colorbar-only-py
plt.scatter(x1, y1, c=RedOPP['TimeNumber'], cmap=my_cmap)
# Plot 1D line of best fit using polyfit https://stackoverflow.com/questions/22239691/code-for-best-fit-straight-line-of-a-scatter-plot-in-python
slope1, intercept1 = np.polyfit(x1,y1,1)
# plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)), color = 'black', linewidth=2)
plt.ylabel('OP Puro Tot Intensity')
plt.xlabel('eIF2\u03B1-P Cyt Intensity')
# plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/OPP_eIF2aP.pdf', format='pdf', bbox_inches='tight', transparent=True)

# fig, ax = plt.subplots(figsize=(6, 1))
# fig.subplots_adjust(bottom=0.5)
# fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=my_cmap), cax=ax, orientation='horizontal', label='Time Number')

# plt.plot(RedOPP['Intensity_IntegratedIntensity_Red'], RedOPP['Intensity_IntegratedIntensity_OPP'])
# plt = px.scatter(RedOPP, x="Intensity_IntegratedIntensity_Red", y="Intensity_IntegratedIntensity_OPP")
# plt.show()

############# Scatter plot of eIF2a-P and OPP (mean) ###############
CytRedIntensityInfo_short = ImageInfo_short.merge(CytRedIntensityInfo_short, how="left", on= ["ImageNumber"])
'''make a list of the the mean for each Image Number from CytRedIntensityInfo_short in the Intensity column'''
mean_red = CytRedIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_Red'].mean().tolist()
'''make a list of the SEM for each Image Number from CytRedIntensityInfo_short in the Intensity column'''
sem_red = CytRedIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_Red'].sem().tolist()
# '''make a list of the 25 percentile for each Image Number from CytRedIntensityInfo_short in the Intensity column'''
# q25_red = CytRedIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_Red'].quantile(0.25).tolist()

TotOPPIntensityInfo_short = ImageInfo_short.merge(TotOPPIntensityInfo_short, how="left", on= ["ImageNumber"])
'''make a list of the mean for each Image Number from TotOPPIntensityInfo_short in the Intensity column'''
mean_opp = TotOPPIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_OPP'].mean().tolist()
'''make a list of the SEM for each Image Number from TotOPPIntensityInfo_short in the Intensity column'''
sem_opp = TotOPPIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_OPP'].sem().tolist()
# '''make a list of the 25 percentile for each Image Number from TotOPPIntensityInfo_short in the Intensity column'''
# q25_opp = TotOPPIntensityInfo_short.groupby('Metadata_time')['Intensity_IntegratedIntensity_OPP'].quantile(0.25).tolist()

plt.figure(2, figsize=(6.4, 4.8))
#x2 = ImageInfo_short['Mean_Red_Cytoplasm_Intensity_IntegratedIntensity_Red']
#y2 = ImageInfo_short['Mean_OPP_whole_cell_Intensity_IntegratedIntensity_OPP']

''' iterate across the points in mean_red plotting an errorbar plot for each point with the x and y as the mean_red and mean_opp and the xerr and yerr as the sem_red and sem_opp; set the color for each point to the entry from cmap'''
for i in range(len(mean_red)):
    plt.errorbar(mean_red[i], mean_opp[i], xerr=sem_red[i], yerr=sem_opp[i], fmt='o', color=colors[i], ecolor='lightgray', elinewidth=3, capsize=0)
    
#plt.scatter(x2, y2, c=ImageInfo_short['ImageNumber'], cmap=my_cmap)

slope2, intercept2 = np.polyfit(mean_red,mean_opp,1)
plt.plot(np.unique(mean_red), np.poly1d(np.polyfit(mean_red, mean_opp, 1))(np.unique(mean_red)), color = 'black', linewidth=2)
plt.ylabel('Mean OP Puro Tot Intensity')
plt.xlabel('Mean eIF2\u03B1-P Cyt Intensity')
'''prevent x axis title from being cut off'''
plt.tight_layout()
plt.show()
# plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/OPP_eIF2aP_MEAN.pdf', format='pdf', bbox_inches='tight', transparent=True)
