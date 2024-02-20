import time
import matplotlib.pylab as plt


def elapsed_time():
    start_time = time.time()

    try:
        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        end_time = time.time()
        elapsed_seconds = end_time - start_time
        formatted_time = f"{elapsed_seconds:.2f}\n"

        try:

            with open('log.txt', 'a') as file:
                file.write(formatted_time)
                file.flush()

            print(formatted_time)
        except Exception as e:
            print(f"Error writing to file: {e}")


if __name__ == "__main__":
    elapsed_time()



def calculate_sum_of_numbers(file_path):
    global total_sum_minutes
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Extract numbers using a simple split and map approach
            numbers = [float(word) for word in content.split() if word.replace('.', '', 1).isdigit()]


            total_sum = sum(numbers)
            total_sum_minutes = total_sum / 60


            return total_sum, total_sum_minutes


    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



file_path = 'log.txt'
result, total_sum_minutes = calculate_sum_of_numbers(file_path)

if result is not None:
    print(f"Sum of numbers in the file: {result}")










activity_data = {}


activity = 'Pomodoro'
time_spent_hours = total_sum_minutes/60.0


activity_data[activity] = time_spent_hours

y_axis_values = range(20)

# Matplotlib
plt.bar(activity_data.keys(), activity_data.values(), color='Yellow')

#  labels
plt.xlabel('Time')
plt.ylabel('Hours')
plt.title('Time Spent on Pomodoro')

plt.yticks(y_axis_values)


plt.show()














