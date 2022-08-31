class Calculation():
    def __init__(self):
        self.n1 = ''
        self.n2 = ''
        self.result = ''

    def Cal(self):
        print ('-' * 60)
        print (f'                Calculo')
        print ('-' * 60)
        while True:
            open = input("""Choois the option
            \r 1.  Multiplication
            \r 2.  Division
            \r 3.  subtraction
            \r 4.  Addition
            \r 5.  Exit
            \r Enter: """).upper()

            if open == '1':
                n1 = input("Type number 1: ")
                n2 = input("Type number 2: ")
                result = int(float(n1)) * int(float(n2))
                print(f"result {result}")
            
            elif open == '2':
                n1 = input("Type number 1: ")
                n2 = input("Type number 2: ")
                result = int(float(n1)) / int(float(n2))
                print(f"result {result}")
            
            elif open == '3':
                n1 = input("Type number 1: ")
                n2 = input("Type number 2: ")
                result = int(float(n1)) - int(float(n2))
                print(f"result {result}")
            
            elif open == '4':
                n1 = input("Type number 1: ")
                n2 = input("Type number 2: ")
                result = int(float(n1)) + int(float(n2))
                print(f"result {result}")

            elif open == '5':
                exit()

calculo = Calculation()
calculo.Cal()            
                

