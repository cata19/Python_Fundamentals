# import functions_with_arguments as f

# f.greeting('Ibrahim')
# f.user_guessing_game('27', 'stop')

from functions_with_arguments import name, greeting as g, user_guessing_game as game
from functions_with_arguments import Test

g('Ibrahim')
# game('20', 'stop')

print(name)
print(Test.a)

test_obj = Test()
print(test_obj.a)
