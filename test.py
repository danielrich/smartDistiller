
class root():
   name = "root"


class branch(root):
   name = "branch"

   def growLeaves(self):
      print ("Grow Leaves")



def dropOldLeaves(fn):
   def wrapped(self):
      print ("drop Old leaves")
      fn(self)
   return wrapped


def dropOldLeavesAgain(self, fn):
   def wrapped():
      print ("drop Old leaves again")
      fn(self)
   return wrapped

b = branch()
branch.growLeaves = dropOldLeaves(branch.growLeaves)

b2 = branch()
