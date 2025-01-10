import time

def calculate_fps(start_time, fps):
    if time.time() - start_time > 1:
        print(f"FPS: {fps}")
        fps = 0
        start_time = time.time()
    return start_time, fps
