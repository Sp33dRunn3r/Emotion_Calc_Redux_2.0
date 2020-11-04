#(A function that contains the coordinating responses for each numerical emotional value)
#------------------------------------------------------------------------------------------------------------------->
def Emotional_Input_Variable(): #(Numerical Values for user input)
    if int(qemtn) >= 8:
        dtrmn = print('So glad to hear your feeling well today!')
    elif int(qemtn) <= 3:
        dtrmn = print('So sorry to hear your not feeling well today!')
    elif int(qemtn) < 5:
        dtrmn = print('Sorry to hear your not feeling well.')
    elif int(qemtn) == 5:
        dtrmn = print('Somewhere in the middle it seems... interesting.')
    elif int(qemtn) > 5:
        dtrmn = print('Glad to hear your feeling well today.')
    return dtrmn
#------------------------------------------------------------------------------------------------------------------->
