# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:49:06 2020

@author: simon
"""

import requests					# requesting webpages
from bs4 import BeautifulSoup 	# parsing html
import json
import optparse

parser = optparse.OptionParser('get-lszs')
parser.add_option('-o', '--outdir',	dest='outdir', help='[optional] output directory')
parser.add_option('-s', '--single-file',	action='store_true', dest='single', help='[optional] output directory')
(opts, args) = parser.parse_args()

def getLSGS(tabletyp):
    requrl = 'https://www.sionaeroport.ch/en/flights'
    # website currently does not require to send the headers
    response = requests.get(requrl)
    
    if(response.status_code != 200):
        print('error: Website returned status code: ' + str(response.status_code))
    
    keyword = 'arrivals-table'
    if('dep' in tabletyp.lower()):
        keyword = 'departures-table'
        
    
    # todo: remove hardcoded
    keyword = 'departures-table'
    
    
    parsed_html = BeautifulSoup(response.text, 'lxml')
    flt_table = parsed_html.find('table', {'id': keyword}).find('tbody')
    
    rows = flt_table.findAll('tr')
    # prepare json dict with empty array
    timetable = []
    
    for row in rows:
        print(row)
        entry = {}
        # Todo once flights increase again
        
    return timetable

"""
<tr class="no-flights-day">
<td colspan="7">
                                                                                          No flights scheduled today                                                                                     </td>
</tr>
<tr class="no-flights-day">
<td colspan="7">
                                                                                          No flights scheduled today                                                                                     </td>
</tr>
<tr class="no-flights-hour" style="display:none; width:100%">
<td colspan="7">
                                                                                     No flights corresponding this schedule                                                                                </td>
</tr>
<tr class="no-flights-day">
<td colspan="7">
                                                                                          No flights scheduled today                                                                                     </td>
</tr>
<tr class="no-flights-day">
<td colspan="7">
                                                                                          No flights scheduled today                                                                                     </td>
</tr>
<tr class="no-flights-hour" style="display:none; width:100%">
<td colspan="7">
                                                                                     No flights corresponding this schedule                                                                                </td>
</tr>
"""


def writeJsonFile(filename, data):
    with open(str(filename), 'w') as outfile:
        json.dump(data, outfile)
        
def getTime(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(json['page']['update_time'])
    except KeyError:
        return 0

#%%
def main():
    try:
        outdir = '.'
        if(opts.outdir is not None):
            outdir = opts.outdir
            
        table = {}
        table['data'] = []
        if(opts.single is not None):
            table['data'] = getLSGS('arr')
            table['data'] = table['data'] + getLSZB('dep')
            # sort by arrital time
            table['data'] = sorted(table['data'], key=lambda k: k['scheduledTime']) 
            writeJsonFile(outdir + '/timetable.json', table)
        else:
            table['data'] = getLSGS('arr')
            writeJsonFile(outdir + '/arrivals.timetable.json', table)
            table['data'] = getLSGS('dep')
            writeJsonFile(outdir + '/departures.timetable.json', table)
        
    except KeyboardInterrupt:
        print('')
        exit(0)


if __name__ == '__main__':
	main()
    
    