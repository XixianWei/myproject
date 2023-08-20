# QUESTION 1: Jumping The Queue

from collections import deque

# Part A solution
def process_queue(input_filename):
    queue = deque()

    with open(input_filename, 'r') as file:
        for line in file:
            operation, name = line.strip().split()

            if operation == 'JOIN':
                queue.append(name)
            elif operation == 'JUMP':
                queue.appendleft(name)

    return list(queue)

input_file = 'hw3_q1.txt'
final_order = process_queue(input_file)
print("Final order of the queue:", final_order)

# Time Complexity: O(N)
#   N is the number of operations in the input file. Each operation (JOIN or JUMP) takes constant time.
#   The loop iterates through each line in the input file once.

# Space Complexity: O(N)
#   The space complexity is determined by the maximum size of the queue.
#   In the worst case, all operations are "JOIN" operations and each person is added to the queue.
#   Thus, the queue can potentially hold up to N elements.
#   Additionally, the list created at the end also contributes to the space complexity.
#   Therefore, the space complexity is O(N).




# QUESTION 2: Number In Sequence

def num_in_seq_recursive(n):
    if n == 1:
        return 8
    else:
        return num_in_seq_recursive(n - 1) + 7

# Test cases
print(num_in_seq_recursive(1))  # Output: 8
print(num_in_seq_recursive(5))  # Output: 36
print(num_in_seq_recursive(10))  # Output: 71


# QUESTION 3: Hyperlink History

class CFGWebsiteSimulator:
    def __init__(self):
        self.base_url = "https://codefirstgirls.com/"
        self.category_urls = ["/courses", "/opportunities"]
        self.subcategory_urls = ["/courses/cfgdegree", "/opportunities/ambassadors"]
        self.current_url = self.base_url
        self.history = []

    def display_options(self, options):
        print("Options:", ", ".join(options))

    def simulate(self):
        while True:
            print("You are currently on the URL", self.current_url)
            print("Where are you clicking?")
            
            if self.current_url == self.base_url:
                self.display_options(["Courses", "Opportunities"])
            elif self.current_url in self.category_urls:
                self.display_options(["CFGDegree", "Back"])
            elif self.current_url in self.subcategory_urls:
                self.display_options(["Back"])
            
            choice = input()
            
            if choice == "Courses" and self.current_url == self.base_url:
                self.current_url = self.category_urls[0]
                self.history.append(self.current_url)
            elif choice == "Opportunities" and self.current_url == self.base_url:
                self.current_url = self.category_urls[1]
                self.history.append(self.current_url)
            elif choice == "CFGDegree" and self.current_url in self.category_urls:
                self.current_url = self.subcategory_urls[0]
                self.history.append(self.current_url)
            elif choice == "Back":
                if len(self.history) > 1:
                    self.history.pop()
                    self.current_url = self.history[-1]
                else:
                    self.current_url = self.base_url
            else:
                print("Invalid choice. Please choose a valid option.")
                continue


if __name__ == "__main__":
    simulator = CFGWebsiteSimulator()
    simulator.simulate()


# Assumptions made:
# The simulation uses a simple list for maintaining the history of URLs visited.
# User choices are taken as inputs through the input() function.


# Time Complexity:
# Displaying options and making navigation decisions are constant time operations.
# The loop runs indefinitely (while True),but the actions taken within each iteration are constant time.

# Space Complexity:
# The space complexity is determined by the history of visited URLs stored in the self.history list.
# The maximum size of this list depends on the number of times a user goes "Back" or navigates to different pages. It will be proportional to the length of the user's browsing session.