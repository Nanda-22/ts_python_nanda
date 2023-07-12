#single and simple inheritance 
class Branch:
    def getbranchdata(self):
        self.bcode=int(input("Enter branch code:"))
        self.bname=input("Enter branch name:")
        self.baddress=input("Enter branch address:")
    def displaybranchdata(self):
        print("Branch code is:",self.bcode)
        print("Branch name is:",self.bname)
        print("Branch address is:",self.baddress)
obj=Branch()
obj.getbranchdata()
obj.displaybranchdata()
