#!/usr/local/bin/python3
#
# Reads stdin, writes to stdout

import csv
import json
import sys

root = json.load(sys.stdin)
output = csv.writer(sys.stdout)

output.writerow([
	'STARTED',
	'METHOD',
	'URL',
	'QUERY',
	'POSTDATA',
	'CODE',
	'RESPONSE',
	'TIME',
	'FULLURL'
])

def dump_content(content):
	if content == None:
		return ''
	elif content.get('mimeType').startswith('application/json'):
		return content.get('text')
	elif content.get('mimeType').startswith('application/x-www-form-urlencoded'):
		return content.get('text')
	else:
		return content.get('mimeType')

for entry in root['log']['entries']:
	request = entry['request']
	response = entry['response']

	split_query = request['url'].split('?')

	output.writerow([
		entry['startedDateTime'],

		request['method'],
		split_query[0],
		'' if len(split_query) < 2 else split_query[1],
		dump_content(request.get('postData')),

		str(response['status']) + ' ' + response['statusText'],
		dump_content(response['content']),

		entry['time'],
		request['url']
	])