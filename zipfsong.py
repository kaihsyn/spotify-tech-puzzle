import operator

album = []
my_input = raw_input().split(' ')

for i in xrange(1, int(my_input[0]) + 1):
	song = raw_input().split(' ')
	song[0] = int(song[0]) * i
	album.append(song)

sorted_album = sorted(album, key=operator.itemgetter(0), reverse=True)

for i in xrange(int(my_input[1])):
	print sorted_album[i][1]
