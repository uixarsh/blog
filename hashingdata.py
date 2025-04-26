from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# Generates hash in binary format
bcrypt.generate_password_hash('testing')        

# Generates hash in string format.
hashed_pwd = bcrypt.generate_password_hash('testing').decode('utf-8')     

# Compare the hash with original string.  
bcrypt.check_password_hash(hashed_pwd, 'password')      # False
bcrypt.check_password_hash(hashed_pwd, 'testing')       # True