# from shuffle import random
states = {'Washington':'Olympia','Oregon':'Salem',\
                    'California':'Sacramento','Ohio':'Columbus',\
                    'Nebraska':'Lincoln','Colorado':'Denver',\
                    'Michigan':'Lansing','Massachusetts':'Boston',\
                    'Florida':'Tallahassee','Texas':'Austin',\
                    'Oklahoma':'Oklahoma City','Hawaii':'Honolulu',\
                    'Alaska':'Juneau','Utah':'Salt Lake City',\
                    'New Mexico':'Santa Fe','North Dakota':'Bismarck',\
                    'South Dakota':'Pierre','West Virginia':'Charleston',\
                    'Virginia':'Richmond','New Jersey':'Trenton',\
                    'Minnesota':'Saint Paul','Illinois':'Springfield',\
                    'Indiana':'Indianapolis','Kentucky':'Frankfort',\
                    'Tennessee':'Nashville','Georgia':'Atlanta',\
                    'Alabama':'Montgomery','Mississippi':'Jackson',\
                    'North Carolina':'Raleigh','South Carolina':'Columbia',\
                    'Maine':'Augusta','Vermont':'Montpelier',\
                    'New Hampshire':'Concord','Connecticut':'Hartford',\
                    'Rhode Island':'Providence','Wyoming':'Cheyenne',\
                    'Montana':'Helena','Kansas':'Topeka',\
                    'Iowa':'Des Moines','Pennsylvania':'Harrisburg',\
                    'Maryland':'Annapolis','Missouri':'Jefferson City',\
                    'Arizona':'Phoenix','Nevada':'Carson City',\
                    'New York':'Albany','Wisconsin':'Madison',\
                    'Delaware':'Dover','Idaho':'Boise',\
                    'Arkansas':'Little Rock','Louisiana':'Baton Rouge'}

states_test = {'Texas':'Austin', 'North Carolina':'Raleigh', 'Idaho':'Boise'}

correct = 0
wrong = 0
for key in states_test:
	print(key)
	answer = input('What is the capital? ')
	if answer == states_test[key]:
		print('Great job!');
		correct += 1;
	elif answer != states_test[key]:
		print('Oops! You missed it. That\'s ok! Keep practicing!');
		wrong += 1;
	
print('You scored:', correct, 'points and missed:', wrong, 'questions.')