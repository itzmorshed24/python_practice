subject = {'Bangla', 'English', 'Science'}
subjects = {'Bangla', 'English', 'Math', 'Physics'}

#union
result = subject.union(subjects)
print(result)

#intersection
results = subject.intersection(subjects)
print(results)

#add()
subject.add('Math')
print(subject)

#update([])
subject.update(['Physics','Chemistry'])
print(subject)

#remove()
subject.remove('Math')
print(subject)

#discard()
subject.discard("Physics")
print(subject)

#pop()
subject.pop()
print(subject)

