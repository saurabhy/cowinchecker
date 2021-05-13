import Constants


def process(response):
    centers = response.get('centers', [])

    resp = []
    flag = False
    for center in centers:
        sessions = center.get('sessions', [])
        for session in sessions:
            if (session.get('available_capacity') > 0) and (session.get('min_age_limit', 0) == Constants.AGE):
                rdum = {'place': center['name'], 'address': center['address'], 'vaccine': session['vaccine'],
                        'date': session['date']}
                resp.append(rdum)
                flag = True

    return flag, resp


def getFullUrl(did):
    return Constants.COWIN_URL + Constants.DISTRICT_PARAM + str(did) + '&' + Constants.DATE_PARAM + Constants.TODAY
