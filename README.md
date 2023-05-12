# FRED_Series_Updates
Economic data series sorted by when observations were updated on the FRED® server.

![Imgur](https://imgur.com/KTMm4AW.jpg)

## What is FRED?
[Short for Federal Reserve Economic Data, FRED is an online database consisting of hundreds of thousands of economic data time series from scores of national, international, public, and private sources.](https://fredhelp.stlouisfed.org/fred/about/about-fred/what-is-fred/)

## What is ALFRED?
[ALFRED® allows you to retrieve vintage versions of economic data that were available on specific dates in history.](https://alfred.stlouisfed.org/)

## Website for FRED's Series Updates
Documentation is found [here](https://fred.stlouisfed.org/docs/api/fred/series_updates.html).

![Imgur](https://imgur.com/v17JCvw.jpg)

## Objective
The objective of this repository is to track updates to economic data series. An update, for our purposes, is defined as a new line of data that does not already exist in our database (currently a csv file). This comparison is done on all fields in the data (i.e., the same time series will be written to the database again if the `last updated` parameter changed per the FRED API). The data gathering process, using the Series Updates API, started on `May 11th, 2023`. Over time we'll be able to see which time series are updated, their frequency, and potentially which time series are viable for certain use cases (such as for the creation of trend factors to be used in an appraisal).
