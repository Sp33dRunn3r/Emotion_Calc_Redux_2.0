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

    -----> Name: {dict['Name']}
    -----> Emotional value for today: {dict['Emotion']}
    -----> Number of people surveyed: {dict['People_Surveyed']}

        ''')
#------------------------------------------------------------------------------------------------------------------->
