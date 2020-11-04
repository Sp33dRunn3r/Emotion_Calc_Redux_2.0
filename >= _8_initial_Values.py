#(First set of numerical values coordinating with emotion for day)
if int(qemtn) >= 8:
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
  
#(Coordinating responses may be changed or modified in the future for more efficient data storage)
