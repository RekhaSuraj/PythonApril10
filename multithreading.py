import threading

def task(name):
	print(f'Thread {name} is running')



t1 = threading.Thread(target=task, args=("A",))
t1.start()
t1.join()