
def machine():
    keys='abcdefghijklmnopqrstuvwxyz !'
    values=keys[-1] + keys[0:-1]

    encryptdict=dict(zip(keys,values))
    decryptdict=dict(zip(values,keys))

    message=(input('pls enter your message:'))
    mode = input("pls enter the mode : Encode(E) OR decode(D):")

    if mode.upper() == 'E':
        newmessage= ''.join([encryptdict[letter] for letter in message.lower()])
    elif mode.upper()=='D':
        newmessage=''.join([decryptdict[letter] for letter in message.lower()])
    else:
        print('pls enter a correct choice:')

    return newmessage.capitalize()
print(machine())
            
