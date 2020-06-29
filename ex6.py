# Joke Setup
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Joke Punchline
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print out the joke.
print(x)
print(y)

# Restate the joke, nesting the string as a variable inside an f-string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# The joke isn't funny, so use boolean.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# False is printed along with joke evaluation
print(joke_evaluation.format(hilarious))
