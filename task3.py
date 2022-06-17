comparison_list = ['непрестижность', 'миелобластоз', 'гидрофильтр', 'патриархия', 'форестьер', 'спидофоб', 'эхинацея', 'анкилит']
comparison_default = 'автополироль'
str_elem_default = 'фи'

def compare(S1,S2):
	ngrams = [
		S1[i:i+3] for i in range(len(S1))
	]
	count = 0
	for ngram in ngrams:
		count += S2.count(ngram)

	return count/max(len(S1), len(S2))

if __name__ == '__main__':
	print(str(comparison_list), '\n========================================')
	for comp_item in comparison_list:
		print('сравниваются:' + comp_item +' и '+ comparison_default + '. Результат:', compare(comp_item, comparison_default))

	print("================================================\n"
		"Элементы, содержащие '"+str_elem_default+"':")

	for comp_item in comparison_list:
		if(comp_item.find(str_elem_default)!= -1):
			print(comp_item)




	