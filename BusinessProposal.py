#!/usr/bin/env python
# coding: utf-8

# # The battle of neighborhoods (Data Description)
# 
# Data Description:
# 31317_1295783_compressed_housing-new-york-units-by-building.csv
# https://cocl.us/new_york/dataset
# We will scrape the above dataset consisting of latitude and longitude coordinates, postal codes.
# 
# 
# Foursquare is a location data provider with information about all manner of venues and events within an area of interest. Such information includes venue names, locations, menus and even photos. As such, the foursquare location platform will be used as the sole data source since all the stated required information can be obtained through the API.
# 
# For this project we will be analysing top familial restaurants, and rental property prices around the state of New York , with the help of Foursqure. To help prospective business owners where to set their venues, and the worst places to avoid due to costs, and socio-economic issues that come with settling there. The data will also aid, single persons, and nuclear families to weigh options, on which neighborhoods to best invest in.
# 
# # Introduction to the Opportunity
# 
# New York, is one of the states in the United states of America, comprised of many Borroughs, like Queens, and the Bronx.
# 
# # Problems to solve
# 
# 1. Look for property prices ranges for different types of units in New York.
# 2. Look for different venues
# 3. Categorise the different venues
# This will be done so, for the sake of accumulating data for prospective busineess opportunities of a business owner. 
# The probles solved, will also help single persons, families, moving into New York, to decided on their rental property plans, and discern on the kind of restaurants, and varius venues available.
# 
# # Work Flow
# 
# Using credentials of Foursquare API. The project will be limitted to a number of a 100 places per neighborhood parameter. And a radius paramter of 500.
# 
# # Segmenting and Clustering
# 
# During the project, clustering will be done using K-Means algorithm.
# 
# # Python libraries used
# 
# Numpy- For creating arrays
# Pandas- For putting data into Dataframes, and retrieving meaning from it.
# Geocoder- For identifying geographical areas
# Folium- Visualization of neighborhoods cluster distribution
# Sklearn/Scikit Learn- k-means clustering
# JSON- For JSON files
# csv - For .csv files
# Requests- For scraping and cleaning data
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[ ]:




