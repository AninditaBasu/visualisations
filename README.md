# Visualisations

Simple diagrams.

-    Tweet word cloud. Reads data from a JSON file and uses [amueller's wordcloud library](https://github.com/amueller/word_cloud). Data is in a JSON file of my own tweets. Tweets are cleaned up for hashtags, punctuations, user names, and other unnecessary strings before feeding into the `wordcloud` library. Output is this image: ![my tweets cloud](./examples/word_cloud.png)
-    Bar graph of Titanic survivors. Reads data from a CSV file and uses pylab's [barchart](http://matplotlib.org/examples/pylab_examples/barchart_demo.html) example. The CSV file is from biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls. The output is this image: ![Titanic survivors, by class and gender](./examples/titanic_bargraph.png)
-    _Work-in-progress_: Composite infographic of bar charts and text. Reads data from a CSV file of all recorded earthquakes till date.  The CSV file is created from a tab-delimited file from https://www.ngdc.noaa.gov/hazard/earthqk.shtml.
-    _Work-in-progress_: Line graph + geo plot. Alexander's route.

Repository file structure: Code is in the root folder, as `.py` files. Source data is in `data` and output is in `examples`.