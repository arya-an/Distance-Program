from pykml import parser
from math import sin, cos, sqrt, atan2, radians


with open('task_2_sensor.kml', 'r') as f:
  root = parser.parse(f).getroot()
x=(root.Document.Folder.Placemark.LineString.coordinates)

R = 6373.0

def get_distance(lat_1, lng_1, lat_2, lng_2): 
    d_lat = lat_2 - lat_1
    d_lng = lng_2 - lng_1 

    temp = (  
         sin(d_lat / 2) ** 2 
       + cos(lat_1) 
       * cos(lat_2) 
       * sin(d_lng / 2) ** 2
    )

    return R * (2 * atan2(sqrt(temp), sqrt(1 - temp)))

str1=str(x).strip()
cordinate = str1.split(' ')
#print(cordinate)
distance = 0
foo = []
for i in range(0,len(cordinate)-1):
  lat1, long1, h1 = cordinate[i].split(',')
  lat2, long2, h2 = cordinate[i+1].split(',')
  lat1, long1, lat2, long2 = map(radians,
                                 [float(lat1),
                                  float(long1),
                                  float(lat2),
                                  float(long2)])
  dist = get_distance(lat1, long1, lat2, long2)
  if dist > 1.0:
    continue
  # print(dist)
  foo.append(dist)
  distance = distance + dist


print("Total distance travelled : {:0.2f} KM".format(distance))
  
  
               

