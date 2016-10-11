<html>
 <head>
  <title>saving a geojson file</title>
 </head>
 <body>

 <?php
 $today = date("Y-m-d-H-i-s");
 $myFile = "./data/merg/".$today.".json";
 $fh = fopen($myFile, 'w') or die("can't open file");
 $stringData = $_GET["data"];
 fwrite($fh, $stringData);
 fclose($fh);

 exec('merg.py');
 
/*   merge();
 //merge all the geojson files in the ./data/merg folder
 function merge(){
 $path = "./data/merg/";
 $MergFile = "./data/test.json";
 $fmerg = fopen($MergFile, 'w') or die("can't open file");
  
 $files = scandir($path);
 $n= count($files);
 
 $Alldata = array() ;
  for ($i = 1 ; $n ; $i++) {
	$filename = $files[$i];
 	$SingFile = file_get_contents($filename);	
 	$Sdata = json_decode($SingFile, true);	
	unset($SingFile); 
     $Alldata = array_merge($Alldata, $sdata);
    fwrite($fmerg, $Alldata);    
 } 
 fclose($fmerg);  
 }   */
 ?>
 </body> 
</html>