import MySQLdb

       

conn = MySQLdb.connect(host='localhost',user='root',passwd='', db='spider') 

cursor =conn.cursor()  

f = open( "1.jpg","rb")   

b = f.read()

f.close()   
  
cursor.execute( "INSERT INTO test_img (img) VALUES (%s)" , (MySQLdb.Binary(b)))

conn.commit()
    
    #cursor.execute("INSERT INTO test_img SET img2='%s'" % MySQLdb.escape_string(b))
    
    #conn.commit()   

    
conn = MySQLdb.connect(host='localhost',user='root',passwd='', db='spider') 

cursor =conn.cursor() 

cursor.execute( "SELECT img FROM test_img where img_id=5" )   
d = cursor.fetchone()[0]   
cursor.close()   

f = open( "5.jpg" , "wb" ) 

f.write(d)

f.close()   