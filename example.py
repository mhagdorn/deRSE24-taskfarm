from taskfarm_worker import TaskFarmWorker

# connect to taskfarm
tf = TaskFarmWorker(
    'user', 'secret',
    'da8eb1c10eac4cefb39c8889d6d7170a',
    url_base='http://localhost:5000/api/')
print(tf.percentDone)

# loop over the tasks
for t in tf.tasks:
    print("worker {} processing task {}"
          .format(tf.worker_uuid, t))
    # do some work
    # update the percentage done
    tf.update(50)
    # do some more work and update percentage
    tf.update(100)
    # mark task as completed
    tf.done()
