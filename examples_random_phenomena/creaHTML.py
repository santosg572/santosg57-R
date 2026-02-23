dd1 = '''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
'''
#<h1>This is a Heading</h1>
#<p>This is a paragraph.</p>

dd2 = '''
</body>
</html> 
'''

filin = open('dir.txt', 'r')
filon = open('sal.html', 'w')

dd = filin.readlines()

filon.write(dd1)

for ss in dd:
  ss2 = '<img src="' + ss + '" alt="Girl in a jacket">'
  filon.write(ss2)

filon.write(dd2)
filon.close()


