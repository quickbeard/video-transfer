import os
import random
import time

server_list = ['10.0.0.109', '10.0.0.110']
busy_list = [30, 25]  # minutes
idle_list = [15, 10]  # minutes
max_time = 3600     # 1 hour


global_start_time = time.time()
# run for max_time hour(s)
phases = 0
while True:
    busy = random.choice(busy_list); busy = busy*60
    dest_server = random.choice(server_list)
    cmd = 'python3 serialize-send-client.py' + dest_server
    
    print('Busy phase', phases + 1, '- sending to server', dest_server, 'for', busy, 'mins...')
    local_start_time = time.time()
    while True:
        os.system(cmd)
        if (time.time() - local_start_time) > busy:
            break
        # if os.system(cmd) takes a long time, it won't stop until it finishes.
        # Therefore, in client.py, we should pick a frame limit and break when it reaches that limit
    
    idle = random.choice(idle_list)
    print('Idle phase', phases + 1, '- sleeping for', idle, 'mins...')
    time.sleep(idle*60)
        
    phases += 1
    if (time.time() - global_start_time) > max_time: break
        
print('Running time:', round((time.time()-start_time)/60, 3), 'minutes.')

'''
s1 -> h1, h2
s2 -> h2, h3
s3 -> h3, h4
s4 -> h5, h6

mega_script_client.py on host 1
server_list = ['s1']

mega_script_client.py on host 2
server_list = ['s1', 's2']
'''