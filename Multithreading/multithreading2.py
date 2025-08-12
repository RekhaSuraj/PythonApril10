import threading
import time

def task(name):
	print(f'Thread {name} is started')
	time.sleep(2)
	print(f'Thread {name} is finished')


print(f'Main thread is starting {threading.current_thread().name}')

t1 = threading.Thread(target=task,args=('A',))
t1.start()

print('\nMain thread continues to run')

t1.join()

print('Main thread finished')

# Main thread is starting MainThread
# Thread A is started

# Main thread continues to run
# Thread A is finished
# Main thread finished