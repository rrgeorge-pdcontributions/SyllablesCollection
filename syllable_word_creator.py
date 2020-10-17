import psycopg2
import random
import json

class WordCreator:
	def __init__(self,repo_path,word_len=None,start_word=None):
		self.word_len = word_len
		self.start_word = start_word
		self.syllable_repo = None
		with open(repo_path,"r",encoding="utf-8") as f:
			self.syllable_repo = json.loads(f.read())["data"]
		self.score_judge = 10000
		self.min_iterations  = 2
		self.max_iterations = 10

	def get_syllables_matches(self,word):
		matches = []
		for s in self.syllable_repo:
			if s["syllable"][0] == word[-1]:
				matches.append(s[syllable])
		return matches

	def create_word(self):
		word = ""
		if self.start_word !=None:
			word = self.start_word
		if len(word.strip()) == 0:
			satisfied = False
			while satisfied == False:
				rint = random.randrange(len(self.syllable_repo))
				if self.syllable_repo[rint]["cnt_score"] >= self.score_judge:
					word = self.syllable_repo[rint]["syllable"]
					break
		iterations = random.randrange(self.min_iterations,self.max_iterations)
		for i in range(iterations):
			candidates = []
			for s in self.syllable_repo:
				syllable = s["syllable"]
				if syllable[0] == word[-1] and s["cnt_score"] >= self.score_judge:
					candidates.append(syllable)
			try:
				candidate = candidates[random.randrange(len(candidates))][1::]
			except:
				break
			word += candidate
			if len(word) < 4:
				iterations += random.randrange(1,self.max_iterations//2)
		return word

	def create_word_wrt_posiscores(self):
		word = ""
		if self.start_word !=None:
			word = self.start_word
		if len(word.strip()) == 0:
			satisfied = False
			while satisfied == False:
				rint = random.randrange(len(self.syllable_repo))
				if self.syllable_repo[rint]["cnt_score"] >= self.score_judge and self.syllable_repo[rint]["start"] > self.syllable_repo[rint]["end"] and self.syllable_repo[rint]["start"] > self.syllable_repo[rint]["middle"]:
					word = self.syllable_repo[rint]["syllable"]
					break
		iterations = random.randrange(self.min_iterations,self.max_iterations)
		for i in range(iterations):
			random.shuffle(self.syllable_repo)
			candidates = []
			for s in self.syllable_repo:
				syllable = s["syllable"]
				if syllable[0] == word[-1] and s["cnt_score"] >= self.score_judge:
					if i != iterations - 1:
						if s["middle"] > s["start"] and s["middle"] > s["end"]:
							candidates.append(syllable)
					else:
						if s["end"] > s["start"] and s["end"] > s["middle"]:
							candidates.append(syllable)
			try:
				candidate = candidates[random.randrange(len(candidates))][1::]
			except:
				break
			word += candidate
			if len(word) < 4:
				iterations += random.randrange(1,self.max_iterations//2)
		return word



for i in range(10):
	print(WordCreator("C://users/rojit/desktop/syllables.json").create_word())
print("="*30)
for i in range(10):
	print(WordCreator("C://users/rojit/desktop/syllables.json").create_word_wrt_posiscores())
	#can retrive atleast one word that sounds completely sane
