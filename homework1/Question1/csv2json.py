#!/usr/bin/python3
import pandas as pd
import sys

# Nifi will send the data using the standard input, so we will use sys.stdin to read the data from previous process
df = pd.read_csv(sys.stdin) 
print(df.head())
df.to_json("/tmp/data.json", orient='records')