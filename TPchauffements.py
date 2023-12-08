#fonction produce_default_dict
def produce_default_dict():
    return {'root': 'password'}

#fonction salutation
def salutation(nom, age):
    print(f"Bonjour '{nom}', vous avez actuellement {age} ans.")


#fonction power_2
def power_2(limit):
    i = 0
    powers = []
    while i <= limit:
        powers.append(str(2 ** i))
        i += 1
    print(','.join(powers))

#fonction check_ip_format
def check_ip_format(ip):
    parts = ip.split('.')
    
    if len(parts) == 4:
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        else:
            return True
    else:
        return False

#Enfin
produce_default_dict()

salutation('gael', '24')
salutation('bébé', '0')

power_2(10)

print(check_ip_format('10.0.0.0'))
print(check_ip_format('192.12.')) 

