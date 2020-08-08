gender = {
    'Suresh':'male',
    'Mamatha':'female',
    'Natasha':'female',
    'Bhargava':'male',    
    'Messi' : 'male'
            }
name = raw_input('enter whose gender you would like to know:')
  
if name in gender:
   print "Gender of %s is %s" % (name, gender[name])
else:
   print " %s does not exit " % (name)
