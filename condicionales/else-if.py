#ingreso_mensual=(int(input("ingresa tu ingreso mensual: ")))

ingreso_mensual = 5000
gasto_mesual = 80000

#if aninados y eelse if (elif)
if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mesual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mesual > 3000 :
        print("estas bien")
    else: 
     print("estas gastando mucho, hay que ver si te alcanza")

elif ingreso_mensual > 10000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas mas o menos")
else:
    print("eres pobre")