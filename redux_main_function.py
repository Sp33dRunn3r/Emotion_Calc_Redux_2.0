dict = {'Emotion':0, 'Name':None, 'Special_Event:':None, 'People_Surveyed':0,} #(Dictionary for data values)
#------------------------------------------------------------------------------------------------------------------->
def feel_question(): #(Function for retrieving numerical input value for individual)
    q_name = input("Hello! What is your name? ")
    while q_name == "" or q_name.isdigit():
        q_name = input('Please enter a real name... ') #(Name checker)
    for greeting in q_name:
        dict['Name'] = (q_name) #(dictionary value update)
        greeting = print('Hello,', q_name, 'nice to meet you!')
        break
    q_feel = input(f"How are you feeling today {q_name}? (From 1 to 10) ")
    while q_feel == "" or not q_feel.isdigit() or int(q_feel) > 10 or int(q_feel) < 1 or q_feel.startswith('0'):
            q_feel = input('Please enter a numeric value from 1 to 10 ') #(Value checker)
    for response in q_feel:
        dict['Emotion'] = (q_feel) #(dictionary value update)
        break

    return print(f'''I see you're feeling like a {q_feel}, thanks for sharing {q_name}!''')
#------------------------------------------------------------------------------------------------------------------->
def Initiator(): #(Program initiator)
    Survey_taker_num = input('''
    -----> If you would like to exit or close the program, press 'Q'

    -----> How many people would you like to survey today? ''') #(Question for survey amount)
    while Survey_taker_num == "" or Survey_taker_num.isalpha():
        Survey_taker_num = input('Please enter a valid response... ')

    for x in range(int(Survey_taker_num)): #(Statistics printed and number of surveys updated)
        feel_question()
        dict['People_Surveyed'] = x + 1
        print(f'''

    -----> Name:, {dict['Name']}
    -----> Emotional value for today: {dict['Emotion']}
    -----> Number of people surveyed: {dict['People_Surveyed']}

        ''')
#------------------------------------------------------------------------------------------------------------------->
Initializing_Question = input('Would another user like to Enter? (yes, no) ') #(Program initiator start)
for runner in Initializing_Question:
    if Initializing_Question.startswith('n'):
        runner = input('Would you like to exit the program? ') #(Program exit Confirmation)
        if runner.startswith('y'):
            print('Goodbye! Enjoy the rest of your week!')
            exit()
        while runner.startswith('n'):
            Initializing_Question = input('Would another user like to Enter? (yes, no) ') #(Program Initializing Confirmation)
            break
    while Initializing_Question.startswith('y'):
        Initiator()
        Initializing_Question = Initializing_Question = input('Would another user like to Enter? (yes, no) ') #(Program initiator start)
        break
