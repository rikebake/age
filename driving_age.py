driving = input('did you drive(Yes/No)')
# if this portion was not added , the cmd will jump to 'what is your age ' no matter what user input
if driving != 'Yes' and driving != 'No':
	print('hey, input Yes or No')
	raise SystemExit # this is to trigger "exit system" caused by error


age = int(input('what is your age?'))
if driving == 'Yes':
	if age >= 18:
		print('you passed the exam')
	else:
		print('weired')
elif driving == 'No':
	if age >= 18:
		print('you can apply for exam')
	else:
		print('Be patient')
#else:
#	print('hey, input Yes or No')