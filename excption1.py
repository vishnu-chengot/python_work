try:
 fh =open('text_file.txt','r')
 fh.write('hello world')
 fh.close()  
except FileNotFoundError:
  print("----------file does not find----------")
except:
  print("----------cant write----------")


