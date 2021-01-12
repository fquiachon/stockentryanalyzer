# stock-entry-analyzer
stock-entry-analyzer, Is a Stock Market web API that aims to automate analysis of the stock market price resistance ans support based on available historical data. 

## Technology Stack
![Alt text](docs/stacj.jpg)

## Pre Setup
### Development Setup
<p>Create a new Python 3.x virtual environment</p>
* Setup python environment

`python3 -m venv env`

* Python Libraries
    * django==3.1.2
    * yfinance==0.1.15
    * pandas==1.1.3
    * pandas-datareader==0.9.0

    
### Database Setup
see project's `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


## Endpoints
https://<host>:<port>/v1/<API Endpoints>

### Stock Market Tickers

#### GET /v1/support/<str:ticker> 200

#### GET /v1/resistance/<str:ticker> 200

#### POST /v1/support 201

request body:
  
  `{
	"tickers": "TSLA,FB"
  }`
  
response body:
  
```
{
  "TSLA": {
    "current_price": 811.19,
    "current_date": "2021-01-11T00:00:00",
    "S1": {
      "date": "2020-12-10 00:00:00",
      "price": 566.34,
      "diff %": 30.18
    },
    "S2": {
      "date": "2020-10-06 00:00:00",
      "price": 406.05,
      "diff %": 49.94
    }
  },
  "Status": "3/3 Completed",
  "FB": {
    "current_price": 256.84,
    "current_date": "2021-01-11T00:00:00",
    "S1": {
      "date": "2020-10-07 00:00:00",
      "price": 254.82,
      "diff %": 0.79
    },
    "S2": {
      "date": "2020-09-21 00:00:00",
      "price": 244.13,
      "diff %": 4.95
    }
  }
}
```

#### POST /v1/resistance 200

request body:
  
  `{
	"tickers": "TSLA,FB"
  }`
  
response body:
  
```
{
  "TSLA": {
    "current_price": 811.19,
    "current_date": "2021-01-11T00:00:00",
    "R1": "No resistance",
    "R2": "No resistance"
  },
  "Status": "2/2 Completed",
  "FB": {
    "current_price": 256.84,
    "current_date": "2021-01-11T00:00:00",
    "R1": {
      "date": "2020-10-01 00:00:00",
      "price": 268.33,
      "diff %": 4.28
    },
    "R2": {
      "date": "2020-08-07 00:00:00",
      "price": 278.89,
      "diff %": 7.91
    }
  }
}
```

## Execution
1. Run django app using command:

    `python manage.py runserver`


