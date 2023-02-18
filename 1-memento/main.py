from document import Document
from history import History

history = History()
mydocument = Document('first content', 'first font', 12)
history.push(mydocument.create_state())

print(mydocument)

mydocument.content = 'second content'
history.push(mydocument.create_state())

print(mydocument)

mydocument.fontSize = 14
history.push(mydocument.create_state())

print(mydocument)

mydocument.fontName = 'second font'

print(mydocument)
print('using history')

mydocument.restore_state(history.pop())
print(mydocument)

mydocument.restore_state(history.pop())
print(mydocument)

mydocument.restore_state(history.pop())
print(mydocument)
