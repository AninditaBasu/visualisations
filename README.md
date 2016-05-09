# Visualisations

A place to experiment with and learn visualisations.

| Code file      | Input           | Output  | Usage scenario|
| ------------- |-------------| -----|----|
|`tweet_cloud.py` | JSON file of tweets | Text file of tweet text cleaned up for hashtags, punctuations, user names, and other unnecessary strings | Use as an input for cognitive analysis services. Or as an input for word cloud generator, like in this example: [my tweets cloud](./examples/tweet_cloud.png) |
|`alexander.py` | CSV file, with place names | CSV file, with columns added for latitude and longitude | Use as an input for geo-plotting, for example on CartoDB like this example: [Invaders of India](https://ani-basu.cartodb.com/viz/e74ef19c-15e8-11e6-bc8b-0e3a376473ab/public_map)|
| `bar_chart_titanic.py`| CSV file | bar charts | Might not have generic application as code is built around a specific file. Used here to generate a chart that could be used in an inforgraphic, like in this example:[Titanic survivors, by class and gender](./examples/titanic_bargraph.png)  |
| `earthquakes.py`|CSV file|horizontal bar charts| Might not have generic application as code is built around a specific file. Used here to create a composite infographic of charts and text generated through the code, like this: [Earthquakes](./examples/earthquakes.png)|

## References

-    wordcloud library: [amueller's wordcloud library](https://github.com/amueller/word_cloud)
-    bar chart code: [pylab's barchart demo](http://matplotlib.org/examples/pylab_examples/barchart_demo.html)
-    horizontal bar chart code: [Matplotlib's barh demo](http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html)
-    Titanic data: [Vanderbilt University's Department of Biostatistics's data set](biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls)
-    Earthquake data: [National Geophysical Data Center](www.ngdc.noaa.gov/hazard/earthqk.shtml)
-    Invaders data: Wikipedia articles

## Repository file structure

-    The root folder contains the script files (`.py`)
-    The `data` folder contains source data
-    The `examples` folder contains the output

All related files have somewhat similar file names, and should be easy to identify as a set.

