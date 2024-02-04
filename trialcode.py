'''
#Still trying to grasp...mmmmh!!!!
# Function to produce infinite Fibonacci numbers
def fibonacci():
  # Generate first number
  a = 1
  yield a

  # Generate second number
  b = 1
  yield b

  # Infinite loop
  while True:
    # Return sum of a + b
    c = a + b
    yield c
    # Function resumes loop here on next call
    a = b
    b = c

# Iterate through the Fibonacci sequence until a limit is reached
for num in fibonacci():
  if num > 50:
    break
  print(num)
'''
#help(dir())
import simple_to_do_list
#import simple_calculator

#simple_to_do_list.main()

