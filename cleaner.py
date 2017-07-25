import os
import unicodedata

def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for file in files:
            #print (file[-3:])
            if file[-3:] == "txt":
                print (file)
                yield os.path.join(root, file)
   
if __name__ == '__main__':
    path = '/home/triya/Desktop/cnn/cnn_politics/'
    l = list(recursive_file_gen(path)) #directory with txt files
    print (l)
    for filename in l:
        with open (filename) as f:
            lines = f.readlines()
        
        new_l = []
        for line in lines:
            l = line.split()
            if l[0][0] != '<':
                new_l.append(line)
        
        o_path = "/home/triya/Desktop/cnn/cnn_cleaned/"
        ofile_name = o_path + filename[len(path):-4] + "_clean.txt"
        o = open ( ofile_name, "w+")
        for line in new_l:
						temp_line = line.decode('utf-8')
						out_line = unicodedata.normalize('NFKD', temp_line).encode('ascii','ignore')
						o.write(out_line)
