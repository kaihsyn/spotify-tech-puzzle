import time

class Problem():
	def __init__(self):
		self.num_cat = 0
		self.num_dog = 0
		self.num_vote = 0
		self.votes = []
		self.vote_stat = {}

	def vote_add(self, vote):
		self.votes.append(vote)
		
		if vote[0] in self.vote_stat:
			self.vote_stat[vote[0]]['like'] += 1
		else:
			self.vote_stat[vote[0]] = { 'like': 1, 'hate': 0 }

		if vote[1] in self.vote_stat:
			self.vote_stat[vote[1]]['hate'] += 1
		else:
			self.vote_stat[vote[1]] = { 'like': 0, 'hate': 1 }

	def vote_remove(self, vote):
		self.votes.remove(vote)
		self.vote_stat_remove(vote)

	def vote_remove_list(self, vote_list):
		self.votes = [vote for vote in self.votes if vote not in vote_list]
		for vote in vote_list:
			self.vote_stat_remove(vote)

	def vote_stat_remove(self, vote):
		self.vote_stat[vote[0]]['like'] -= 1
		self.vote_stat[vote[1]]['hate'] -= 1

class Result():
	def __init__(self):
		self.max = 0
		self.now = 0

def backtrack(res, prob):

	if res.now + len(prob.votes) <= res.max:
		return

	if len(prob.votes) == 0:
		if res.now > res.max:
			res.max = res.now
		return

	votes = list(prob.votes)

	while len(votes) > 0:
		# sort votes
		votes = sorted(votes, key=lambda v: prob.vote_stat[v[1]]['like'] + prob.vote_stat[v[0]]['hate'])

		# select one vote
		sel_vote = votes.pop(0)
		prob.vote_remove(sel_vote)

		# remove confilct
		del_votes = [vote for vote in prob.votes if vote[0] == sel_vote[1] or vote[1] == sel_vote[0]]
		prob.vote_remove_list(del_votes)

		for vote in prob.votes:
			if vote in votes:
				votes.remove(vote)

		res.now += 1
		backtrack(res, prob)
		res.now -= 1

		prob.vote_add(sel_vote)
		for vote in del_votes:
			prob.vote_add(vote)

	return

rounds = int(raw_input())
for i in xrange(rounds):
	prob = Problem()
	res = Result()

	prob.num_cat, prob.num_dogs, prob.num_votes = [int(j) for j in raw_input().split(' ')]

	for j in xrange(prob.num_votes):
		prob.vote_add(tuple([int(v[1:]) if v[:1] == 'C' else int(v[1:])+prob.num_cat for v in raw_input().split(' ')]))

	print 'Computing...'

	time1 = time.time()
	backtrack(res, prob)
	time2 = time.time()

	print res.max
	print time2 - time1
