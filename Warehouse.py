'''

The warehouse management and stocktaking  programused by other store managers to :
● Search products by code.
● Determine the product with the lowest quantity and restock it.
● Determine the product with the highest quantity.
● Calculate the value of each item entry, based on the quantity and cost of the
item. The value is calculated by multiplying the cost by the quantity for each
item entered.

'''

# Modules imports

from tabulate import tabulate

# Class

class Shoe(object):
    
    # Shoe class defination will have all the methods in a warehouse  management system
    
    val = []
        
    def read_data(self):
        
        file = None


        
        try:
            
        # risky code goes here
            
           with open("inventory.txt","r") as f:
               for i in enumerate(f):
                   inventory_str = i[1].strip()
                   inventory_list = inventory_str.split(",")
                   print(f"{inventory_list[0]}\t\t{inventory_list[1]}\t\t{inventory_list[2]}\t\t{inventory_list[3]}\t\t{inventory_list[4]}")
       
                   
        except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
               print("The file that you are trying to open does not exist")
           
        finally:
            
            # Closing file
            
            if file is not None:
               file.close()




                   
    def search_data(self):
        
        # Function to search products by code.
        
        file = None
        code = input("Enter product code to search the product : ")
        
        try:

            # risky code goes here
        
            with open("inventory.txt","r") as f:
               for i in enumerate(f):
                   inventory_str = i[1].strip()
                   inventory_list = inventory_str.split(",")
                   if code == inventory_list[1] : 
                      print(f"{inventory_list[0]}\t\t{inventory_list[1]}\t\t{inventory_list[2]}\t\t{inventory_list[3]}\t\t{inventory_list[4]}")
        except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
               print("The file that you are trying to open does not exist")
            
        finally:

            # Closing file
            
            if file is not None:
               file.close()                      
        
    def lowest_quantity(self) :
        
        # Function to determine the product with the lowest quantity and restock it.

        file = None
        Min = 0
        row = []
        try:

        # risky code goes here
            
            num_list = []
            with open('inventory.txt','r')as fh:
                for line in fh.readlines():
                    num_list.append(int((line.split(','))[4]))

            Min = min(num_list)
            rr= []
            with open("inventory.txt","r") as f:
               for i in f.readlines():

                   if f"{Min}" in i:
                      inventory_str = i
                      inventory_list = inventory_str.split(",")
                      if f"{Min}" in inventory_list[4]:
                          print(f"{inventory_list[2]} '{inventory_list[1]}' has got the highest stock quantity of {inventory_list[4]} items and it is up for sale !!")   
               

            
               
        except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
               print("The file that you are trying to open does not exist")
               
        except ValueError as error:

             # Handling Value Error error which occured in a try block
             
               print("Value error !!")
               print(error)
            
        finally:

            # Closing file
            
            if file is not None:
               file.close()

               
    def highest_quantity(self) :
        
          # Function to determine the product with the lowest quantity and put it on sale.

        file = None
        Max = 0
        try:

        # risky code goes here
            
            num_list = []
            with open('inventory.txt','r')as fh:
                for line in fh.readlines():
                    num_list.append(int((line.split(','))[4]))

            Max = max(num_list)
            rr = []
            with open("inventory.txt","r") as f:
               for i in f.readlines():

                   if f"{Max}" in i:
                      inventory_str = i
                      inventory_list = inventory_str.split(",")
                      if f"{Max}" in inventory_list[4]:
                          print(f"{inventory_list[2]} '{inventory_list[1]}' has got the highest stock quantity of {inventory_list[4]} items and it is up for sale !!")   
               
        except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
               print("The file that you are trying to open does not exist")
               
        except ValueError as error:

            # Handling Value Error error which occured in a try block
            
               print("Value error !!")
               print(error)
            
        finally:

            # Closing file
            
            if file is not None:
               file.close()
               
    def value_per_item(self) :

       # Function to calculate the value of each item entry, based on the quantity and cost of the item        
        file = None
        
        try:

        # risky code goes here            
           
           with open("inventory.txt","r") as f: 
               for i in enumerate(f):
                   inventory_str = i[1].strip()
                   inventory_list = inventory_str.split(",")
                   value = int(inventory_list[3]) * int(inventory_list[4])
                   inventory_list.append(value)
                   string = ','.join([str(item) for item in inventory_list])
                   self.val.append(value)
                   
           with open("inventory.txt","r+") as f:
                   string = ','.join([str(item) for item in self.val])             
                   for i in self.val:
                       f.write(i+"\n")
                   
        except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
               print("The file that you are trying to open does not exist")
            
        finally:

            # Closing file
            
            if file is not None:
               file.close()
               

    def read_table(self):
        
    # Function to tepresent the data from the objects list in a table format using Python’s tabulate module, with the new value column added.
        
     file = None
     try:

        # risky code goes here
         
        with open("inventory.txt","r") as f:
          print("Country\t\t,Code\t,Product,Cost,Quantity,Value")  
          for i in enumerate(f):
              inventory_str = i[1].strip()
              inventory_list = inventory_str.split(",\t")
              all_data = [
                        [f"{inventory_list[0]}"]
                       ]
              table1 = tabulate(all_data,headers='firstrow')
              print(table1)
                   
     except FileNotFoundError:

            # Handling FileNotFoundError error which occured in a try block
            
           print("The file that you are trying to open does not exist")
            
     finally:

            # Closing file         
            if file is not None:
               file.close()

               
# Creating at least 5 shoe objects and storing these in a list. 
 
shoe1 = Shoe()
shoe2 = Shoe()
shoe3 = Shoe()
shoe4 = Shoe()
shoe5 = Shoe()

# Adding functionality to search products in the objects list by code.

shoe_list = [shoe1.search_data(),shoe2.search_data(),shoe3.search_data(),shoe4.search_data(),shoe5.search_data()]

# Calling code to determine the product with the lowest and highest quantity,

shoe1.lowest_quantity()
shoe1.highest_quantity()

''' Representing  the data from the objects list in a table format using
    Python’s tabulate module, with the new value column added. '''

shoe1.read_table()


            
        
