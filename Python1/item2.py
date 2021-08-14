print(' *** Wind classification ***')

sWind = float(input('Enter wind speed (km/h) : '))

if sWind >= 209:
    print('Wind classification is Super Typhoon.')
elif sWind >= 102 and sWind < 209:
    print('Wind classification is Typhoon.')
elif sWind >= 56 and sWind < 102:
    print('Wind classification is Tropical Storm.')
elif sWind >= 52 and sWind < 56:
    print('Wind classification is Depression.')
else:
    print('Wind classification is Breeze.')
