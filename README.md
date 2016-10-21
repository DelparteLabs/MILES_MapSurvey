# MILES
Save_json.php is a php script to be placed on server web folder, and read the incoming http request and write the data string into a json format.
Change line 9 for the json string to be stored.
$myFile = "./data/merg/".$today.".json";
In this example, the data string will be stored in json format, in the webfolder/data/merg/, and naming with the time string.
Merg.py is to combine all individual geojson file with comment into a single json file for display
change ‘path’ in line 8 for directing the script to the original geojson file.
Change the directory to the single json file in line 31.
Gson2csv.py is to extract the information from generated json file for statistics.
Textfile1 is the comment type statistics, change line 484 for the directory of file
Textfile2 is the word cloud statistics, change line 488 for directory of file.

Comment.html is the webpage for user interaction. 
Comm_type_chart.html is the webpage for displaying the pie chart result of comment type statistics.
Word_chart.html is the webpage for displaying the 100 most frequently used word in the comment text. This is a revise version of D3 word cloud implementation at http://bl.ocks.org/ericcoopey/6382449
Hiscomment.html is the webpage for listing all users comment in plain text.
Geojsonlayer.html is the webpage for displaying of geojson comment string, and it was modified from geojson-layer-js from github
https://github.com/Esri/geojson-layer-js
