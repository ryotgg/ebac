import pandas as pd
import json

# json string                                                                                                                
s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"x","row2":"y","row3":"z"}}'

# read json to data frame                                                                                                    
df = pd.read_json(s)
print(df)