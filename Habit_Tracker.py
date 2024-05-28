import requests
import datetime as dt
pixela_endpoint='https://pixe.la/v1/users'
USERNAME='aaravone'
GRAPH_ID='graph1'
pixela_params={
    'token':'qwerty1234',
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor': 'yes'
}
response=requests.post(url=pixela_endpoint,json=pixela_params)
#print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    'id':GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'shibafu',
}
headers ={
    'X-USER-TOKEN': 'qwerty1234'
}

#response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
#print(response.text)
input_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=dt.datetime(year=2024,month=3, day=9)
input_config={
    'date': today.strftime('%Y%m%d'),
    'quantity':'10.65',
}

#response=requests.post(url=input_endpoint,json=input_config,headers=headers)
#print(response.text)

update_endpoint=f"{input_endpoint}/{today.strftime('%Y%m%d')}"
new_pixela_data={
    'quantity':'4.5'
}
response=requests.put(url=update_endpoint,json=new_pixela_data,headers=headers)
print(response.text)