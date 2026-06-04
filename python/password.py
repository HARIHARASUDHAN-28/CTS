def user(user_id,passw):
    if user_id=="admin":
        
        if(passw=="pass123"):
            return "login successfully"
        
        else:
            return "invalid password"  
        
    else:
        return "invalid admin"      
    
    
user_id=input("Enter user ID:")
passw=input("Enter a password:")
print(user(user_id,passw))
