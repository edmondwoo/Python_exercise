def timer(func):
    def wrap(sleep_time):
        t_start = time.time()
        func(sleep_time)
        t_end = time.time()
        t_count = t_end - t_start
        print(‘[花費時間]’, t_count)

    return wrap

@timer
def dosomething(sleep_time):
    print(‘do some thing’)
    time.sleep(sleep_time)

dosomething(3)