# Harrible

The existing tools for analyzing web traffic are horrible if you are tracing more than a dozen ajax requests. Chrome/Safari/FF dev tools don't let you:

 * Delete/hide unimportant requests
 * Flag and annotate requests
 * See the whole path on a single line, not just the last segment ("filename")
 
Basically I need a spreadsheet. 

This is a trivial python script that selects some fields of a HAR file into CSV format. If you need different fields, edit the source. 

Usage: `python harrible.py < input.har > output.csv`

More info: http://www.softwareishard.com/blog/har-12-spec/