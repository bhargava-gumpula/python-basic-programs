import threading, time, random, os, subprocess

# Making function for the threads

def annoy(message):
    while True:
        time.sleep(random.randint(1,3))
        print(message)

def shell_command(command):
    while True:
        time.sleep(1)
        os.system(command)

def host_name():
    host_name=subprocess.check_output(['hostname'])
    while True:
        time.sleep(1)
        print host_name

# Making 4 threads

t1 = threading.Thread(target=annoy, args=('BOO !!',))
t2 = threading.Thread(target=annoy, args=('Hi',))
t3 = threading.Thread(target=shell_command, args=('date',))
t4 = threading.Thread(target=host_name)

# Running the treads

t1.start()
t2.start()
t3.start()
t4.start()

x=0
while True:
    print(x)
    x += 1
    time.sleep(1)



