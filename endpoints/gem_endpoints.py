from typing import List, Dict, Union

from fastapi import APIRouter, Security, security, Depends, Query
from fastapi.security import HTTPAuthorizationCredentials
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from fastapi.encoders import jsonable_encoder
import repos.gem_repository
from endpoints.user_endpoints import auth_handler
#from populate import calculate_gem_latitude
from models.gem_models import *
from db.db import session
from geopy.geocoders import Nominatim


gem_router = APIRouter()


@gem_router.get('/')
def greet():
    return 'Hello please use the link: ' + 'http://127.0.0.1:8000/docs'


@gem_router.get('/gems', tags=['Gems'])
def gems(places_farther_than: Optional[int] = None):
    gems = select(Gem)
    
    if places_farther_than:
        gems = gems.where(Gem.distance >= 0)
    


    if type:
        gems = gems.order_by(-Gem.distance).order_by(-Gem.distance).order_by(None)
    gems = session.exec(gems).all()

    #THIS WAY WE GET THE LOCATIONS AND NAMES AND ID OF 
    # ALL THE PLACES AND THEN WE USE THESE NAMES AND GET THE LOCATION OF THE ENTERED PLACES FROM THE USERS CURRENT LOCATION. 
    # FOR EXAMPLE IF THE DEVELOPER ENTERS A CITY BANGALORE WHILE SITTING AT MUMBAI 
    # THEN THE DISTANCE SAY IS 900 miles AND NOW THE CONSUMER IF RUNS THIS API FROM BANGALORE 
    # WITH A FILTER OF PLACES FARTHER THAN 800 MILESS THEN BY LOGIC BANGALORE SHOULD NOT COME WHILE THE
    # CONSUMER IS IN BANGALORE BECUSE BANGALORE IS NOT 900 MILES FROM BANGALORE.


    emp = []
    empid = []
    for x in gems:
        print(str(x))
        for y in x:
            
            if 'location' in y:
                print("Please wait while we get location")
                v2 = y[1]
                emp.append(v2)
            if 'id' in y:
                print("please wait while we get id")
                v3 = y[1]
                empid.append(v3)
    
    test_keys = emp
    test_values = empid
    
    
    
   
    res = {}
    for key in test_keys:
        for value in test_values:
            res[key] = value
            test_values.remove(value)

            break
    
    dist_val = []
    locs_place = []
    for i in res.keys():
        dict1 = {}
        loc = Nominatim(user_agent="GetLoc")
    
        # entering the location name
        getLoc = loc.geocode(i)
        
        # printing address
        
        
        # printing latitude and longitude
        

        val_lat = getLoc.latitude
        val_lon = getLoc.longitude
       

        import geocoder
        g = geocoder.ip('me')
        

        val = g.latlng

        lat2 = val[0]
        lon2 = val[1]

        loc1 = (val_lat,val_lon)
        loc2 = (lat2,lon2)
        import haversine as hs
        from haversine import Unit

        
        dist = hs.haversine(loc1,loc2,unit = Unit.MILES)
        dist_val.append(dist)
        gems = select(Gem)



        if places_farther_than:
            if dist >=places_farther_than:
                dict1['id'] = res[i]
                dict1['location'] = (i)
                dict1['distance'] = dist
                dict1['unit'] = "Miles"
                locs_place.append(dict1)

                

        

    

    gems = locs_place
    return {'gems': gems}





@gem_router.post('/gems', tags=['Gems'])
def create_gem(gem: Gem, user=Depends(auth_handler.get_current_user)):
    """Creates Entry"""
    if not user.is_auth:
        return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content="not authorised")

    loc = Nominatim(user_agent="GetLoc")
 
    # entering the location name
    getLoc = loc.geocode(gem.location)
    
    # printing address
    
    
    # printing latitude and longitude
    

    val_lat = getLoc.latitude
    val_lon = getLoc.longitude


    import geocoder
    g = geocoder.ip('me')


    val = g.latlng

    lat2 = val[0]
    lon2 = val[1]

    loc1 = (val_lat,val_lon)
    loc2 = (lat2,lon2)
    import haversine as hs
    from haversine import Unit

    
    dist = hs.haversine(loc1,loc2,unit = Unit.MILES)


    gem_v = Gem(distance=dist, seller=user,location=gem.location)
    session.add(gem_v)

    session.commit()
    return gem


@gem_router.put('/gems/{id}', response_model=Gem, tags=['Gems'])
def update_gem(id: int, gem: Gem, user=Depends(auth_handler.get_current_user)):
    gem_found = session.get(Gem, id)

    try:
   
        if not user.is_auth:
            return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content = "not authorized")
        update_item_encoded = jsonable_encoder(gem)
        update_item_encoded.pop('id', None)
        for key, val in update_item_encoded.items():
            gem_found.__setattr__(key, val)
        session.commit()
        return gem_found

    except:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,content="not found")




@gem_router.delete('/gems/{id}', status_code=HTTP_204_NO_CONTENT, tags=['Gems'])
def delete_gem(id:int, user=Depends(auth_handler.get_current_user)):
    gem_found = session.get(Gem, id)
    try:

        if not user.is_auth:
            return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content="not authorized")


        session.delete(gem_found)
        session.commit()
    except:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,content="not found")
