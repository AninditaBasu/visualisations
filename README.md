# Visualisations

A place to experiment with visualisations. To turn raw data into appealing stories. With minimal coding.

|  Story| Data format | Processing | Code file | 
|:-------- |:--------| :-----|:----|
|[Titanic infographic](./examples/titanic.png)  | XLS file | Worksheet added to XLS file, where data is processed with spreadsheet's inbuilt functions | No code |
| [Invaders of India](https://ani-basu.cartodb.com/viz/e74ef19c-15e8-11e6-bc8b-0e3a376473ab/public_map)|CSV file, with place names | CSV file, with columns added for latitude and longitude. Used as datasheet on CartoDB| `alexander.py` | 
| [Tweet cloud](./examples/tweet_cloud.png)|JSON file of tweets pulled via Twitter's API | Extract tweet text and clean up for hashtags, punctuations, user names, and other unnecessary strings  |`tweet_cloud.py` | 
| [Earthquakes](./examples/earthquakes.png)| CSV file|create bar charts | `earthquakes.py`|

## References

-    wordcloud library: [amueller's wordcloud library](https://github.com/amueller/word_cloud)
-    horizontal bar chart code: [Matplotlib's barh demo](http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html)
-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles

## Repository file structure

-    The root folder contains the script files (`.py`)
-    The `data` folder contains source data
-    The `examples` folder contains the output

All related files have somewhat similar file names, and should be easy to identify as a set.

