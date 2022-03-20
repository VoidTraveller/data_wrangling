ppp_late = open('public_150k_plus_080820.csv','r')
ppp_recent = open('public_150k_plus_recent.csv','r')

print('August file(late) has ' + str(len(ppp_late.readlines())) + ' rows.')
print('Recent file has ' + str(len(ppp_recent.readlines())) + ' rows.')
