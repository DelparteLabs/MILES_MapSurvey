import json
#import csv
from collections import Counter
import math

fjson = "J:/Diwork/MILES_data_updated/PokeySurveyMap/PokeyMap/data/allcomments.json"

with open(fjson) as f:
      data = json.load(f)
t1=0.0
t2=0.0
t3=0.0
t4=0.0
t5=0.0
t6=0.0
t7=0.0
t8=0.0

neighbor =['Alameda Park', 'Alameda School', 'Ammon Park', 'Arbon/Rockland',
           'Arimo','Bancroft', 'Bicentennial Park', 'Bonneville', 'Buckskin Road',
           'Caribou', 'Century', 'Chubbuck', 'Chubbuck East', 'City Creek', 'Clark Street West',
           'Cotant Park', 'Chubbuck Elementary', 'Foothill', 'Fort Hall', 'Fred Meyer Area', 'Fremont',
           'Garrett', 'Green Acres', 'Hawthorne North','Hawthorne South','Heritage Railroad',
           'Highland Center', 'Highland East','Highland North', 'Highland West','Historic Old Town','Holt Arena Area',
           'Inkom','ISU','Jefferson','Johnny Creek','Lava Hot Spring','Marsh Creek','Mink Creek','Monticello',
           'Nop Park','OK Ward Park North','OK Ward Park South','Other','Pine Ridge','Pocatello Creek East',
           'Pocatello Creek West','Rapid Creek','Riverside','Riverview','Roosevelt','Ross Creek East',
           'Ross Creek West','Scardino','Springfield','Syringa','Tydeman Park','Tyhee','University District',
           'Westwood North','Westwood South','Whittier','Winco','Yellowstone']
           
           
lon = [-112.444635, -112.457603, -112.432191, -112.750328, -112.265962, -111.937601, -112.470563, -112.44121,
      -112.390428, -112.397804, -112.377159, -112.471369, -112.453865, -112.442857, -112.461386, -112.504967,
       -112.486136, -112.481197, -112.632896, -112.448659, -112.465961, -112.496407, -112.43643,  -112.471232,
       -112.470731, -112.466693, -112.41827, -112.42101, -112.407136, -112.433519, -112.456497, -112.429856,
       -112.189338, -112.422785, -112.43941, -112.424234, -112.025966, -112.203123, -112.344469, -112.436911,
       -112.461556, -112.485942, -112.485883, -112.822856, -112.466329, -112.415408, -112.427807, -112.327229,
       -112.419158, -112.469821, -112.445752, -112.249281, -112.612991, -112.442908, -112.754764, -112.451615,
       -112.446006, -112.488876, -112.437576, -112.460825, -112.45575, -112.434098, -112.447085, -112.453952]

lat = [42.887808, 42.888708, 42.881677, 42.525236, 42.566385, 42.811551, 42.941511, 42.873725, 42.856807, 42.732896,
       42.820681, 42.927744, 42.931005, 42.845394, 42.852783, 42.92466, 42.924192, 42.857959, 42.76151, 42.885073,
       42.859424, 42.902975, 42.877234, 42.903218, 42.891823, 42.875384, 42.912524, 42.905079, 42.905969, 42.911078,
       42.864507, 42.868437, 42.842673, 42.855733, 42.883881, 42.811699, 42.606746, 42.703446, 42.779774, 42.89137,
       42.90161, 42.909363, 42.90299, 42.762878, 42.914505, 42.885662, 42.8962, 42.882652, 42.831863, 42.871494,
       42.879496, 42.976053, 42.98072, 42.903759, 43.022481, 42.905248, 42.87109, 42.950983, 42.866512, 42.882128,
       42.880854, 42.8539, 42.893561, 42.898792]

comment = ''
area = []
tmpa = []
ilon = 0
ilat = 0
flon =[]
flat =[]
n = 0
Number = 0
for feature in data['features']:
      ct = feature['properties']['Comment_Type']
##      print ct
      if ct == 'River Access':
            t1 = t1+1
      elif ct == 'Recreation':
            t2 = t2+1
      elif ct == 'Transportation':
            t3 = t3+1
      elif ct == 'Water Quality':
            t4 = t4+1
      elif ct == 'Habitat':
            t5 = t5+1
      elif ct == 'Water Amount':
            t6 = t6+1
      elif ct == 'Beautification':
            t7 = t7+1
      elif ct == 'Other':
            t8 = t8+1

      comment = comment + feature['properties']['Comment']
      
      #datt = feature['properties']['Your_Area']
      #print datt
      #datword = datt.split(':')
      #sizedatt = len(datword)/2
      #if sizedatt == 1:
            #area = area + datword[0]
            #area.append(datword[0])
      #area = area + datword[sizedatt]
      #area.append(datword[sizedatt])

      datt2 = feature['properties']['Your_Area']
      datword2 = datt2.split(':')
      #newlist = [str(x) for x in datword2]

      Number = Number +1
      for i in datword2:
            
            if i == 'Alameda Park' or i == ' Alameda park' or i== 'Alameda park  ':
                  ilon = ilon + (-112.444635)
                  ilat = ilat + (42.887808)
                  n = n+1
            if i == 'Alameda School' or i == ' Alameda School' or i== 'Alameda School  ':
                  ilon = ilon + (-112.457603)
                  ilat = ilat + (42.888708)
                  n = n+1
            if i == 'Ammon Park' or i == ' Ammon Park' or i== 'Ammon Park  ':
                  ilon = ilon + (-112.432191)
                  ilat = ilat + (42.881677)
                  n = n+1
            if i == 'Arbon/Rockland' or i == ' Arbon/Rockland' or i== 'Arbon/Rockland  ':
                  ilon = ilon + (-112.750328)
                  ilat = ilat + (42.525236)
                  n = n+1
            if i == 'Arimo' or i == ' Arimo' or i== 'Arimo  ':
                  ilon = ilon + (-112.265962)
                  ilat = ilat + (42.566385)
                  n = n+1
            if i == 'Bancroft' or i == ' Bancroft' or i== 'Bancroft  ':
                  ilon = ilon + (-111.937601)
                  ilat = ilat + (42.811551)
                  n = n+1
            if i == 'Bicentennial Park' or i == ' Bicentennial Park' or i== 'Bicentennial Park  ':
                  ilon = ilon + (-112.470563)
                  ilat = ilat + (42.941511)
                  n = n+1
            if i == 'Bonneville' or i == ' Bonneville' or i== 'Bonneville  ':
                  ilon = ilon + (-112.44121)
                  ilat = ilat + (42.873725)
                  n = n+1
            if i == 'Buckskin Road' or i == ' Buckskin Road' or i== 'Buckskin Road  ':
                  ilon = ilon + (-112.390428)
                  ilat = ilat + (42.856807)
                  n = n+1
            if i == 'Caribou' or i == ' Caribou' or i== 'Caribou  ':
                  ilon = ilon + (-112.397804)
                  ilat = ilat + (42.732896)
                  n = n+1
            if i == 'Century' or i == ' Century' or i== 'Century  ':
                  ilon = ilon + (-112.377159)
                  ilat = ilat + (42.820681)
                  n = n+1
            if i == 'Chubbuck' or i == ' Chubbuck' or i== 'Chubbuck  ':
                  ilon = ilon + (-112.471369)
                  ilat = ilat + (42.927744)
                  n = n+1
            if i == 'Chubbuck East' or i == ' Chubbuck East' or i== 'Chubbuck East  ':
                  ilon = ilon + (-112.453865)
                  ilat = ilat + (42.931005)
                  n = n+1
            if i == 'City Creek' or i == ' City Creek' or i== 'City Creek  ':
                  ilon = ilon + (-112.442857)
                  ilat = ilat + (42.845394)
                  n = n+1
            if i == 'Clark Street West' or i == ' Clark Street West' or i== 'Clark Street West  ':
                  ilon = ilon + (-112.461386)
                  ilat = ilat + (42.852783)
                  n = n+1
            if i == 'Cotant Park' or i == ' Cotant Park' or i== 'Cotant Park  ':
                  ilon = ilon + (-112.504967)
                  ilat = ilat + (42.92466)
                  n = n+1
            if i == 'Chubbuck Elementary' or i == ' Chubbuck Elementary' or i== 'Chubbuck Elementary  ':
                  ilon = ilon + (-112.486136)
                  ilat = ilat + (42.924192)
                  n = n+1
            if i == 'Foothill' or i == ' Foothill' or i== 'Foothill  ':
                  ilon = ilon + (-112.481197)
                  ilat = ilat + (42.857959)
                  n = n+1
            if i == 'Fort Hall ' or i == ' Fort Hall ' or i== 'Fort Hall   ':
                  ilon = ilon + (-112.632896)
                  ilat = ilat + (42.76151)
                  n = n+1               
            if i == 'Fred Meyer Area' or i == ' Fred Meyer Area' or i== 'Fred Meyer Area  ':
                  ilon = ilon + (-112.448659)
                  ilat = ilat + (42.885073)
                  n = n+1
            if i == 'Fremont' or i == ' Fremont' or i== 'Fremont  ':
                  ilon = ilon + (-112.465961)
                  ilat = ilat + (42.859424)
                  n = n+1
            if i == 'Garrett' or i == ' Garrett' or i== 'Garrett  ':
                  ilon = ilon + (-112.496407)
                  ilat = ilat + (42.902975)
                  n = n+1
            if i == 'Green Acres' or i == ' Green Acres' or i== 'Green Acres  ':
                  ilon = ilon + (-112.43643)
                  ilat = ilat + (42.877234)
                  n = n+1                  
            if i == 'Hawthorne North' or i == ' Hawthorne North' or i== 'Hawthorne North  ':
                  ilon = ilon + (-112.471232)
                  ilat = ilat + (42.903218)
                  n = n+1  
            if i == 'Hawthorne South' or i == ' Hawthorne South' or i== 'Hawthorne South  ':
                  ilon = ilon + (-112.470731)
                  ilat = ilat + (42.891823)
                  n = n+1 
            if i == 'Heritage Railroad' or i == ' Heritage Railroad' or i== 'Heritage Railroad  ':
                  ilon = ilon + (-112.466693)
                  ilat = ilat + (42.875384)
                  n = n+1 
            if i == 'Highland Center' or i == ' Highland Center' or i== 'Highland Center  ':
                  ilon = ilon + (-112.41827)
                  ilat = ilat + (42.912524)
                  n = n+1
            if i == 'Highland East' or i == ' Highland East' or i== 'Highland East  ':
                  ilon = ilon + (-112.42101)
                  ilat = ilat + (42.905079)
                  n = n+1
            if i == 'Highland North' or i == ' Highland North' or i== 'Highland North  ':
                  ilon = ilon + (-112.407136)
                  ilat = ilat + (42.905969)
                  n = n+1
            if i == 'Highland West' or i == ' Highland West' or i== 'Highland West  ':
                  ilon = ilon + (-112.433519)
                  ilat = ilat + (42.911078)
                  n = n+1
            if i == 'Historic Old Town' or i == ' Historic Old Town' or i== 'Historic Old Town  ':
                  ilon = ilon + (-112.456497)
                  ilat = ilat + (42.864507)
                  n = n+1
            if i == 'Holt Arena Area' or i == ' Holt Arena Area' or i== 'Holt Arena Area  ':
                  ilon = ilon + (-112.429856)
                  ilat = ilat + (42.868437)
                  n = n+1                  
            if i == 'Inkom' or i == ' Inkom' or i== 'Inkom ':
                  ilon = ilon + (-112.189338)
                  ilat = ilat + (42.842673)
                  n = n+1
            if i == 'ISU' or i == ' ISU' or i== 'ISU  ':
                  ilon = ilon + (-112.422785)
                  ilat = ilat + (42.855733)
                  n = n+1
            if i == 'Jefferson' or i == ' Jefferson' or i== 'Jefferson  ':
                  ilon = ilon + (-112.43941)
                  ilat = ilat + (42.883881)
                  n = n+1
            if i == 'Johnny Creek' or i == ' Johnny Creek' or i== 'Johnny Creek  ':
                  ilon = ilon + (-112.424234)
                  ilat = ilat + (42.811699)
                  n = n+1
            if i == 'Lava Hot Springs' or i == ' Lava Hot Springs' or i== 'Lava Hot Springs  ':
                  ilon = ilon + (-112.025966)
                  ilat = ilat + (42.606746)
                  n = n+1
            if i == 'Marsh Creek' or i == ' Marsh Creek' or i== 'Marsh Creek  ':
                  ilon = ilon + (-112.203123)
                  ilat = ilat + (42.703446)
                  n = n+1
            if i == 'Mink Creek' or i == ' Mink Creek' or i== 'Mink Creek  ':
                  ilon = ilon + (-112.344469)
                  ilat = ilat + (42.779774)
                  n = n+1
            if i == 'Monticello' or i == ' Monticello' or i== 'Monticello ':
                  ilon = ilon + (-112.436911)
                  ilat = ilat + (42.89137)
                  n = n+1
            if i == 'Nop Park' or i == ' Nop Park' or i== 'Nop Park ':
                  ilon = ilon + (-112.461556)
                  ilat = ilat + (42.90161)
                  n = n+1
            if i == 'OK Ward Park North' or i == ' OK Ward Park North' or i== 'OK Ward Park North ':
                  ilon = ilon + (-112.485942)
                  ilat = ilat + (42.909363)
                  n = n+1
            if i == 'OK Ward Park South' or i == ' OK Ward Park South' or i== 'OK Ward Park South ':
                  ilon = ilon + (-112.485883)
                  ilat = ilat + (42.90299)
                  n = n+1
            if i == 'Other' or i == ' Other' or i== 'Other ':
                  ilon = ilon + (-112.822856)
                  ilat = ilat + (42.762878)
                  n = n+1
            if i == 'Pine Ridge' or i == ' Pine Ridge' or i== 'Pine Ridge ':
                  ilon = ilon + (-112.466329)
                  ilat = ilat + (42.914505)
                  n = n+1
            if i == 'Pocatello Creek East' or i == ' Pocatello Creek East' or i== 'Pocatello Creek East ':
                  ilon = ilon + (-112.415408)
                  ilat = ilat + (42.885662)
                  n = n+1
            if i == 'Pocatello Creek West' or i == ' Pocatello Creek West' or i== 'Pocatello Creek West ':
                  ilon = ilon + (-112.427807)
                  ilat = ilat + (42.8962)
                  n = n+1
            if i == 'Rapid Creek' or i == ' Rapid Creek' or i== 'Rapid Creek ':
                  ilon = ilon + (-112.327229)
                  ilat = ilat + (42.882652)
                  n = n+1                  
            if i == 'Riverside' or i == ' Riverside' or i== 'Riverside ':
                  ilon = ilon + (-112.419158)
                  ilat = ilat + (42.831863)
                  n = n+1 
            if i == 'Riverview' or i == ' Riverview' or i== 'Riverview ':
                  ilon = ilon + (-112.469821)
                  ilat = ilat + (42.871494)
                  n = n+1 
            if i == 'Roosevelt' or i == ' Roosevelt' or i== 'Roosevelt ':
                  ilon = ilon + (-112.445752)
                  ilat = ilat + (42.879496)
                  n = n+1 
            if i == 'Ross Creek East' or i == ' Ross Creek East' or i== 'Ross Creek East ':
                  ilon = ilon + (-112.249281)
                  ilat = ilat + (42.976053)
                  n = n+1 
            if i == 'Ross Creek West' or i == ' Ross Creek West' or i== 'Ross Creek West ':
                  ilon = ilon + (-112.612991)
                  ilat = ilat + (42.98072)
                  n = n+1 
            if i == 'Scardino' or i == ' Scardino' or i== 'Scardino ':
                  ilon = ilon + (-112.442908)
                  ilat = ilat + (42.903759)
                  n = n+1 
            if i == 'Springfield' or i == ' Springfield' or i== 'Springfield ':
                  ilon = ilon + (-112.754764)
                  ilat = ilat + (43.022481)
                  n = n+1 
            if i == 'Syringa' or i == ' Syringa' or i== 'Syringa ':
                  ilon = ilon + (-112.451615)
                  ilat = ilat + (42.905248)
                  n = n+1 
            if i == 'Tydeman Park' or i == ' Tydeman Park' or i== 'Tydeman Park ':
                  ilon = ilon + (-112.446006)
                  ilat = ilat + (42.87109)
                  n = n+1 
            if i == 'Tydeman Park' or i == ' Tydeman Park' or i== 'Tydeman Park ':
                  ilon = ilon + (-112.446006)
                  ilat = ilat + (42.87109)
                  n = n+1                   
            if i == 'Tyhee' or i == ' Tyhee' or i== 'Tyhee  ':
                  ilon = ilon + (-112.488876)
                  ilat = ilat + (42.950983)
                  n = n+1
            if i == 'University District' or i == ' University District' or i== 'University District  ':
                  ilon = ilon + (-112.437576)
                  ilat = ilat + (42.866512)
                  n = n+1
            if i == 'Westwood North' or i == ' Westwood North' or i== 'Westwood North  ':
                  ilon = ilon + (-112.460825)
                  ilat = ilat + (42.882128)
                  n = n+1
            if i == 'Westwood South' or i == ' Westwood South' or i== 'Westwood South  ':
                  ilon = ilon + (-112.45575)
                  ilat = ilat + (42.880854)
                  n = n+1
            if i == 'Whittier' or i == ' Whittier' or i== 'Whittier  ':
                  ilon = ilon + (-112.434098)
                  ilat = ilat + (42.8539)
                  n = n+1                  
            if i == 'Winco' or i == ' Winco' or i== 'Winco  ':
                  ilon = ilon + (-112.447085)
                  ilat = ilat + (42.893561)
                  n = n+1
            if i == 'Yellowstone' or i == ' Yellowstone' or i== 'Yellowstone  ':
                  ilon = ilon + (-112.453952)
                  ilat = ilat + (42.898792)
                  n = n+1
            if i==' ':
                  n=n+1

      if ilon != 0 :
           #print n
            flon.append(ilon/n)
            flat.append(ilat/n)
            tlon=ilon/n
            tlat=ilat/n
            for j in range(0,64):
                 dist = math.sqrt((tlon-lon[j])*(tlon-lon[j])+(tlat-lat[j])*(tlat-lat[j]))
                 if j==0:
                       small = dist
                 if dist < small:
                       smallx = lon[j]
                       smally = lat[j]
                       small = dist
            #print small
            for s in range(0,64):
                  if smallx == lon[s]:
                       area.append(neighbor[s])     
      n = 0
      ilon = 0
      ilat = 0

neighbor_name = []
neighbor_per = []
areacnt = Counter(area).most_common(5)
for i in range(0,5):
      var1 = areacnt[i][0]
      var2 = float(areacnt[i][1])/float(Number)
      print var1, var2
      neighbor_name.append(var1)
      neighbor_per.append(var2)
      
tt = t1+t2+t3+t4+t5+t6+t7+t8

tp1 = 100*(t1/tt)
tp2 = 100*(t2/tt)
tp3 = 100*(t3/tt)
tp4 = 100*(t4/tt)
tp5 = 100*(t5/tt)
tp6 = 100*(t6/tt)
tp7 = 100*(t7/tt)
tp8 = 100*(t8/tt)

##print tp1,tp2,tp3,tp4,tp5,tp6,tp7,tp8

##with open('J:/Diwork/MILES_data_updated/PokeySurveyMap/comm_type.csv','w') as csvfile:
##      fieldnames = ['Comment_Type','Percentage']
##      writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
##
####      writer.writeheader()
##      writer.writerow({'Comment_Type': 'River Access', 'Percentage': tp1})
##      writer.writerow({'Comment_Type': 'Recreation', 'Percentage': tp2})
##      writer.writerow({'Comment_Type': 'Transportation', 'Percentage': tp3})
##      writer.writerow({'Comment_Type': 'Water Quality', 'Percentage': tp4})
##      writer.writerow({'Comment_Type': 'Habitat', 'Percentage': tp5})
##      writer.writerow({'Comment_Type': 'Water Amount', 'Percentage': tp6})
##      writer.writerow({'Comment_Type': 'Beautification', 'Percentage': tp7})
##      writer.writerow({'Comment_Type': 'Other', 'Percentage': tp8})
##
##print "done writing to csv file"

commwords = comment.split()
wordlist = ['river']
listprint = 'river'
for word in commwords:
      word = str(word)
      if word != 'about' and word !='all' and word != 'able' and word != 'some' and word != 'many'\
         and word != 'it' and word !='of'  and word != 'be' and word !='a' and word !='in' and word !='the'\
         and word != 'IT' and word !='I' and word !='lot' and word !='or' and word !='(dd)If'\
         and word != 'was' and word !='were' and word !='on' and word !='from' and word !='for'\
         and word != 'and' and word !='also' and word !='could' and word !='would' and word !='with'\
         and word != 'out' and word !='by' and word !='as' and word !='will' and word !='up'\
         and word != 'not' and word !='to' and word !='at' and word !='into' and word !='DO'\
         and word != 'NOT' and word !='TO' and word !='AGAINThe' and word !='its' and word !='your'\
         and word != 'is' and word !='Not' and word !='If' and word !='an' and word !='YOUR'\
         and word != 'but' and word !='OF' and word !='THE' and word !='WOULD' and word !='A'\
         and word != 'THIS' and word !='this' and word !='This' and word != 'What' and word !='st'\
         and word != 'Id' and word !='Make' and word !='re' and word !='rid' and word !='San'\
         and word != 'dont' and word !='just' and word != "It's" and word !="don\'t" and word !="I\'d"\
         and word != "it\'s" and word !="I\'ve" and word !="doesn\'t" and word !="I\'m" and word !='two'\
         and word != 'ALL' and word !='over' and word != 'much' and word !='over' and word !='even'\
         and word != 'year' and word !='year.a' and word !='years' and word !='yes' and word !='you'\
         and word != "won't" and word !='without' and word !='wants' and word !='here' and word !='are'\
         and word != 'than' and word !='there' and word !='want' and word !='tge' and word !='that'\
         and word != 'should' and word !='BUT' and word !='which' and word !='-' and word !='..all'\
         and word != '100' and word !='50' and word !='3' and word !='40' and word !='50' and word !='5000'\
         and word != '6000' and word !='ACE' and word !='AFTER' and word !='At' and word !='AND' and word !='DONE'\
         and word != '100' and word !='Also' and word !='(which' and word !='Any' and word !='But'\
         and word != 'Do' and word !='My' and word !='SA?' and word !='St' and word !='TOO.' and word !='Too.Any'\
         and word != '"no' and word !='......lots' and word !='......i' and word !='On' and word !='HAVE'\
         and word != 'So' and word !='Rd.Is' and word !='TX' and word !='That' and word !='WAS' and word !='WERE'\
         and word != 'what' and word != 'so' and word !='can' and word !='my' and word !='if' and word !='they'\
         and word != 'IN' and word !='It' and word !='The' and word !='Then' and word !='We' and word !='FOR'\
         and word != 'we' and word !='where' and word !='YOU' and word !='has' and word !='these' and word !='their'\
         and word != 'above' and word !='go' and word !='have' and word !='get' and word !='those' and word !='put'\
         and word != 'here.' :
            if word == 'river.':
                  word = 'river'
            elif word == 'area.':
                  word = 'area'
            wordlist.append(word)
            listprint = listprint + ' ' + word

cnt = Counter(wordlist).most_common(100)
#wordf = sorted(cnt.iteritems())
#wordf = cnt.items()
mwordf = [i for (i,j) in cnt]
mwordc = [j for (i,j) in cnt]

wordstr = ''
index = 0 
for i in mwordf:
      if index == 0:
         wordstr = wordstr + i
         index = index + 1
      else :
         wordstr = wordstr + ',' + i
         index = index + 1
for j in mwordc:
      wordstr = wordstr + ',' + str(j)


tptext = str(tp1)+','+str(tp2)+','+str(tp3)+','+str(tp4)+','+str(tp5)+','+str(tp6)+','+str(tp7)+','+str(tp8)

textfile1=open("J:/Diwork/MILES_data_updated/PokeySurveyMap/commtype.txt",'w')
textfile1.write(tptext)
textfile1.close()

textfile2= open("J:/Diwork/MILES_data_updated/PokeySurveyMap/word.txt",'w')
textfile2.write(wordstr)
textfile2.close()


