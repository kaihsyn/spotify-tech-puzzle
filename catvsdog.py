import time

class Problem():
	def __init__(self):
		self.num_cat = 0
		self.num_dog = 0
		self.num_vote = 0
		self.votes = []

class Result():
	def __init__(self):
		self.max = 0
		self.now = 0

def backtrack(res, prob):

	if len(prob.votes) == 0:
		if res.now > res.max:
			res.max = res.now
		return
	"""
	# select one vote
	sel_vote = prob.votes.pop(0)

	# remove conflict votes
	left_votes = []
	for vote in prob.votes:
		if vote[0] == sel_vote[1] or vote[1] == sel_vote[0]:
			prob.vote.remove(vote)
			left_votes.append(vote)

	res.now += 1
	backtrack(res, prob)
	res.now -= 1

	# put them back
	prob.votes.append(sel_vote)
	prob.votes += left_votes
	"""
	votes = list(prob.votes)

	while len(votes) > 0:
		# select one vote
		sel_vote = votes.pop(0)
		prob.votes.remove(sel_vote)

		# remove confilct
		del_votes = []
		for vote in prob.votes:
			if vote[0] == sel_vote[1] or vote[1] == sel_vote[0]:
				prob.votes.remove(vote)
				del_votes.append(vote)
			elif vote in votes:
				votes.remove(vote)

		res.now += 1
		backtrack(res, prob)
		res.now -= 1

		prob.votes.append(sel_vote)
		prob.votes += del_votes

	return

rounds = int(raw_input())
for i in xrange(rounds):
	prob = Problem()
	res = Result()

	prob.num_cat, prob.num_dogs, prob.num_votes = [int(j) for j in raw_input().split(' ')]

	for j in xrange(prob.num_votes):
		prob.votes.append(tuple([int(v[1:]) if v[:1] == 'C' else int(v[1:])+prob.num_cat for v in raw_input().split(' ')]))

	prob.votes = sorted(prob.votes)

	time1 = time.time()
	backtrack(res, prob)
	time2 = time.time()

	print res.max
	print time2 - time1
