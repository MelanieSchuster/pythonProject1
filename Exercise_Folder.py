sum_bytes = 0
python_folder = 'C:/Users/schus/Documents/Bewerbungsunterlagen'
def folder_recursion(sum_bytes):
    for file in os.listdir(python_folder):
        f = os.path.join(python_folder, file)
        if os.path.isfile(f):
        #folders are not treated
        #print(file)
        #print(os.stat(file))
            sum_bytes += os.path.getsize(f)
        #print(os.path.getsize(file))
        else:
            sum_bytes = 1
            for folder in os.path.islink(folder):
                sum_bytes += 1
        return sum_bytes + f+folder
print('Sum space: {}'.format(sum_bytes))