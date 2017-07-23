months = ['Jan','Feb','Mar','Apr']
months.append ('May')
months.append('Jul')
print 'adding May & Jul',months
months.insert(5,'Jun')
print 'inserting june',months
print 'index of May is',months.index('May')
months.remove('Jun')
print 'Jun is removed.The new list is',months
months.sort()
print 'sorted list is',months
months.reverse()
print 'reverse list is',months
