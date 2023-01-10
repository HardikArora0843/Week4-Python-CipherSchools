file = open("random.txt","w")
file.write("blah blah blah")
file.close()


file = open("random.txt","w")
file.close()


file=open("sample.txt","r")
file.close()
print(file.read())



class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self,*arge):
        print("Exitded")
        print(arge)
        
        




        





