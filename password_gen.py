import string as s, random as r

def password_generator(password_len = 8):
    sample = s.ascii_letters + s.digits + s.punctuation
    return r.sample(sample, password_len)

print(''.join(password_generator(int(input('How many characters for the password? ')))))