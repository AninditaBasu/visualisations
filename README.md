# Infographics

Simple diagrams with minimal coding.

## Completed diagrams

| Infographic| Data format | Processing | Code file | 
|:-------- |:--------| :-----|:----|
|[Titanic](./images/titanic.png)  | XLS file | Worksheet added to XLS file, where data is processed with spreadsheet's inbuilt functions | No code |
| [Earthquakes](./images/earthquakes.png)| Tab-delimited text file file|(1) Run a code to turn the tab-delimited text file to a CSV file. (2) Add worksheets to the CSV file for data processing, and save as XLS. | `tab2csv.py`|
| [Invaders of India](https://ani-basu.cartodb.com/viz/e74ef19c-15e8-11e6-bc8b-0e3a376473ab/public_map)|CSV file, with place names | CSV file, with columns added for latitude and longitude. Used as datasheet on CartoDB| `geo_lookup.py` | 
| [Tweet cloud](./images/tweet_cloud.png)|JSON file of tweets pulled via Twitter's API | Extract tweet text and clean up for hashtags, punctuations, user names, and other unnecessary strings  |`tweet_cloud.py` | 

## In-progress diagrams: the Mahabharat project

-    [Arjun's travels](https://ani-basu.cartodb.com/viz/150d1be0-1945-11e6-82c4-0e98b61680bf/public_map)
-    [Weapon diagram](mb_weapons.html)

## Sources

-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles
-    Python wordcloud library: [amueller's wordcloud library](https://github.com/amueller/word_cloud)
-    Mahabharat data: Kisarimohan Ganguly's English translation, BORI's Cultural Index, and Wikipedia
-    Sankey diagram: (1) [code for a simple diagram](https://gist.github.com/d3noob/c2637e28b79fb3bfea13) and [explanation of the code](http://www.d3noob.org/2013/02/sankey-diagrams-description-of-d3js-code.html) (2) [code for CSV to JSON](https://github.com/mohans-ca/Who-Said-What-Sankey) and [explanation of the code](https://www.crowdanalytix.com/communityBlog/who-said-what---d3-sankey-chart-tutorial-using-twitter-data)
