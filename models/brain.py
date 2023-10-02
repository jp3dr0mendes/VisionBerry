# import RPi.GPIO

# class Brain:
#     def __init__(self, request):
#         self.fruit_apropriado = 16
#         self.fruit_inadequado = 36
#         self.no_fruit         = 37

#         GPIO.setup(self.fruit_apropriado, GPIO.OUT)
#         GPIO.setup(self.fruit_inadequado, GPIO.OUT)
#         GPIO.setup(self.no_fruit, GPIO.OUT)

#         self.start(request)

#     def start(self, content):
#         if content == None:
#             GPIO.output(self.fruit_apropriado, False)
#             GPIO.output(self.self.fruit_inadequado, False)
#             GPIO.output(self.no_fruit, True)
#             print("No fruit")
#         else: self.response(content)

#     def response(self, request):
#         if request: 
#             GPIO.output(self.fruit_apropriado, True)
#             GPIO.output(self.self.fruit_inadequado, False)
#             GPIO.output(self.no_fruit, False)
#             print("Fruto Apropriado")
#         else: 
#             GPIO.output(self.fruit_inadequado, True)
#             GPIO.output(self.fruit_apropriado, False)
#             GPIO.output(self.no_fruit, False)
#             print("Fruto Inadequado")


class Brain:
    def __init__(self, request):
        # self.fruit_apropriado = 16
        # self.fruit_inadequado = 36
        # self.no_fruit         = 37

        # GPIO.setup(self.fruit_apropriado, GPIO.OUT)
        # GPIO.setup(self.fruit_inadequado, GPIO.OUT)
        # GPIO.setup(self.no_fruit, GPIO.OUT)

        self.start(request)

    def start(self, content):
        if content == None:
            # GPIO.output(self.fruit_apropriado, False)
            # GPIO.output(self.self.fruit_inadequado, False)
            # GPIO.output(self.no_fruit, True)
            print("No fruit")
            return "No Fruits"
        else: self.response(content)

    def response(self, request):
        if request: 
            # GPIO.output(self.fruit_apropriado, True)
            # GPIO.output(self.self.fruit_inadequado, False)
            # GPIO.output(self.no_fruit, False)
            print("Fruto Apropriado")
            return "Fruto Apropriado"
        else: 
            # GPIO.output(self.fruit_inadequado, True)
            # GPIO.output(self.fruit_apropriado, False)
            # GPIO.output(self.no_fruit, False)
            print("Fruto Inadequado")
            return "Frutp Inadequado"