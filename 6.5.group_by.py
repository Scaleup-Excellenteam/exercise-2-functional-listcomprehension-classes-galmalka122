def group_by(func, iteratable):
  """
  Creates a dictionary where each key is the value returnd
  From the function and each value is a list of the arguments
  Which are equales to the key.

  Args:
      func (function): the function to apply each argument.
      iteratable (any): the arguments to pass to the function.

  Returns:
      dict: Dictionary where the values grouped by the returned
            Function value.
  """
  grouped_by = {}
  key_value_tuples = [(func(value), value) for value in iteratable]
  for x,y in key_value_tuples:
    grouped_by.setdefault(x,[]).append(y)
  return grouped_by