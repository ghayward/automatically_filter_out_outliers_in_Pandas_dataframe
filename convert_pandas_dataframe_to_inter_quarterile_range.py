import pandas as pd
import numpy as np


def df_iqr_adjust_romain_hayward(df, list_of_columns_to_modify):
    iqr_df = df
    for i in list_of_columns_to_modify:
        Q1 = iqr_df[i].quantile(0.25)
        Q3 = iqr_df[i].quantile(0.75)
        IQR = Q3 - Q1
        iqr_df = iqr_df.query('(@Q1 - 1.5 * @IQR) <= %s <= (@Q3 + 1.5 * @IQR)' % i)
    return iqr_df


"""
Citations:

   1) Understanding the iqr logic by Romain, and the loop logic added by me
       Link -> https://www.back2code.me/2017/08/outliers/
   2) Understanding how to pass the 'i' column into the pandas query string I learned from here
       Link -> https://stackoverflow.com/questions/29085544/undefinedvariableerror-when-querying-pandas-dataframe
"""

"""
What is the above code doing?

-Takes the dataframe, then asks what columns you want to perform an IGR filter on.
-IQR filter is defined by Q1 - 1.5 * IQR and Q3 + 1.5 * IQR.
-IQR itself is everything between 25th percentile and 75th percentile, inclusive.
-We take the original df, and then call it 'iqr_df'.
-This is like our vehicle to hold the updates as we filter along column after column.
-We look at our first column that we are checking and find it's 25% and 75% percentile.
-Then we compute the IQR for that column.
-Then we use the Pandas query command to only select values that are in that IQR range for that column.
-Then we do it this same loop again for the same iqr_df vehicle-dataframe.
-We finish and give the updated dataframe, without outliers.
PS. One bit of magic is the '%s'. It's critical. If you change the character, you can lose the magic:
What's going on there is that we have to take the i from the for loop and pass it into a string. We have
to use the special % formatting command to pull the value you outside the string at the end and then inject it 
back in. You see this a lot in just how to pass a value to a string. 
-GH


"""