#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:07:31 2022

@author: angela_gao
"""
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import numpy as np
import seaborn as sns

ImageInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/Image.csv')
ImageInfo_short = ImageInfo[['ImageNumber', 'Metadata_Site']]
ImageInfo_short.sort_values(by=['Metadata_Site'], inplace = True)
Time = [0, 0.5, 1, 2, 3] * 3
Time.sort()
Time = Time*3
ImageInfo_short['Metadata_time'] = Time
Replicate = [1, 2, 3] * 15
Replicate.sort()
ImageInfo_short['Replicate'] = Replicate

# ######## Settings for Jess Microscope #########
# ImageInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/Jess_Microscope/072222/ImageAnalysis/Pipeline_07_26_22IF/GranuleInfo/All/Image.csv')
# ImageInfo_short = ImageInfo[['ImageNumber', 'Metadata_Site', 'Metadata_Well']] 
# # 150uM is Image Number 1-525; 300uM is Image Number 526-1050
# ImageInfo_short = ImageInfo_short.truncate(after=524)
# # Update time according to imaging
# Time = [0,1,2,3,4,5,6]*25
# Time.sort()
# Time = Time*3
# ImageInfo_short['Metadata_time'] = Time

############### Load eIF2a-p data ################
CytIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/Red_Cytoplasm.csv')
CytIntensityInfo_short = CytIntensityInfo[['ImageNumber', 'Intensity_IntegratedIntensity_Red']]
# TotIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/Jess_Microscope/072222/ImageAnalysis/Pipeline_07_26_22IF/GranuleInfo/All/Red_whole_cell.csv')
# TotIntensityInfo_short = TotIntensityInfo[['ImageNumber', 'Intensity_IntegratedIntensity_Red']]

################### Load OPP data #################
# CytOPPIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/ECHO_Revolve_Microscopy/Microscopy_08_03_22/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/OPP_Cytoplasm.csv')
# CytOPPIntensityInfo_short = CytOPPIntensityInfo[['ImageNumber', 'Intensity_IntegratedIntensity_OPP']]
TotOPPIntensityInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/Pipeline_08_03_22IF/GranuleInfo/OPP_whole_cell.csv')
TotOPPIntensityInfo_short = TotOPPIntensityInfo[['ImageNumber', 'Intensity_IntegratedIntensity_OPP']]

# Global Values
Metadata_Time_multiplier = 1 #60/60
plt.rcParams['font.size'] = '21'
plt.rcParams.update({'font.family':'Helvetica'})

CytIntensity_time = ImageInfo_short.merge(CytIntensityInfo_short, how="left", on= ["ImageNumber"])
CytIntensity_time.rename(columns={'Intensity_IntegratedIntensity_Red': 'eIF2a-P Cytoplasmic Intensity'}, inplace=True)
CytIntensity_time['Time (hr)'] = ((CytIntensity_time['Metadata_time']) * Metadata_Time_multiplier).round(1)
# TotIntensity_time = TotIntensityInfo_short.merge(ImageInfo_short, how="left", on= ["ImageNumber"])
# TotIntensity_time.rename(columns={'Intensity_IntegratedIntensity_Red': 'eIF2a-P Total Intensity'}, inplace=True)
# TotIntensity_time['Time (hr)'] = np.around((TotIntensity_time['Metadata_time']) * Metadata_Time_multiplier)

# CytOPPIntensity_time = ImageInfo_short.merge(CytOPPIntensityInfo_short, how="left", on= ["ImageNumber"])
# CytOPPIntensity_time.rename(columns={'Intensity_IntegratedIntensity_OPP': 'OPP Cytoplasmic Intensity'}, inplace=True)
# CytOPPIntensity_time['Time (hr)'] = ((CytOPPIntensity_time['Metadata_time']) * Metadata_Time_multiplier).round(1)
TotOPPIntensity_time = ImageInfo_short.merge(TotOPPIntensityInfo_short, how="left", on= ["ImageNumber"])
TotOPPIntensity_time.rename(columns={'Intensity_IntegratedIntensity_OPP': 'OPP Total Intensity'}, inplace=True)
TotOPPIntensity_time['Time (hr)'] = ((TotOPPIntensity_time['Metadata_time']) * Metadata_Time_multiplier).round(1)


# ############# Boxplot ###############
# # eIF2a-p Boxplot
# plt.figure(1)
# ax = sns.boxplot(x='Time (hr)', y='eIF2a-P Cytoplasmic Intensity', data=CytIntensity_time, color='cyan', width=0.6, fliersize=0)
# sns.stripplot(x='Time (hr)', y='eIF2a-P Cytoplasmic Intensity', data=CytIntensity_time, color='0', jitter=0.1, alpha=0.01)
# plt.ylabel('eIF2a-P Cyt Intensity')
# plt.xlabel('Time (hr)')
# plt.ylim(-10, 400)

# # OPP Boxplot
# # plt.figure(2)
# # ax = sns.boxplot(x='Time (hr)', y='OPP Cytoplasmic Intensity', data=CytOPPIntensity_time, color='lightcoral', width=0.6, fliersize=0)
# # sns.stripplot(x='Time (hr)', y='OPP Cytoplasmic Intensity', data=CytOPPIntensity_time, color='0', jitter=0.1, alpha=0.3)
# # plt.ylabel('OPP Cyt Intensity')
# # plt.ylim(0, 500)

# plt.figure(3)
# ax = sns.boxplot(x='Time (hr)', y='OPP Total Intensity', data=TotOPPIntensity_time, color='lightcoral', width=0.6, fliersize=0)
# sns.stripplot(x='Time (hr)', y='OPP Total Intensity', data=TotOPPIntensity_time, color='0', jitter=0.1, alpha=0.01)
# plt.ylabel('OPP Total Intensity')
# plt.ylim(0, 400)

# ############# Normalized Boxplot ###############
# CytIntensity = CytIntensity_time[['Time (hr)', 'eIF2a-P Cytoplasmic Intensity']]
# CytIntensityMedian_time = CytIntensity.groupby(['Time (hr)']).median()
# CytIntensityMedian_time = CytIntensityMedian_time.reset_index()
# InitCytIntensityMedian = CytIntensityMedian_time.loc[0, 'eIF2a-P Cytoplasmic Intensity']
# CytIntensity['eIF2a-P Cytoplasmic Intensity FC'] = CytIntensity['eIF2a-P Cytoplasmic Intensity']/InitCytIntensityMedian

# plt.figure(4)
# ax = sns.boxplot(x='Time (hr)', y='eIF2a-P Cytoplasmic Intensity FC', data=CytIntensity, color='cyan', width=0.6, fliersize=0)
# sns.stripplot(x='Time (hr)', y='eIF2a-P Cytoplasmic Intensity FC', data=CytIntensity, color='0', jitter=0.1, alpha=0.03)
# plt.ylabel('eIF2a-P Cyt Intensity FC')
# plt.xlabel('Time (hr)')
# plt.ylim(0, 13)

############### Lineplot ###############
# cytoplasmic eIF2a-P
CytIntensity_Well = CytIntensity_time[['Replicate','eIF2a-P Cytoplasmic Intensity', 'Time (hr)']]
CytIntensityMedian = CytIntensity_Well.groupby(['Replicate', 'Time (hr)']).median()
CytIntensityMedian = CytIntensityMedian.reset_index()
# # Determine median of each well (Jess Microscope)
# CytIntensity_Well = CytIntensity_time[['Metadata_Well', 'eIF2a-P Cytoplasmic Intensity', 'Time (hr)']]
# CytIntensityMedian = CytIntensity_Well.groupby(['Metadata_Well']).median()
# CytIntensityMedian = CytIntensityMedian.reset_index()
CytIntensityMedian = CytIntensityMedian[['Time (hr)', 'eIF2a-P Cytoplasmic Intensity']]
CytIntensityMEAN = CytIntensityMedian.groupby(['Time (hr)']).mean()
CytIntensityMEAN = CytIntensityMEAN.reset_index()
CytIntensitySEM = CytIntensityMedian.groupby(['Time (hr)']).sem()
CytIntensitySEM = CytIntensitySEM.reset_index()
CytIntensitySEM.rename(columns={'eIF2a-P Cytoplasmic Intensity': 'SEM'}, inplace=True)
# plt.figure(5)
# plt.errorbar(CytIntensityMEAN['Time (hr)'], CytIntensityMEAN['eIF2a-P Cytoplasmic Intensity'], yerr=CytIntensitySEM['SEM'], fmt='o--c', capsize=4, capthick=2, linewidth=2, markersize=7)
# plt.xlabel('Time (hr)')
# plt.ylabel('eIF2a-P Cyt Intensity')
# plt.ylim(0, 120)
# plt.xticks(CytIntensityMEAN['Time (hr)'], rotation=0)
# plt.xlabel('Time (hr)')

# Total OPP
TotOPPIntensity_Well = TotOPPIntensity_time[['Replicate','OPP Total Intensity', 'Time (hr)']]
TotOPPIntensityMedian = TotOPPIntensity_Well.groupby(['Replicate', 'Time (hr)']).median()
TotOPPIntensityMedian = TotOPPIntensityMedian.reset_index()
TotOPPIntensityMedian = TotOPPIntensityMedian[['Time (hr)', 'OPP Total Intensity']]
TotOPPIntensityMEAN = TotOPPIntensityMedian.groupby(['Time (hr)']).mean()
TotOPPIntensityMEAN = TotOPPIntensityMEAN.reset_index()
TotOPPIntensitySEM = TotOPPIntensityMedian.groupby(['Time (hr)']).sem()
TotOPPIntensitySEM = TotOPPIntensitySEM.reset_index()
TotOPPIntensitySEM.rename(columns={'OPP Total Intensity': 'SEM'}, inplace=True)

# ############### Normalized Lineplot ###############
# Cyt eIF2a-P
InitCytIntensity = CytIntensityMEAN.loc[0, 'eIF2a-P Cytoplasmic Intensity']
CytIntensityMedian['eIF2a-P Cytoplasmic Intensity FC'] = CytIntensityMedian['eIF2a-P Cytoplasmic Intensity']/InitCytIntensity
NormCytIntensityMedian = CytIntensityMedian[['Time (hr)', 'eIF2a-P Cytoplasmic Intensity FC']]
NormCytIntensityMEAN = NormCytIntensityMedian.groupby(['Time (hr)']).mean()
NormCytIntensityMEAN = NormCytIntensityMEAN.reset_index()
NormCytIntensitySEM = CytIntensityMedian.groupby(['Time (hr)']).sem()
NormCytIntensitySEM = NormCytIntensitySEM.reset_index()
NormCytIntensitySEM.rename(columns={'eIF2a-P Cytoplasmic Intensity FC': 'SEM'}, inplace=True)

# Total OPP
InitTotOPPIntensity = TotOPPIntensityMEAN.loc[0, 'OPP Total Intensity']
TotOPPIntensityMedian['OPP Total Intensity FC'] = TotOPPIntensityMedian['OPP Total Intensity']/InitTotOPPIntensity
NormTotOPPIntensityMedian = TotOPPIntensityMedian[['Time (hr)', 'OPP Total Intensity FC']]
NormTotOPPIntensityMEAN = NormTotOPPIntensityMedian.groupby(['Time (hr)']).mean()
NormTotOPPIntensityMEAN = NormTotOPPIntensityMEAN.reset_index()
NormTotOPPIntensitySEM = TotOPPIntensityMedian.groupby(['Time (hr)']).sem()
NormTotOPPIntensitySEM = NormTotOPPIntensitySEM.reset_index()
NormTotOPPIntensitySEM.rename(columns={'OPP Total Intensity FC': 'SEM'}, inplace=True)


# plt.figure(6)
# plt.errorbar(NormCytIntensityMEAN['Time (hr)'], NormCytIntensityMEAN['eIF2a-P Cytoplasmic Intensity FC'], yerr=NormCytIntensitySEM['SEM'], fmt='o--c', capsize=4, capthick=2, linewidth=2, markersize=7)
# plt.xlabel('Time (hr)')
# plt.ylabel('eIF2\u03B1-P Cyt Intensity FC') # https://pythonforundergradengineers.com/unicode-characters-in-python.html
# plt.ylim(0.8, 3.2)
# plt.xticks(CytIntensityMEAN['Time (hr)'], rotation=0)
# plt.xlabel('Time (hr)')

# # plt.figure(6)
# plt.errorbar(NormTotOPPIntensityMEAN['Time (hr)'], NormTotOPPIntensityMEAN['OPP Total Intensity FC'], yerr=NormTotOPPIntensitySEM['SEM'], fmt='o--c', capsize=4, capthick=2, linewidth=2, markersize=7)
# plt.xlabel('Time (hr)')
# plt.ylabel('OPP Total Intensity FC') # https://pythonforundergradengineers.com/unicode-characters-in-python.html
# plt.ylim(0, 1.2)
# plt.xticks(NormTotOPPIntensityMEAN['Time (hr)'], rotation=0)
# plt.xlabel('Time (hr)')

fig,ax1 = plt.subplots(figsize=(6.4, 4.8))
ax2 = ax1.twinx()
ax1.errorbar(NormCytIntensityMEAN['Time (hr)'], NormCytIntensityMEAN['eIF2a-P Cytoplasmic Intensity FC'], yerr=NormCytIntensitySEM['SEM'], fmt='o--y', capsize=4, capthick=2, linewidth=2, markersize=7)
ax2.errorbar(NormTotOPPIntensityMEAN['Time (hr)'], NormTotOPPIntensityMEAN['OPP Total Intensity FC'], yerr=NormTotOPPIntensitySEM['SEM'], fmt='o--b', capsize=4, capthick=2, linewidth=2, markersize=7)
ax1.set_xlabel('Time (hr)')
ax1.set_ylabel('eIF2\u03B1-P Cyt Intensity FC', color='y')
ax2.set_ylabel('OPP Total Intensity FC', color='b', rotation=-90, labelpad=25)

plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/SORA_Microscopy/050223/ImageAnalysis/NormalizedLineplot.pdf', format='pdf', bbox_inches='tight', transparent=True)
