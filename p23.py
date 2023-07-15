#tiltle what is this module?
# #source code:  do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.

# 	it can't find it. this is an undocumented module.
# va gur snpr bs jung? looks like rot
from string import ascii_lowercase
text = 'va gur snpr bs jung?'
for i in range(26):
    translation_table = str.maketrans(ascii_lowercase,ascii_lowercase[i:]+ascii_lowercase[:i])
    result = text.translate(translation_table)
    print(result) #wee got lucky and found: in the face of what?
import this #because of the title
# strange line In the face of ambiguity
#next http://www.pythonchallenge.com/pc/hex/ambiguity.html





