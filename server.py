import pickle
import socket
import struct
import cv2
import time
import pandas as pd
import statistics
from _thread import *

IP = '10.0.0.109'
PORT = 33333
BUFFER_SIZE = 4096
FRAME_LIM = 800 # Stop receiving after receving this number of frames

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

server_socket.bind((IP, PORT))
print('Socket bind completed')

server_socket.listen(10)
print(f'Socket now listening on {IP}:{PORT}')

def process_data(conn, ip_addr):
    OUTPUT_CSV = 'host-' + ip_addr + '_server-' + IP + '.csv'
    timestamp_list = []
    data = b''; payload_size = struct.calcsize('Q')
    frame_count = 0; total_time = 0
    
    while True:   
        # Retrieve message size
        while len(data) < payload_size:
            data += conn.recv(BUFFER_SIZE)
        if not data: break
            
        curr = time.time()  # Current time
        if frame_count == 0:
            timestamp_list.append([curr, curr-epoch, curr-epoch])
        else:
            timestamp_list.append([curr, (curr-timestamp_list[frame_count-1][0])*1000, curr-epoch]) 
        total_time += timestamp_list[frame_count][1]
        frame_count += 1
        print('Received', frame_count, 'frames from', ip_addr, '-', 'Avg. frame transfer time:', round(total_time/frame_count, 4), 'ms.', end = '\r')

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack('L', packed_msg_size)[0]

        # Retrieve all data based on message size
        while len(data) < msg_size:
            data += conn.recv(BUFFER_SIZE)
        data = data[msg_size:]

        if frame_count == FRAME_LIM: break

    # print()
    # print('Average tranfer time of each frame:', round(total_time/frame_count, 4))
    # df = pd.DataFrame(timestamp_list)
    # df.to_csv(OUTPUT_CSV, mode = 'a', header = False, index = False)


epoch = 0; thread_count = 0
while True:
    conn, addr = server_socket.accept()
    print()
    print(f'{addr} is connected.')
    if thread_count == 0:
        epoch = time.time()
    start_new_thread(process_data, (conn, addr[0], ))   # For multiple connections
    thread_count += 1
server_socket.close()
    
