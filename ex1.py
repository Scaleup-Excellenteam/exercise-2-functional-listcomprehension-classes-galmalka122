from functools import wraps
    
def type_check(correct_type):
  """
  A decorator factory that returns a decorator that checks if the parameter
  Passed to the decorated function is of the correct type.
  If it is not, a custom TypeError is raised.

  Args:
    correct_type (type): The expected type of the parameter.

  Returns:
      decorator (function): A decorator that takes a function and returns a 
      Wrapped function that checks if the parameterpassed to the function
      Is of the correct type.

  Raises:
      TypeError: If the parameter passed to the decorated function is not of the correct type.

  Example:
      >>> @type_check(int)
      ... def times2(num):
      ...     return num * 2
      ...
      >>> times2(2)
      4
      >>> times2('2')
      TypeError: Expected argument of type int, but got str
  """
  def decorator(func):
    @wraps(func)
    def wrapper(arg):
      if not isinstance(arg, correct_type):
        raise TypeError(f"Expected argument of type {correct_type.__name__}, but got {type(arg).__name__}")
      return func(arg)
    return wrapper
  return decorator
