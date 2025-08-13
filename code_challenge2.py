amount = eval(input("Enter money to deposit ---> "))

print("Here is the breakdown of your deposit.")

thousands = amount // 1000

print(thousands, "\t - \t1000")
amount = amount - thousands * 1000

fhundreds = amount // 500

print(fhundreds, "\t - \t500")
amount = amount - fhundreds * 500

thundreds = amount // 200

print(thundreds, "\t - \t200")
amount = amount - thundreds * 200

hundred = amount // 100

print(hundred, "\t - \t100")
amount = amount - hundred * 100

fifties = amount // 50

print(fifties, "\t - \t50")
amount = amount - fifties * 50

twenties = amount // 20

print(twenties, "\t - \t20")
amount = amount - twenties * 20

tens = amount // 10

print(tens, "\t - \t10")
amount = amount - tens * 10

ones = amount // 1

print(ones, "\t - \t1")
amount = amount - ones * 1