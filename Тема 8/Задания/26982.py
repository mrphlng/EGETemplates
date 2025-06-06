from itertools import permutations
a = 0
b = 0
c = 0
for x in permutations('0123456789', 6):
    z = ''.join(x)
    if z[0] != 0 and z % 5 == 0 and '02' in z == 0 and '04' in z == 0 and '06' in z == 0 and '08' in z == 0 and '20' in z == 0 and '22' in z == 0 and '00' in z == 0 and '24' in z == 0 and '26' in z == 0 and '28' in z == 0 and '40' in z == 0 and '42' in z == 0 and '44' in z == 0 and '46' in z == 0 and '48' in z == 0 and '60' in z == 0 and '62' in z == 0 and '64' in z == 0 and '66' in z == 0 and '68' in z == 0 and '80' in z == 0 and '82' in z == 0 and '11' in z == 0 and '13' in z == 0 and '15' in z == 0 and '17' in z == 0 and '19' in z == 0 and '31' in z == 0 and '33' in z == 0 and '35' in z == 0 and '37' in z == 0 and '39' in z == 0 and '51' in z == 0 and '53' in z == 0 and '55' in z == 0 and '57' in z == 0 and '59' in z == 0 and '71' in z == 0 and '73' in z == 0 and '75' in z == 0 and '77' in z == 0 and '79' in z == 0 and '91' in z == 0 and '93' in z == 0 and '95' in z == 0 and '97' in z == 0 and '99' in z == 0:
        c += 1
print(c)