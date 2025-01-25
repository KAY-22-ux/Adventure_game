# This program generates an amazing story using additional
# words provided by the user and ensures appropriate articles are used before a noun.


#variable to store user inputs
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
color = input("color: ")
animal_food = input("animal's food: ")
name = input("Enter your full name: ")


#function to determine appropriate article
def determine_article(user_word):
    if user_word[0].lower() in 'aeiou':
        return "an"  
    else :
        return "a"


#story sample with user inputs
print("")
print(f'''Your Story is :
      
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family. Later, to our surprise, we realized
the {animal} turned out to have {determine_article(color)} {color} ropes tied around it and was in search of {animal_food}.
After, we went home and everything was back to normal.
                        
                        compiled by {name}''')

