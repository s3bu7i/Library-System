

import sqlite3

#database dosyasını yaratmaq üçün isdifadə olunur :)
#marker.execute("""create table Books(
 #                   Book_name VARCHAR(75),
  #                  Book_writer VARCHAR(75),
   #                 Book_ID INTEGER NOT NULL)
    #                
     #               """ ) 

#dosya yaradıldıqdan sonra database ə məlumatları aşağıdakı kodlar ötürür :)

def addbook():
    
    while True:
        
        bookname = input("Enter the name of the book :")
        bookwriter = input("Enter the writer of the book :")
        bookid = input("Enter the ID of the book :")
        
        connect = sqlite3.connect("mylibrary.db")
        marker=connect.cursor()
        marker.execute("""INSERT INTO Books
                    (Book_name,Book_writer,Book_ID)
                    VALUES
                    ('{}','{}','{}')
                    
                    
                    """.format(bookname,bookwriter,bookid))
        connect.commit()
        connect.close()
        
        print("Registration is complete :) ")
        opt =input("If you want to close the program 'C' press the key :")
        
        if opt == "C":
            break
    
def searchbook():
    
    while True:
        
        print("You Can Serach For Books :) ")  
        
        connect = sqlite3.connect("mylibrary.db")
        marker=connect.cursor()
        
        booksearch = input("Enter the name of the book :")
        bookwritersearch = input("Enter the writer of the book :")
        bookidsearch = input("Enter the ID of the book :")
        
        if booksearch:
            bring = marker.execute("SELECT *from Books WHERE Book_name = '{}' ".format(booksearch))
            
        elif bookwritersearch:
            bring = marker.execute("SELECT *from Books WHERE Book_writer = '{}' ".format(bookwritersearch))
            
        elif bookidsearch:
            bring = marker.execute("SELECT *from Books WHERE Book_ID = '{}' ".format(bookidsearch))
        
        fetch = bring.fetchall()
        total=len(fetch)
        #if len(fetch) == 1:
            
        #   fetch = fetch[0]
        #  print("""{} book's
        #         Writer : {}
            #        ID : {} 
            #       """.format(fetch[0],fetch[1],fetch[2]))
            
        #elif len(fetch) > 1:
        #   print("{} result was found".format(len(fetch)))
            
        for i in range(0,len(fetch)):
            
            print(total,"result was found :)")
            #print("Book : {}; Writer : {}; ID : {}".format(fetch[i][0],fetch[i][1],fetch[i][2]))
            print("""{} book's :
                Writer : {}
                ID : {}""".format(fetch[i][0],fetch[i][1],fetch[i][2]))
        
    
while True:
    
    print(" Welcome To The Library Program ")
    print("Book add : 1 | Book search : 2 ")
    
    choose = int(input("Enter The Transaction You Want To Select :) "))
    if choose == 1:
        addbook()
    elif choose == 2:
        searchbook()
    


    