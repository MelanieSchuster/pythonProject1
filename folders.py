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

# 1. include summing space occupied for folders with their content
# Hint: use recersion
