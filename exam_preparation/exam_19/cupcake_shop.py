def stock_availability(cupcake_flavours, param, *args):
    if param == "delivery":
        cupcake_flavours.extend(args)
        return cupcake_flavours
    if param == "sell":
        if args:
            if type(args[0]) == int:
                n = int(args[0])
                for _ in range(n):
                    cupcake_flavours = cupcake_flavours[n:]
                    return cupcake_flavours
            else:
                for arg in args:
                    if arg in cupcake_flavours:
                        while arg in cupcake_flavours:
                            cupcake_flavours.remove(arg)
                return cupcake_flavours
        else:
            return cupcake_flavours[1:]

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
