#This module should contains comparator used in sorting only

#Sort data by distance to latitude and longtitude
#This function should receive a MsCompany object list model
#And center latitude and longtitude as the parameter
def sortByDist(compList, centerLat, centerLng):
    compList.sort(key = lambda p: (compList.lat - centerLat)**2 + (compList.lng - centerLng)**2)
    return compList