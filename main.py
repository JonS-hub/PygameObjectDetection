import cv2
import numpy as np
from ultralytics import YOLO
import supervision as sv
import pygame

model = YOLO("yolo11s.pt")
cap = cv2.VideoCapture('person.mp4')

LIGHT_PURPLE_BGR = (255, 0, 191)  
LIGHT_PURPLE_RGB = (191, 0, 255)  
PURPLE_HEX = "#BF00FF"           

 
corner_annotator = sv.BoxCornerAnnotator(
    color=sv.Color.from_hex(PURPLE_HEX), 
    thickness=2, 
    corner_length=15
)

track_history = {} 


pygame.init()
pygame.display.set_caption("Pygame Visualization")
screen_width, screen_height = 1020, 600
pygame_screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 16, bold=True)

def draw_on_pygame(surface, track_id, centers_list):
    if len(centers_list) > 1:
        points = [(int(c[0]), int(c[1])) for c in centers_list]
        pygame.draw.lines(surface, (210, 210, 210), False, points, 2)

    current_pos = (int(centers_list[-1][0]), int(centers_list[-1][1]))
 
    pygame.draw.circle(surface, LIGHT_PURPLE_RGB, current_pos, 6)
  
    text_surface = font.render(f"ID: {track_id}", True, (0, 0, 0))
    surface.blit(text_surface, (current_pos[0] + 10, current_pos[1] - 10))

def draw_on_opencv(frame, track_id, box):
   
    x1, y1, _, _ = box
    cv2.putText(
        frame, 
        f"ID: {track_id}", 
        (int(x1), int(y1) - 10), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.5, 
        LIGHT_PURPLE_BGR, 
        2
    )

count = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    count += 1
    if count % 3 != 0: continue 

    frame = cv2.resize(frame, (screen_width, screen_height))
    results = model.track(frame, persist=True, classes=0, verbose=False)

    pygame_screen.fill((255, 255, 255)) 

    if results[0].boxes is not None and results[0].boxes.id is not None:
        detections = sv.Detections.from_ultralytics(results[0])
        
        opencv_annotated_frame = corner_annotator.annotate(scene=frame.copy(), detections=detections)

        centers = detections.get_anchors_coordinates(anchor=sv.Position.CENTER)
        track_ids = detections.tracker_id
        xyxy_boxes = detections.xyxy 

        for center, t_id, box in zip(centers, track_ids, xyxy_boxes):
            if t_id not in track_history:
                track_history[t_id] = [] 
            
            track_history[t_id].append(center)

            draw_on_pygame(pygame_screen, t_id, track_history[t_id])
            draw_on_opencv(opencv_annotated_frame, t_id, box)
            
    else:
        opencv_annotated_frame = frame.copy()

    cv2.imshow("RGB", opencv_annotated_frame)
    pygame.display.flip()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()