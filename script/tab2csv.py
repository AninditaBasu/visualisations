#
# Data was downloaded from National Geophysical Data Center
# https://www.ngdc.noaa.gov/hazard/earthqk.shtml
# in tab-delimited format and converted to CSV.
# Downloaded file name = signif.txt
#

import csv

txt_file = r"./data/signif.txt"
csv_file = r"./data/earthquakes.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)

txt_file.close()
csv_file.close()
