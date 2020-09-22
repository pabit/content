import collections
import random

import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401

incident = demisto.incidents()
listData = demisto.executeCommand("getList", {"listName": "XSOAR Health - Failed Incidents Dates"})
listContent = list(listData[0].get('Contents').split(","))
datesOnlyList = []
for fulldate in listContent:
    dateonly = fulldate.split(" ")[0]
    datesOnlyList.append(dateonly)

listsdata = []
if listContent != ['']:
    listcollections = collections.Counter(datesOnlyList)
    topLists = listcollections.most_common(10)
    listsnumber = len(topLists)
    listbooknumber = 0
    listTrue = True
    while listbooknumber < listsnumber:
        for list_element in topLists:
            random_number = random.randint(0, 16777215)
            hex_number = str(hex(random_number))  # convert to hexadecimal
            color = '#' + hex_number[2:]  # remove 0x and prepend '#'
            listWidgetData = {
                "data": [
                    list_element[1]
                ],
                "name": str(list_element[0]),
                "color": color
            }
            listsdata.append(listWidgetData)
            listbooknumber = listbooknumber + 1

    demisto.results(json.dumps(listsdata))

else:
    data = {
        {
            "data": [
                0
            ],
            "name": "N\A",
                    "color": "#00CD33"
        },

    }
    demisto.results(json.dumps(data))
