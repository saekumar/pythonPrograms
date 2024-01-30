class Agent:
    def __init__(self):
        self.state = "greeting"
    
    def greet(self):
        print("Hello! I'm an intelligent agent that can add two integers. Please provide me with two numbers to add or type 'stop' to exit.")
        self.state = "addition"
    
    def add(self, num1, num2):
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}. Please provide me with two more numbers to add or type 'stop' to exit.")
    
    def run(self):
        while True:
            if self.state == "greeting":
                self.greet()
            elif self.state == "addition":
                user_input = input("Enter two numbers separated by a space: ")
                if user_input.lower() == "stop":
                    break
                try:
                    num1, num2 = map(int, user_input.split())
                    self.add(num1, num2)
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")
    
if __name__ == '__main__':
    agent = Agent()
    agent.run()
