from argparse import ArgumentParser

class SimpleArgObject(object):
  pass

'''
Reads out the default arguments of an ArgumentParser.
Option to include custom args in a dictionary.
Good for running argument-based processes in notebooks.
'''
def map_arg_to_defaults(args : ArgumentParser, custom_args : dict = None) -> SimpleArgObject:

  d_args = SimpleArgObject()
  for a in args._actions[1:]: # first action is 'help'
    setattr(d_args, a.dest, a.default)

  if custom_args is not None:
    for a in custom_args.keys():
        setattr(d_args, a, custom_args[a])

  return d_args