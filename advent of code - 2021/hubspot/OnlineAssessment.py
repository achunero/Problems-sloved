from dateutil import parser
import requests
import json


# Get the dataset that you need to work with
def get_data_json_format(url):
    result = requests.get(url)
    return result.json()


# Parse the data set and produce two hashmap, one with {country:email} and another with {emailid:[dates]}
def parse_json_data(input):
    email_dates = {}
    country_email = {}
    for person in input['partners']:
        if person['country'] not in country_email:
            country_email[person['country']] = [person['email']]
        else:
            country_email[person['country']].append(person['email'])

        email_dates[person['email']] = person['availableDates']

    return email_dates, country_email


# Read the countries hashmap, and for each country read the different set of email id. For each email, read the dates
# and find the possible start dates. Finally which ever start date has occured maximum number of times choose that
# as the final start date and its corresponding email id's
def find_start_date_for_country(person, countries):
    country_startdate = {}
    for country in countries:

        con = {}

        for eid in countries[country]:
            dates = person[eid]

            for dt in range(0, len(dates) - 1):
                startdate = parser.parse(dates[dt])
                enddate = parser.parse(dates[dt + 1])
                diff = enddate - startdate

                if diff.days == 1:
                    if dates[dt] not in con:
                        con[dates[dt]] = [1, [eid]]
                    else:
                        con[dates[dt]][0] += 1
                        con[dates[dt]][1].append(eid)

        cnt = 0
        final_date = None

        for sdate in con:
            if con[sdate][0] > cnt:
                final_date = sdate
                cnt = con[sdate][0]
                attendees = con[sdate][1]
            else:
                if con[sdate][0] == cnt:
                    d1 = parser.parse(sdate)
                    d2 = parser.parse(final_date)
                    if d1 < d2:
                        final_date = sdate
                        attendees = con[sdate][1]

        country_startdate[country] = (final_date, cnt, attendees)

    return country_startdate


# Finally create the structure for output
def final_output_formatter(data):
    output = []
    for cont in data:
        count = data[cont][1]
        name = cont
        emailid = data[cont][2]
        startdate = data[cont][0]
        output.append({
            "attendeeCount": count,
            "attendees": emailid,
            "name": cont,
            "startDate": data[cont][0]
        })

    return output


# Post the output to the respective url
def post_json_output(url, send_result):
    r = requests.post(url, data=json.dumps(send_result, indent=2))
    print(r)


if __name__ == "__main__":
    get_url = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=3ae2c123c8b723d348215b1b4f17'
    post_url = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=3ae2c123c8b723d348215b1b4f17'
# Get data from url
    data = get_data_json_format(get_url)

# Clean the data and get the desired data
    person_dates, country = parse_json_data(data)

# Find the start date and number of attendees
    final_output = find_start_date_for_country(person_dates, country)

# Post the output to the URL
    result = final_output_formatter(final_output)
    output = {"countries": result}
    print(json.dumps(output, indent=2))
    post_json_output(post_url, output)
