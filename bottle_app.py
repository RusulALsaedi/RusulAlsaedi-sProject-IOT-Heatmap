@route('/Heatmap')
def Heatmap():
    req = requests.get('https://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?')
    data = req.json()
    return template("Heatmap",data=data)
