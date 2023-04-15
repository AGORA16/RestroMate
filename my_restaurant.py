class restaurant:
    name='THE GRAND FAMOUS RESTAURANT'
    branch='Chromepet'
    menu_=[]
    def __init__ (self,d_name, price, type):
        self.d_name=d_name
        self.price=price
        self.type=type
        self.ol={}
        restaurant.menu_.append(self)

    @classmethod
    def menu(cls):
        print('***************************** MENU *****************************')
        print()
        print('Dish Name',end='\t')
        print('Price',end='\t')
        print('Type')
        for i in cls.menu_:
            print(i.d_name,end='\t\t')
            print(i.price,end='\t')
            print(i.type)
        print()

    def show_order(self):
        if self.ol!={}:
            print('Dish Name','Price','Type','ordered count',sep='   ')
            for i in self.ol:
                for j in restaurant.menu_:
                    if i==j.d_name:
                        print(j.d_name,j.price,j.type,self.ol[i],sep='\t   ')
        else:
            print("You haven't ordered yet... please make some order..")
                
    def make_order(self):
        print('The available Items are :')
        self.menu()
        c=1
        for i in restaurant.menu_:
            print(f'Enter {c} to select {i.d_name}')
            c+=1
        onum=input('-->')
        if '0'<=onum<='9':
            count=int(input('Enter How many counts do you wants to add :'))
            for i in range(len(restaurant.menu_)+1):
                if i==int(onum):
                    self.ol[restaurant.menu_[i-1].d_name]=count
            print('Item Added Successfully...')
        else:
            print('invalid input')

    def rem_dish(self):
        if self.ol!={}:
            self.show_order()
            ri=input('Enter the item name you want to remove \n-->')
            if ri in self.ol:
                rc=int(input('Enter the count you want to remove :'))
                if rc==self.ol[ri]:
                    self.ol.pop(ri)
                else:
                    self.ol[ri]-=rc
            print('Item Removed successfully....')
        else:
            print("You haven't ordered yet.. please make some order to remove..")


    def payment(self):
        if self.ol!={}:
            print('The oders of You :')
            sum=0
            print('Dish Name','Price','Type','ordered count','amount',sep='  ')
            for i in self.ol:
                for j in restaurant.menu_:
                    if i==j.d_name:
                        print(j.d_name,j.price,j.type,self.ol[i],self.ol[i]*j.price,sep='\t   ')
                        sum+=self.ol[i]*j.price
                
            print("THE TOTAL AMOUNT IS : ",sum)
            p=input('To make payment press p :')
            if p=='p' or p=='P':
                self.ol={}
                print('Payment Successful..')
                print('Thanks... Visit Again')
            else:
                print('Enter a valid input')
        else:
            print("You haven't ordered yet... please make some order..")

        
    def main(self):
        print()
        op=input('Enter 1 to display the Menu \nEnter 2 to display your Orders \nEnter 3 to Add Dish \nEnter 4 to Remove a Dish from your order \nEnter 5 to Make Payment \nEnter 6 to Exit \n-->')
        if op=='1':
            self.menu()
            self.main()
        elif op=='2':
            self.show_order()
            self.main()
        elif op=='3':
            self.make_order()
            self.main()
        elif op=='4':
            self.rem_dish()
            self.main()
        elif op=='5':
            self.payment()
            self.main()
        elif op=='6':
            print('Thanks... Visit Again')
            return
        else:
            print('Invalid Input')
            self.main()

print('****************** WELCOME TO THE GRAND FAMOUS RESTAURANT ******************')
print('******************************* Chromepet *******************************')
r1=restaurant('dosa',25,'veg')
r2=restaurant('idli',15,'veg')
r3=restaurant('fish',120,'non-veg')
r4=restaurant('prawn',100,'non-veg')
r1.main()
