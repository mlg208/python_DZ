import threading

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
num_threads = 4  

def calculate_average(sublist):
    total = sum(sublist)
    count = len(sublist)
    return total / count

def thread_function(sublist, result):
    avg = calculate_average(sublist)
    result.append(avg)

sublists = []
step = len(data) // num_threads
for i in range(0, len(data), step):
    sublist = data[i:i+step]
    sublists.append(sublist)

threads = []
results = []
for sublist in sublists:
    thread = threading.Thread(target=thread_function, args=(sublist, results))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

final_average = sum(results) / len(results)

print(f"Среднее значение: {final_average}")
