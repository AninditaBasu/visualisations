# Infographics

|  Story| Data format | Processing | Code file | 
|:-------- |:--------| :-----|:----|
|[Titanic](./examples/titanic.png)  | XLS file | Worksheet added to XLS file, where data is processed with spreadsheet's inbuilt functions | No code |
| [Earthquakes](./examples/earthquakes.png)| Tab-delimited text file file|(1) Run a code to turn the tab-delimited text file to a CSV file. (2) Add worksheets to the CSV file for data processing, and save as XLS. | `tab2csv.py`|
| [Invaders of India](https://ani-basu.cartodb.com/viz/e74ef19c-15e8-11e6-bc8b-0e3a376473ab/public_map)|CSV file, with place names | CSV file, with columns added for latitude and longitude. Used as datasheet on CartoDB| `alexander.py` | 
| [Tweet cloud](./examples/tweet_cloud.png)|JSON file of tweets pulled via Twitter's API | Extract tweet text and clean up for hashtags, punctuations, user names, and other unnecessary strings  |`tweet_cloud.py` | 

## Repository file structure

-    The root folder contains the script files (`.py`)
-    The `data` folder contains source data
-    The `examples` folder contains the output

Related files have somewhat similar file names, and should be easy to identify as a set.

## Sources

-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles
-    Python wordcloud library: [amueller's wordcloud library](https://github.com/amueller/word_cloud)


