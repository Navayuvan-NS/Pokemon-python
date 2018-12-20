import urllib2

def getUrl(dictn, name, typel):

	
	response = urllib2.urlopen("https://www.pokemon.com/us/pokedex/"+name)

	page = response.read()

	out = open("html.txt", "w")
	out.write(page)
	out.close()
	name = name[:-4]
	dictn[name] = {}
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
			dictn[name]['Height'] = a
			#print "Height = " + a
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
			#print "Catogory = " + a
			dictn[name]['Category'] = a
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
			#print "Weight = " + a
			dictn[name]['Weight'] = a
	inq.close()


	inq = open("html.txt", "r")
	q = 0
	t = ""
	for x in inq:
		search = "<span class=\"attribute-title\">Abilities</span>"
	  	if search in x:
			q = q + 1
		
		searcht = "<span class=\"attribute-value\">"
		if searcht in x and q == 1:
			a = ' '.join(x.split())
			a = a[30:-7]
			#print "Abilities " + a
			t = t + a + ", "
		if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
			break
	t = t[:-2]
	dictn[name]['Abilities'] = t
	inq.close()

	inq = open("html.txt", "r")
	q = 0
	t = ""
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
			if a not in typel:
				typel.append(a)
			#print "Type " + a
			t = t + a + ", "
		if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
			break
	t = t[:-2]
	dictn[name]['Type'] = t
	inq.close()

	inq = open("html.txt", "r")
	q = 0
	t= ""
	for x in inq:
		search = "<div class=\"dtm-weaknesses\">"
	  	if search in x:
			q = q + 1

		searcht = "<span>"
		if searcht in x and q == 1:
			
			a1 = ' '.join(x.split())
			a1 = a1[6:]
			#print "Weakness " + a1 
			t = t + a1 + ", "

		if( q == 1) and ("</div>" in ' '.join(next(inq).split())):
			break
	t = t[:-2]
	dictn[name]['Weakness'] = t
	inq.close()

	return dictn, typel

dictn = {}
typel = []
file = open("all_pokemon.txt", "r")
for x in file:
	dictn, typel = getUrl(dictn, x, typel)

print dictn

print "Type :", typel