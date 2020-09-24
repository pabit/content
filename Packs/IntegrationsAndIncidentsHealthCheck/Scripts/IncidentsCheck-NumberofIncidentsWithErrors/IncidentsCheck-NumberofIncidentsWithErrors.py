import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401

RED_HTML_STYLE = "color:#FF1744;text-align:center;font-size:800%;>"
GREEN_HTML_STYLE = "color:#00CD33;text-align:center;font-size:800%;>"

incident = demisto.incidents()
query = incident[0].get('CustomFields', {}).get('numberoffailedincidents', 0)

if str(query) != '0':
    html = f"<h1 style={RED_HTML_STYLE}{str(query)}</h1>"

else:
    html = f"<h1 style={GREEN_HTML_STYLE}0 </h1>"

demisto.results({
    'ContentsFormat': formats['html'],
    'Type': entryTypes['note'],
    'Contents': html
})
