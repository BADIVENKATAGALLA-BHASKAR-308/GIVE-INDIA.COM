# #scraping of give india

# def give_india():
# 	import json
# 	import requests
# 	import pprint
# 	from bs4 import BeautifulSoup
# 	response = requests.get("https://www.giveindia.org/certified-indian-ngos")  #this link is working
# 	# print(response)
# 	soup = BeautifulSoup(response.text,"html.parser")
# 	#finding the list_of_ngo
# 	list_ = []
# 	dict_of_ngo = {}
# 	main_table = soup.find_all("table",class_="jsx-697282504")
# 	for td in main_table:
# 		sub_td = td.find_all("td",class_="jsx-697282504 nonprofit-name-desktop")
# 		for i in sub_td:
# 			row_tag = i.find("div",class_="row")
# 			list_.append(row_tag.text)


# 	# finding the list of states

# 	trs_list = []
# 	for i in main_table:
# 		trs = i.find_all("tr")
# 		count=0
# 		for j in trs:
# 			count+=1
# 			if count == 1:
# 				continue
# 			else:
# 				trs_list.append(j)
# 	list_of_states = []
# 	for tds in trs_list:
# 		tds_tags = tds.find_all("td")
# 		count_of_3rd_td = 0
# 		for k in tds_tags:
# 			count_of_3rd_td+=1
# 			if count_of_3rd_td == 3:
# 				list_of_states.append(k.text)

# 	#dict of combination of ngo and state
# 	for i in range(len(list_)):
# 		dict_of_ngo[list_[i]] = list_of_states[i]
# 	pprint.pprint(dict_of_ngo)

# 	#finding the unique states
# 	unique_states_list = []
# 	for i in list_of_states:
# 		if i not in unique_states_list:
# 			unique_states_list.append(i)
# 	#finding the individual count of state
# 	dict_of_repition = {}
# 	for i in unique_states_list:
# 		count_of_state = 0
# 		for j,k in dict_of_ngo.items():
# 			if k == i:
# 				count_of_state+=1
# 		dict_of_repition[i] = count_of_state
# 	print(dict_of_repition)

# 	#finding the another dictonery
# 	dict_of_repition_1 = {}
# 	for i in unique_states_list:
# 		list_of_state_ngo = []
# 		for j,k in dict_of_ngo.items():
# 			if k==i:
# 				list_of_state_ngo.append(j)
# 		dict_of_repition_1[i] = list_of_state_ngo
# 	pprint.pprint(dict_of_repition_1)
# 	# hai = input("enter the state_name:-")
# 	# for i,j in dict_of_repition_1.items():
# 	# 	if i == hai:
# 	# 		print("this are all the ngo s in this state:-",j)

# give_india()