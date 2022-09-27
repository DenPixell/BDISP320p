class Users():
    id = 0
    name = str
    surname = str
    login = str
    password = str
    group = str
    def Default_Users(self):
        self.id = self.id+1
        self.name="Null"
        self.surname = "Null"
        self.login = "Null"
        self.password = "Null"
        self.group = "Null"
    def New_Users(self,n,s,l,p,g):
        self.id = self.id + 1
        self.name = n
        self.surname = s
        self.login = l
        self.password = p
        self.group = g
    def Change_Users(self,i,n,s,l,p,g):
        if self.id==i:
            self.name = n
            self.surname = s
            self.login = l
            self.password = p
            self.group = g
    def RetUsers(self,n):
        if self.name==n:
            return (f"Id: {self.id}   Name: {self.name}   Surname: {self.surname}   Login: {self.login}   Password {self.password}   Group {self.group} ")
        else:
            return "Null"