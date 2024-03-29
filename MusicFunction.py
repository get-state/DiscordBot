import urllib.request
import urllib.parse
import re
import pafy
import youtube_dl

"""This whole code allows to search for the most popular result on youtube. 
Instead of displaying video it post link to the site.
The function get_youtube_url was based on code written by 
Grant Curell, 5 Feb 2015, "Python – Search Youtube for Video", 
https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video"""

"""This function looks for first YT url that pops out in the search results."""

def get_youtube_url():
    search_for = urllib.parse.urlencode({"search_query" : input("Search: ")})
    first_part_url = urllib.request.urlopen("http://www.youtube.com/results?" + search_for)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', first_part_url.read().decode())
    search_url = "http://www.youtube.com/watch?v=" + search_results[0]
    return search_url
    
"""This function looks for information about video form given url."""

def inofrmation_Video():
    url = get_youtube_url()
    video = pafy.new(url)
    return video,url
