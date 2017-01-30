import players

tyler = players.QuarterBack()

print('Tyler as QB created succesfully!')

#tyler.printstats()

#print('Tyler stats printed succesfully!')

tyler.runplay(20)

print('Tyler runplay executed succesfully!')

tyler.printstats()

print('Tyler stats updated sucessfully!')

tyler.passplay(True, 45)

tyler.printstats()

print('Tyler pass complete updated!')

tyler.passplay(False)

tyler.printstats()

print('Tyler pass incomplete updated!')