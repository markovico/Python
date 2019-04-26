import math

string = 'hello'

pi = 3.14
print(math.sin(pi/2.0))
print(string.upper())

story = """
        Roses are {colour}
        Violets are {colour2}
        Sugar is {adjective}
        Ando so are you
        """

"""
        Roses are {colour}
        Violets are {colour2}
        Sugar is {adjective}
        Ando so are you
"""

#provide missing words
c1 = input("Give me colour : ")
c2 = input ("Give me another colour : ")
adj = input ("and an adjective : ")
#display story
#print(story.format(c1, c2, adj))

print(story.format(colour=c1, colour2=c2, adjective=adj))


story3 = f"""
        Roses are {c1}
        Violets are {c2} 
        Sugar is {adj}
        Ando so are you
        """

print(story3)
