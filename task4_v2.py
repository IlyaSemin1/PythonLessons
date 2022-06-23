class Comparsion:
	def __init__(self, wordList):
		self.list = wordList

	def compare(self):
		for string1, string2 in self.list:
			ngrams = [
				string1[i:i+3] for i in range(len(string1))
			]
			count = 0
			for ngram in ngrams:
				count += string2.count(ngram)
			print('Сравниваются: '+ string1 +' и '+ string2 +'. Результат:', count/max(len(string1), len(string2)))

if __name__ == '__main__':

	comparison_list = [ 
		('непрестижность', 'непереносимость'), 
		('миелобластоз', 'боррелиоз'),
		('гидрофильтр', 'гидорцикл'), 
		('патриархия','матриархат'), 
		('форестьер','флибустьер'), 
		('спидофоб', 'правдоруб'), 
		('эхинацея','анимация'), 
		('анкилит', 'антилопа')
	]

	comparsion = Comparsion(comparison_list)
	comparsion.compare()

