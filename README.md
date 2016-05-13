# Infographics

In progress: The Mahabharat project
-    [Arjun's travels](https://ani-basu.cartodb.com/viz/150d1be0-1945-11e6-82c4-0e98b61680bf/public_map)
-    Weapon cloud

Almost done projects are in the following table.

|  Story| Data format | Processing | Code file | 
|:-------- |:--------| :-----|:----|
|[Titanic](titanic.png)  | XLS file | Worksheet added to XLS file, where data is processed with spreadsheet's inbuilt functions | No code |
| [Earthquakes](earthquakes.png)| Tab-delimited text file file|(1) Run a code to turn the tab-delimited text file to a CSV file. (2) Add worksheets to the CSV file for data processing, and save as XLS. | `tab2csv.py`|
| [Invaders of India](https://ani-basu.cartodb.com/viz/e74ef19c-15e8-11e6-bc8b-0e3a376473ab/public_map)|CSV file, with place names | CSV file, with columns added for latitude and longitude. Used as datasheet on CartoDB| `geo_lookup.py` | 
| [Tweet cloud](tweet_cloud.png)|JSON file of tweets pulled via Twitter's API | Extract tweet text and clean up for hashtags, punctuations, user names, and other unnecessary strings  |`tweet_cloud.py` | 


## Repository file structure

-    The root folder contains the infographics
-    The `data` folder contains source data
-    The `script` folder contains the code files

## Sources

-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles
-    Python wordcloud library: [amueller's wordcloud library](https://github.com/amueller/word_cloud)
-    Mahabharat: Kisarimohan Ganguly's English translation, BORI's Cultural Index, and Wikipedia

