# FRED_Series_Updates
Economic data series sorted by when observations were updated on the FRED® server.

## Website
Documentation is found [here](https://fred.stlouisfed.org/docs/api/fred/series_updates.html).

## Objective
The objective of this repository is to track updates to economic data series. An update, for our purposes, is defined as a new line of data that does not already exist in our database (currently a csv file). This comparison is done on all fields in the data (i.e., the same time series will be written to the database again if it is updated per the FRED API). The idea is that over time we'll be able to see which time series are updated, their frequency, and potentially which ones are viable for certain use cases (such as for the creation of trend factors).
