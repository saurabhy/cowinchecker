def process(response):
    centers = response.get('centers', [])

    resp = []
    flag = False
    for center in centers:
        sessions = center.get('sessions', [])
        for session in sessions:
            if (session.get('available_capacity') > 0) and (session.get('min_age_limit', 0) == 18):
                rdum = {'place': center['name'], 'address': center['address'], 'vaccine': session['vaccine'],
                        'date': session['date']}
                resp.append(rdum)
                flag = True

    return flag, resp
