import threading
from time import sleep, ctime
from random import randint

# global task list
tasks = [3, 7, 9, 2, 3, 56, 78, 74]

#tasks = [randint(1, 1000000) for i in range(100000)]

# global result list
results = []

# MAX Threading
THREAD_MAX = 3

# Create task
def loop_create():
    while 1:
        # GLOBAL TASK generate
        tmp = randint(10, 1000)
        # add task to GLOBAL TASK list
        tasks.append(tmp)

        print tasks
        #print results
        print '--------'
        print len(tasks)
        print '--------'
        sleep(1)

# Solve task
def loop_solver():
    while 1:
        if tasks:
            # get the task info
            tmp = tasks.pop(0)

            # solve this problem
            res_tmp = solution(tmp)

            #print res_tmp
            # add the result to Result List
            results.append(res_tmp)

            sleep(1)


def solution(res):
    if res:
        return res, res % 2


def solution_engine():

    tasks_threads = []
    soltion_threads = []

    # Start Task Creater
    tasks_thread = threading.Thread(target = loop_create,
                             args = ())
    tasks_threads.append(tasks_thread)


    for i in range(THREAD_MAX):

        # Start Task solver
        t = threading.Thread(target = loop_solver,
                              args = ())
        soltion_threads.append(t)

    # start a task generate
    for task_thread in tasks_threads:
        task_thread.start()
    # start a series of solution threads
    for solution_thread in soltion_threads:
        solution_thread.start()


    # wait for all threads to finish
    for task_thread in tasks_threads:
        task_thread.join()
    for solution_thread in soltion_threads:
        solution_thread.join()

    print "\nAll threads Done at ", ctime()

if __name__ == '__main__':
    solution_engine()
