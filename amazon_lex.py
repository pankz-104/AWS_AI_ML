import json 
import logging 
from botocore.vendored import requests 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # TODO implement 
    logger.debug(event)
        # using openweathermap api 

    
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=bc8f5fcba0ddc55c61ed343a9e860a52&q='
    
    
    city = event['currentIntent']['slots']['weathercity']
    
    logger.debug(city)
    
    url = api_address + city
    json_data = requests.get(url).json()
    
    
    formatted_data = json_data['weather'][0]['main']
    desc_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    pre = json_data['main']['pressure']
    result = "Temperature : {}k \n pressure : {}pa \n condition : {} \n description : {}".format(temp,pre,formatted_data,desc_data)

    # return formatted_data
    #print(json)
    return {
        'sessionAttributes':event['sessionAttributes'],
        'dialogAction':{
            'type':'Close',
            'fulfillmentState':"Fulfilled",
            'message':{
                'contentType':'PlainText',
                'content':str(result)
                
            }
        }
    }
