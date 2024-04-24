# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
  # define the function here
  mn = min(example_list)
  print(mn)
  mx = max(example_list)
  print(mx)
  avg = sum(example_list) / len(example_list)
  print(avg)

# call the function below here
stats(example_list)