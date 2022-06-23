class Comparison:
	string1 = None
	string2 = None
	def compare(self, string1, string2):
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

	comparison_01 = Comparison()		
	for word1, word2 in comparison_list:
		comparison_01.string1 = word1
		comparison_01.string2 = word2
		comparison_01.compare(comparison_01.string1, comparison_01.string2)

