import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
#
# # print(response.status_code)
#
# if response.status_code == 200:
#     posts = response.json()
#
#     for post in posts:
#         print(post)
# else:
#     print("Something went wrong")

# data = [
#     {
#         "userId": 1,
#         "name": "Bob"
#     },
#     {
#         "userId": 2,
#         "name": "Alice"
#     }
# ]
#
# response = requests.post(url, json=data)
#
# if response.status_code == 201:
#     print("Successfully created post")
# else:
#     print("Failed to create post")

# print("Hello World")
# print("Hello again")

# import time
#
# def plan_project():
#     time.sleep(2)
#     print("Planned project")
#
# def start_project():
#     time.sleep(4)
#     print("Starting project")
#
# def end_project():
#     time.sleep(3)
#     print("Ending project")
#
# t1 = time.perf_counter()
#
# plan_project()
# start_project()
# end_project()
#
# t2 = time.perf_counter()
#
# print(f"Total time {t2 - t1} seconds taken")


import threading
import time

# def plan_project():
#     time.sleep(2)
#     print("Planned project")
#
# def start_project():
#     time.sleep(4)
#     print("Starting project")
#
# def end_project():
#     time.sleep(3)
#     print("Ending project")
#
# t1 = time.perf_counter()
#
# thread1 = threading.Thread(target=plan_project)
# thread2 = threading.Thread(target=start_project)
# thread3 = threading.Thread(target=end_project)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# t2 = time.perf_counter()
#
# print(f"Total time {t2 - t1} seconds taken")
#
# print("Hello World!")


# def print_tasks(task):
#     print(f"Task: {task} started")
#     time.sleep(1)
#     print(f"Task: {task} completed")
#
# t1 = time.perf_counter()
#
# threads = []
#
# for i in range(1, 11):
#     thread = threading.Thread(target=print_tasks, args=(i, ))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# t2 = time.perf_counter()
#
# print(f"All task completed in {t2 - t1} seconds")


# def print_tasks(task):
#     print(f"Task: {task} started")
#     time.sleep(1)
#     # print(f"Task: {task} completed")
#
# from concurrent.futures import ThreadPoolExecutor
#
# threads = []
#
# t1 = time.perf_counter()
#
# with ThreadPoolExecutor(max_workers=5) as executor:
#     for i in range(1, 11):
#         thread = executor.submit(print_tasks, i)
#         threads.append(thread)
#
# t2 = time.perf_counter()
#
# print(f"All task completed in {t2 - t1} seconds")

import queue

task_queue = queue.Queue()

def worker():
    while True:
        task = task_queue.get()

        if task is None:
            break

        print("Processing", task)
        time.sleep(1)
        task_queue.task_done()

num_threads = 5

threads = []

t1 = time.perf_counter()

for _ in range(num_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)


for i in range(15):
    task_queue.put(i)

for _ in range(num_threads):
    task_queue.put(None)

for thread in threads:
    thread.join()

t2 = time.perf_counter()


print(f"All task completed in {t2 - t1} seconds")









