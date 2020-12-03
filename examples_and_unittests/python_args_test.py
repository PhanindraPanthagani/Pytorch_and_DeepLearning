


print("The value of __name__ is",__name__ )
root_path  = r'C:\Users\Phanindra\OneDrive - The University of Texas at Dallas\POOH'
b = 3
print("root_path is {} and \n b is {} ".format(root_path,b))
csv_file_paths  = ['Pooja','Phani']

def main():
    for indx,name in enumerate(csv_file_paths):
        print("Index is {} and name is {}".format(indx,name))

if __name__ == "__main__":
    main()

