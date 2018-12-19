import urllib2

response = urllib2.urlopen("https://www.pokemon.com/us/pokedex/bulbasaur")

page = response.read()

out = open("html.txt", "w")
out.write(page)
out.close()

inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Height</span>"
	if search in x:
    	a =  next(inq)
    	a = ' '.join(a.split())
    	# print a
    	a = a[30:-7]
    	print "Height = " + a
inq.close()

inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Category</span>"
	if search in x:
    	a =  next(inq)
    	a = ' '.join(a.split())
    	# print a
    	a = a[30:-7]
    	print "Catogory = " + a
inq.close()

inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Weight</span>"
  	if search in x:
    	a =  next(inq)
    	a = ' '.join(a.split())
    	# print a
    	a = a[30:-7]
    	print "Weight = " + a
inq.close()