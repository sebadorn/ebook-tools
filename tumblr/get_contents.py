#!/usr/bin/env python

import os, sys
sys.path.append( os.path.join( os.path.dirname( __file__ ), "pytumblr" ) )

import codecs
import pytumblr


api_key = ""
blog = "blastron01"
tag_filter = "kumoko"


def cmpTimestamp( a, b ):
	return a["timestamp"] - b["timestamp"]


if __name__ == "__main__":

	client = pytumblr.TumblrRestClient( api_key )

	limit = 50
	iterations = 3

	chapters = []

	if not os.path.isdir( "downloads" ):
		os.mkdir( "downloads" )

	for i in range( iterations ):
		result = client.posts( blog, limit = limit, type = "text", tag = tag_filter, offset = i * limit )

		if "posts" not in result:
			print( "  - No posts in the result:" )
			print( result )
			break

		for post in result["posts"]:
			if tag_filter in post["tags"] and bool( post["body"] ):
				print( "  - Received post: \"%s\"" % ( post["title"] ) )
				chapters.append( post )

	print( "" )
	print( "  - Sort by timestamp." )
	chapters = sorted( chapters, cmp = cmpTimestamp )
	print( "" )

	j = 1

	for chapter in chapters:
		fName = str( j ).zfill( 4 ) + ".html"

		out = codecs.open( "downloads/" + fName, "w", "utf-8" )
		out.write( chapter["body"] )
		out.close()

		j += 1
		print( "  - Wrote file: \"%s\" -> \"%s\"" % ( chapter["title"], fName ) )
