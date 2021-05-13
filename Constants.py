from datetime import date

COWIN_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?'

DISTRICT_PARAM = 'district_id='

INTERVAL = 60 * 15  # 15 minutes

DISTRICT_CODE_KANPUR = 664
DISTRICT_CODE_AHM = 770

today_date = date.today()

DATE_PARAM = 'date='

TODAY = str(today_date.day) + '-' + str(today_date.month) + '-' + str(today_date.year)

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'}

AGE = 18
