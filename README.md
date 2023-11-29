# PennsylvaniaCovidCases
Pulling Pennsylvania Covid Cases by County and then grouping the counties that are linked to Philly Metro.

Beautiful Soup is used to parse the website in lxml.  It locates the county cases .PDF.  Tabula is used to convert the .PDF into a dataframe.
