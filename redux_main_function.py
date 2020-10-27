#(Dictionary for data values)
dict = {'Emotion':0, 'Name':None, 'Special_Event:': 'Nothing out of the ordinary has happened today.'}

def feel_question(): #(Function for retrieving numerical input value for individual)
    q_name = input("Hello! What is your name? ")
    while q_name == "" or q_name.isdigit():
        q_name = input('Please enter a real name... ') #(Name checker)
    for greeting in q_name:
        dict['Name'] = (q_name) #(dictionary value update)
        greeting = print('Hello,', q_name, 'nice to meet you!')
        break
    q_feel = input(f"How are you feeling today {q_name}? (From 1 to 10)")
    while q_feel == "" or not q_feel.isdigit() or int(q_feel) > 10 or int(q_feel) < 1 or q_feel.startswith('0'):
            q_feel = input('Please enter a numeric value from 1 to 10 ') #(Value checker)
    for response in q_feel:
        dict['Emotion'] = (q_name) #(dictionary value update)
        break

    return print(f"I see you're feeling like a {q_feel}, thanks for sharing {q_name}!")

feel_question()
