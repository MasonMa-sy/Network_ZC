Using Keras as networks API.
Keras version is 2.1.6
tensorflow version is 1.8.0

This version of code just use dense and/or conv2d to contruct networks.  
There is a very serious problem of overfitting.  

2018/9/26<br>
The overfitting may be solved. This problem may be related to different historical field.

2018/11/2<br>
Run ZC model freely. The results also look good.

2018/11/17
Processing historical data.
SST from HadISST1: https://climexp.knmi.nl/select.cgi?id=someone@somewhere&field=hadisst1
In the equatorial Pacific, the depth of 20C isotherm is widely used to represent the thermocline depth.
Z20C form GODAS(Can not get data from GODAS directly):http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.EMC/.CMB/
.GODAS/.monthly/.BelowSeaLevel/.POT/Y/%28-20%29%2820%29RANGE/X/122.25/288.75/RANGE/%28Celsius_scale%29unitconvert/
Z/20/invertontogrid/datafiles.html
The monthly mean is calculated using the historical data from 198001 to 201809.
The wind stress anomaly data for ZC prediction: https://iridl.ldeo.columbia.edu/SOURCES/.FSU/index.html