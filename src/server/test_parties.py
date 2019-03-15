import datetime
testParties = [
    {
      "id":1,
      "name":"first",
      "location": {
        "latitude":50.1,
        "longtitude":24.123,
      },
      "description": "small party!",
      "seets" : 5,
      "tutorial": False,
      "cousine": "Greek",
      "date": str(datetime.date(2019, 12, 1)),
      "image": "http://127.0.0.1:5000/second.png",
    },
        
    {
      "id":2,
      "name":"second",
      "location": {
        "latitude":100.1,
        "longtitude":124.123,
      },
      "description": "Big Party!",
      "seets" : 15,
      "tutorial": True,
      "cousine": "French",
      "date": str(datetime.date(2009, 6, 14)),
      "image": "http://127.0.0.1:5000/first.png",
    }
]