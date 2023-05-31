# IF-CellProfiler-pipeline
This image segmentation pipeline identifies individual stress granules and cells in 16-bit tiff images. It outputs total pixel intensity and count of stress granule, cytoplasmic G3BP1 fluorescence, OPP fluorescence, and eIF2a-P fluorescence in csv files.

### eIF2a-P_OPP_Intensity_v2.py
Input: Image.csv, Red_Cytoplasm.csv, OPP_whole_cell.csv  
Output: eIF2a-P cytoplasmic intensity FC and OPP Total intensity line plot   

Definition:   
eIF2a-P cytoplasmic intensity FC: all values of eIF2a-P cytoplasmic intensity divided by mean of the three replicates of medians of eIF2a-p cytoplasmic intensity at time 0  
OPP total intensity FC: all values of OPP total intensity divided by the mean of the three replicates of the medians of OPP total intensity at time 0  
Line plot: three replicates of median of eIF2a-P cytoplasmic intensity FC in each well and three replicates of median of OPP Total intensity FC in each well

### OPPuro_eIF2aP_Relate_v2.py
Input: Image.csv, Red_Cytoplasm.csv, OPP_whole_cell.csv
Output: scatter plot of mean eIF2a-P and OPP

Definition:  
Scatter plot: mean of all cytoplasmic eIF2a-P values at a timepoint related to mean of all total OPP related at the same timepoint through parent_nuclei
