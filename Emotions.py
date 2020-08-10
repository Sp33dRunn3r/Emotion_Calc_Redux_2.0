#Emotion values Dictionary:
dict = {'key1':0, 'Name':None, 'Special_Event:': 'Nothing out of the ordinary has happened today.'}
prsn_cnt = 0
#Initiator start:
q_reup = input('Would another user like to Enter? (yes, no) ')
for runner in q_reup:
    if q_reup.startswith('n'):
        runner = input('Would you like to exit the program? ')
        if runner.startswith('y'):
            print('Goodbye! Have a nice rest of your week!')
            exit()
        while runner.startswith('n'):
            q_reup = input('Would another user like to Enter? (yes, no) ')
            break
    while q_reup.startswith('y'):
        #Variable for name input:
        qname = input('Hello, what is your name? ')
        #Output condition execution for name value:
        while qname == "" or qname.isdigit():
            qname = input('Please enter a real name... ')
            qname = qname
        for greeting in qname:
            dict['Name'] = (qname)
            greeting = print('Hello,', qname, 'nice to meet you!')
            break

        #Variable for numerical emtn input:
        qemtn = input('How are you feeling today? (From 1 to 10) ')
        #Output condition execution for emtn value:

        while qemtn == "" or not qemtn.isdigit() or int(qemtn) > 10 or int(qemtn) < 1 or qemtn.startswith('0'):
            qemtn = input('Please enter a numeric value from 1 to 10 ')
            qemtn = qemtn
        for response in qemtn:
            response = print('I see you\'re feeling like a', qemtn, 'Thanks for sharing!')
            break


        #Determiner for numerical value output:
        for dtrmn in qemtn:
            if int(qemtn) == 10:
                dict['key1'] = (qemtn)
                dtrmn = input('Did something special happen today? (yes, no) ')
        #Follow up to determiner extremes (numerical values: 10)
                if dtrmn.startswith('n'):
                    dtrmn = print('It seems nothing out of the ordinary happened for you today.')
                    dtrmn = dtrmn
                    break
                elif dtrmn.startswith('y'):
                    dtrmn = input('Tell me! What happened today?? ')
                    dict['Special_Event:'] = (dtrmn)
                    dtrmn = dtrmn
                    break
            elif int(qemtn) == 1:
                dict['key1'] = (qemtn)
                dtrmn = input('Did something sad happen today? (yes, no) ')
        #Follow up to determiner extremes (numerical values: 1)
                if dtrmn.startswith('n'):
                    dtrmn = print('It seems nothing out of the ordinary happened for you today.')
                    dtrmn = dtrmn
                    break
                elif dtrmn.startswith('y'):
                    dtrmn = input('If you\'d like to share... what happened today? ')
                    dict['Special_Event:'] = (dtrmn)
                    dtrmn = dtrmn
                    break
            elif int(qemtn) >= 8:
                dict['key1'] = (qemtn)
                dtrmn = print('So glad to hear your feeling well today!')
            elif int(qemtn) <= 3:
                dict['key1'] = (qemtn)
                dtrmn = print('So sorry to hear your not feeling well today!')
            elif int(qemtn) < 5:
                dict['key1'] = (qemtn)
                dtrmn = print('Sorry to hear your not feeling well.')
            elif int(qemtn) == 5:
                dict['key1'] = (qemtn)
                dtrmn = print('Somewhere in the middle it seems... interesting.')
            elif int(qemtn) > 5:
                dict['key1'] = (qemtn)
                dtrmn = print('Glad to hear your feeling well today.')


        #Dictionary statistics stated)
        print('Name:',dict['Name'])
        print('Emotion scale for today:',dict['key1'])
        print('Special Event:','"',dict['Special_Event:'],'"')
        print('All finished!')
        prsn_cnt = prsn_cnt + 1
        print("Number of People Inputed:", prsn_cnt)
        q_reup = input('Would another user like to Enter? (yes, no) ')
        break
