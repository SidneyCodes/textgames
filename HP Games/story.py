from random import choice as c #random choice
from random import randint as r #random number
import random

wizards = ['harry','ron','hermonie','snape','dobby','hagrid']
drink = ['butterbeer','pumpkin juice','firewhisky','water','milk','soda','giggle water','root beer','lemonade','old cauldron slime','sprite','muggle madness tea','almond milk']
pets = ['owl','cat','frog','dog','toad','lion','fish','chinchilla','hamster','shark','lizard','dragon','snake','mantis shrimp']
magical_animal = ['hippogriff','unicorn','house elf','sea dragon','basilisk','acromantula','phoenix']
item = ['wand','horcrux','cauldron','broom','snitch','bludger','waffle','book','sorting hat','sword of gryffindor']
places = ['hogsmead','hogswarts','diagon alley','london','privet drive','kings cross station','12 grimauld place','leaky cauldron','gringotts','weasley brothers joke shop','forbidden forest','the cabin of the hagrid']
color = ['metallic blue','red','orange','yellow','green','purple','invisible','a color that has no name','black','white','pink','beige','lavander']
weather = ['stormy','rainy','sunny','volcano-y','hailey','snowy','cloudy with a chance of meatballs and basilisk-y']

random.shuffle(wizards)

print(f'The weather was {c(weather)}... and the sky was {c(color)}')
print(f'{c(wizards).title()} had a tiny {c(color)} {c(pets)} that turned into a {c(color)} {c(magical_animal)} because it was {c(weather)} and this is that story')
print(f'One day, the {c(color)} {c(pets)} was a flexible {c(color)} and {c(color)} {c(pets)} and started doing magic and turned the house {c(color)}')
print(f'This was a problem because the {c(color)} {c(pets)} ate {c(wizards).title()}s {c(color)} {c(item)}. {c(wizards).title()}s mom was MAD! She was so mad she turned {c(color)}!')
print(f'{c(wizards).title()} has to move to {c(places).title()} and turn into a {c(pets)}, the problem is that the spell backfired and he turned into a {c(color)} {c(magical_animal)}')
print(f'{c(wizards).title()} ran to {c(places).title()} and picked up an emergency {c(color)} {c(item)} which helped turn him back into a wizard')
print(f'{c(wizards).title()} was very thirsty so he drank some {c(color)} {c(drink)} and this turned him into {c(wizards).title()}, this was a problem, because suddently he wanted to eat a {c(color)} {c(magical_animal)}')
print(f'{c(wizards).title()} looked in the mirror. {c(wizards).title()} was now {c(wizards).title()}! This was impossible! {c(wizards).title()} was now {c(wizards).title()}! This was impossible! {c(wizards).title()} was now {c(wizards).title()}! Oh, and {c(wizards).title()} was also {c(color)}!')
print(f'Ok, so everyone needed to fix this. {c(wizards).title()} and {c(wizards).title()} met up with a {c(color)} {c(magical_animal)} and brought {r(2,500)} {c(color)} {c(item)}s and saved the day')
print(f'Ok, a second emergency, {c(wizards).title()}, now changed back, ate a {c(color)} {c(item)} and turned into a {c(color)} {c(magical_animal)} and accidently ate a {c(color)} {c(pets)}')
print(f'Finally, it all worked out and {c(wizards).title()} turned back into {c(wizards).title()}, but {c(wizards).title()} was never the same again.')
print(f'The best lesson from this is never use a {c(color)} {c(item)} in {c(places)} while drinking {c(color)} {c(drink)}, and never, never snack on a {c(color)} {c(pets)} or {c(color)} {c(magical_animal)}\n')
print(f'{c(wizards).title()} also found out that drinking {c(color)} {c(drink)} is a terrible idea because you may get transported to {c(places).title()} and turn into {c(wizards).title()}')
print(f'Let me tell you why {c(wizards).title()} is actually the evil twin of {c(wizards).title()} trying to take over the world with a {c(item)}, but only when its {c(weather)}')

