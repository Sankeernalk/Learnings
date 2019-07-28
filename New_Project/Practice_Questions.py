def print_directory_contents(spath):
    import os
    for schild in os.listdir(spath):
        schildpath = os.path.join(spath,schild)
        if os.path.isdir(schildpath):
            if os.listdir(schildpath) == []:
                print(schildpath)
            else:
                print_directory_contents(schildpath)
        else:
            print(schildpath)


print_directory_contents('C:\\Users\\611419222\\Documents')