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
		scores = []
		if len(word.strip()) == 0:
			word = self.syllable_repo[random.randrange(len(self.syllable_repo))]["syllable"]
		iterations = random.randrange(1,4)
		score_judge = 10000
		for i in range(iterations):
			candidates = []
			for s in self.syllable_repo:
				syllable = s["syllable"]
				if syllable[0] == word[-1] and s["cnt_score"] > score_judge:
					candidates.append(syllable)
			candidate = candidates[random.randrange(len(candidates))][1::]
			word += candidate
		return word


print(WordCreator("C://users/rojit/desktop/syllables.json").create_word())