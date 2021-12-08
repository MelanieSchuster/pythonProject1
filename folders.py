import os.path

print(__file__)
python_folder = os.path.dirname(__file__)
print(python_folder)

sum_bytes = 0
for file in os.listdir(python_folder):
    if os.path.isfile(file):
        #folders are not treated
        print(file)
        #print(os.stat(file))
        sum_bytes += os.path.getsize(file)
        print(os.path.getsize(file))
print('Sum space: {}'.format(sum_bytes))

def sum_space(some_folder):
    sum_bytes = 0
    for file in os.listdir(some_folder):
        f = os.path.join(some_folder, file)
        if os.path.isfile(f):
            sum_bytes += os.path.getsize(f)
        else:
            sum_bytes += sum_space(f)
        return sum_bytes
some_folder = 'C:/Users/schus/Documents/Bewerbungsunterlagen'
print(some_folder)
print('Sum space: {}'.format(sum_space(some_folder)))


# 1. include summing space occupied for folders with their content
# Hint: use recursion
# step 1: create a function that iterates over files in a folder and returns the sum of the size
# step 2: add a condition for the case of a folder - then the function should call
# itself for the subfolder as input parameter

#Mein Versuch:

#if __name__ == '__main__':
 #   def folder_recursion(sum_bytes2):
  #      sum_bytes2=0
   #     folder = 'C:/Users/schus/Documents/Bewerbungsunterlagen'
    #    for file in os.listdir(folder):
     #       f2 = os.path.join(folder, file)
      #      if os.path.isfile(f2):
       #     #folders are not treated
        #    #print(file)
         #   #print(os.stat(file))
          #      sum_bytes2 += os.path.getsize(f)
           # #print(os.path.getsize(file))
            #else:
             #   for file in os.path.islink(folder):
              #      sum_bytes2 += os.path.getsize(folder)
            #return file + folder_recursion(sum_bytes2)
  #  print('Sum space: {}'.format(folder_recursion(sum_bytes2)))