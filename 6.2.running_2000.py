import time

def timer(func, *args, **kwargs):
  """
  Messures the running time of a function

  Args:
      func (function): the function to messure the runtime

  Returns:
      float: the running time of the function
  """
  if len(args) > 0 and len(kwargs) > 0:
    start_time = time.time()
    func(*args,**kwargs)
  
  elif len(args) > 0  and not len(kwargs) > 0:
    start_time = time.time()
    func(*args)
    
  else:
    start_time = time.time()
    func(**kwargs)
    
  return time.time()- start_time