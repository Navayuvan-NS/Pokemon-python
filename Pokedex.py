import urllib2

response = urllib2.urlopen("https://www.pokemon.com/us/pokedex/jigglypuff")

page = response.read()

out = open("html.txt", "w")
out.write(page)
out.close()

q = 0
inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Height</span>"

	if search in x:
		q = q + 1
	if search in x and q == 1:
		a =  next(inq)
		a = ' '.join(a.split())
		# print a
		a = a[30:-7]
		print "Height = " + a
inq.close()

q = 0
inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Category</span>"
	if search in x:
		q = q + 1
	if search in x and q == 1:
		a =  next(inq)
		a = ' '.join(a.split())
		# print a
		a = a[30:-7]
		print "Catogory = " + a
inq.close()

q = 0
inq = open("html.txt", "r")
for x in inq:
	search = "<span class=\"attribute-title\">Weight</span>"
	if search in x:
		q = q + 1
	if search in x and q == 1:
		a =  next(inq)
		a = ' '.join(a.split())
		# print a
		a = a[30:-7]
		print "Weight = " + a
inq.close()


inq = open("html.txt", "r")
q = 0
for x in inq:
	search = "<span class=\"attribute-title\">Abilities</span>"
  	if search in x:
		q = q + 1
	
	searcht = "<span class=\"attribute-value\">"
	if searcht in x and q == 1:
		a = ' '.join(x.split())
		a = a[30:-7]
		print "Abilities " + a
	if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
		break
inq.close()

inq = open("html.txt", "r")
q = 0
for x in inq:
	search = "<div class=\"dtm-type\">"
  	if search in x:
		q = q + 1
	
	searcht = "<a href=\"/us/pokedex/?type"
	if searcht in x and q == 1:
		a1 = ' '.join(x.split())
		a1 = a1[27:-4]
		a = ""
		for w in range(len(a1)):
			if a1[w] == "\"":
				break
			else:
				a = a+a1[w]

		print "Type " + a
	if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
		break
inq.close()

inq = open("html.txt", "r")
q = 0
for x in inq:
	search = "<div class=\"dtm-weaknesses\">"
  	if search in x:
		q = q + 1
		print "yes"

	#searcht = "?weakness="
	#if searcht in x and q == 1:
	#		print "yes"

	#	print "Type " + a
	if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
		break
	else:
		print x
inq.close()


