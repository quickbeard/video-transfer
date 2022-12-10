import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import time
import sys

DEST_IP = sys.argv[1]
DEST_PORT = 33333
FILENAME = 'video1-240p.mp4'
FRAME_LIM = 800

def establish_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'Connecting to {DEST_IP}:{DEST_PORT}')
    client_socket.connect((DEST_IP, DEST_PORT))
    print('Connected.')
    return client_socket

def send_video_frames(client_socket, filename):
    cap = cv2.VideoCapture(filename)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if video finished or no Video Input
        if not ret: break
        # Serialize frame
        data = pickle.dumps(frame)
        # message length
        message_size = struct.pack('Q', len(data))
        # Send all
        client_socket.sendall(message_size + data)
        print('Sent', frame_count, 'frames', end = '\r')
        frame_count += 1
        if frame_count == FRAME_LIM: break
        time.sleep(0.03)

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    client_socket = establish_connection()
    send_video_frames(client_socket, FILENAME)
