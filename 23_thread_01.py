# from threading import Thread
#
#
# def task(count: int):
#     for n in range(count):
#         print(n)
#
# thread1 = Thread(target=task, args=(10,))
# thread2 = Thread(target=task, args=(20,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print('Done')

# # Version Python 3.9
# import time
# from threading import Thread
#
# class MyThread(Thread):
#     def __init__(self, name: str, count: int):
#         Thread.__init__(self)
#         self.setName(name)
#         self.count = count
#     def run(self):
#         for i in range(self.count):
#             print(f'Thread {self.getName()} - {i}')
#             time.sleep(.02)
#
# t_1 = MyThread('Thread-1', 10)
# t_2 = MyThread('Thread-2', 20)
# t_1.start()
# t_2.start()

# Version Python 3.13
import re, time
from queue import Queue
from threading import Thread

# class MyThread(Thread):
#     def __init__(self, count: int):
#         Thread.__init__(self)
#         self.daemon = True
#         self.count = count
#     def run(self):
#         for i in range(self.count):
#             print(f'{self.name} - {i}')
#             time.sleep(.02)

# t_1 = MyThread(10)
# t_2 = MyThread(20)
# t_1.start()
# t_2.start()
# t_1.join()

# In case of counting the total msg number gotten by consumers, here a global list is put forward as below:
msg_lst = list()

class MsgProducer(Thread):
    def __init__(self, count: int, queue: Queue):
        Thread.__init__(self)
        self.count = count
        self.queue = queue
    def run(self):
        for i in range(self.count):
            msg = f'{self.name} - {i}'
            self.queue.put(msg, block=True)

class MsgConsumer(Thread):
    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue
        self.daemon = True
    def run(self):
        while True:
            msg = self.queue.get(block=True)
            print(f'{self.name} - {msg}\n', end='')
            # Dealing the msgs and saving in the msg_lst
            msg_lst.append(f'{self.name} - {msg}')

queue = Queue(3)
threads = list()
threads.append(MsgProducer(10, queue))
threads.append(MsgProducer(10, queue))
threads.append(MsgProducer(10, queue))
threads.append(MsgConsumer(queue))
threads.append(MsgConsumer(queue))
# Find consumers and save in a list
con_lst = list()                # Initializing a list to save consumers
for t in threads:
    if isinstance(t, MsgConsumer):
        if t.name not in con_lst:
            con_lst.append(t.name)
print(con_lst)

for t in threads:
    t.start()

# Thread-4 - Thread-1 - 0   msg format
# Statistics, Producers' msg number and Consumer
for t in threads:
    # if type(t) == MsgProducer:
    if isinstance(t, MsgProducer):
        t.join()

print(len(msg_lst))
# print(msg_lst)

# Counting msg number handled by consumers irrespectively
con_msg_dct = dict()
for msg in msg_lst:
    for con in con_lst:
        if re.match(con, msg):
            con_msg_dct[con] = con_msg_dct.setdefault(con, 0) + 1

print(con_msg_dct)


