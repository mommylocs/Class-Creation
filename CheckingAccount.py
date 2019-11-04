class CheckingMbr:
    """This is the Checking Member's data"""
    def __init__(self,name, address, acct_no, acct_bal):
        self.name = name
        self.address = address
        self.acct_no = acct_no
        self.acct_bal =acct_bal
        name_split = name.split(" ")
        self.first_name = name_split[0]
        self.last_name = name_split[1]
    #Welcome message when user logs in    
    def welcome_msg(self):
        print ("Hello " + self.first_name)
    def print_details(self):
        print (self.last_name, self.acct_no[8:12], self.acct_bal)
    
user1 = CheckingMbr("Mama Mia","1100 Bowman St, 32219", "000111222333",1567.00 )
#user1.first_name= "Mama"
#user1.last_name= "Mia"
#user1.address = "1100 Bowman St, 32219"
#user1.acct_no = "000111222333"
#user1.acct_bal = 1567.00

#print (user1.last_name, user1.acct_no[8:12], user1.acct_bal)




