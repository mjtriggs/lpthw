name = 'Zed A. Shaw'
age = 35
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % hair

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height, weight,
  age + height + weight)

print "In kilograms, %s weighs %d kg." % (name, weight / 2.2)
print "In metres, %s is %f m tall." % (name, height * 0.0254)
# %f is for floating point
