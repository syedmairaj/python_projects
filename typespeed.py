import time

def typing_speed_test():
    prompt = "The quick brown fox jumps over the lazy dog"
    print("Type this sentence as fast as you can:\n", prompt)
    input("Press Enter when you're ready...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    speed_wpm = words_typed / (time_taken / 60)
    print("Your typing speed was {:.2f} words per minute.".format(speed_wpm))

    accuracy = calculate_accuracy(prompt, user_input)
    print("Your typing accuracy was {:.2f}%.".format(accuracy))

def calculate_accuracy(prompt, user_input):
    prompt_words = prompt.split()
    user_words = user_input.split()
    correct_words = [uw for pw, uw in zip(prompt_words, user_words) if pw == uw]
    accuracy = (len(correct_words) / len(prompt_words)) * 100
    return accuracy

typing_speed_test()
