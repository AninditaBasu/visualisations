# Infographics

Simple diagrams with minimal coding. See [visualisations](http://aninditabasu.github.io/visualisations/). An ongoing project is at [the Mahabharat project](https://rawgit.com/AninditaBasu/visualisations/master/mb_weapons.html)

The following tools were used:

-    The inbuilt functions and pivot charts of spreadsheets (Microsoft Excel or OpenOffice Calc)
-    Python scripts:
    - `tab2csv.py`: Converts a tab-delimited text file into a comma-delimited spreadsheet file
    - `tweet_cloud.py`: Extracts live tweets, cleans up the text, and generates a word cloud
    - `geo_lookup.py`: Takes a CSV file as input, looks up the latitudes and longitudes of the places in the file, and adds these values to the CSV file.
    The Python scripts use the following libraries: `json`, `csv`, `geopy`, `wordcloud`, `matplotlib`, `Pillow` 
-    Converting a d3.js diagram to a static PNG file: [sankeyMATIC](http://www.sankeymatic.com/build/)

Sources of data are these:

-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles
-    Mahabharat data, major sources:
    - Kisarimohan Ganguly's English translation
    - BORI's Cultural Index
    - Apte's Sanskrit dictionary

The following resources were used for coding:
-    Sankey diagram:
    -    [code for a simple diagram](https://gist.github.com/d3noob/c2637e28b79fb3bfea13) and [explanation of the code](http://www.d3noob.org/2013/02/sankey-diagrams-description-of-d3js-code.html)
    -    [code for CSV to JSON](https://github.com/mohans-ca/Who-Said-What-Sankey) and [explanation of the code](https://www.crowdanalytix.com/communityBlog/who-said-what---d3-sankey-chart-tutorial-using-twitter-data)
