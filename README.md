Classical Statistics
==============================

Datasets and example code for Lesson 5 in Oracle Academy's Data Science Bootcamp. Python scripts are included for generating various datasets: **multivariate_hdfs.py**, **function_generator.py**, and **white_noise_shocks.py**.  R functions for building linear models and decomposing timeseries data are in **Bootcamp.R**.  Sample data for R is included in the **.dat** files.  Finally, **shocks.pig** provides Pig Latin code for finding whitenoise shocks in a large set of time series data using Hadoop.

Suggested progression:

1. Use **flume_example.conf** and the python scripts to generate time-series and regression data.
2. Use Hive to sample the time series and regression data and construct datasets for R.
3. Use the code in **Bootcamp.R** to analyze the datasets
4. Modify **shocks.pig** to detect white noise shocks in the appropriate data in HDFS.