import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


"""
Write a function to count the manager wise sale (sale_cnt)
and mean value of sale amount (sale_mean). 
Order the output dataframe by sale_cnt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Manager
    - sale_cnt
    - sale_mean
and numeric index starting with 0 (after sorting).
"""

def compute_agg_stats(df):
    return(df.groupby('Manager').agg(sale_cnt = ('Item', 'count'), sale_mean = ('Sale_amt', 'mean')).sort_values('sale_cnt', ascending=False).reset_index())