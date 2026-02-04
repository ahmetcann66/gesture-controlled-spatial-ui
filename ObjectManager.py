import cv2
import math

class ObjectManager:
    def __init__(self):
        self.objects = []
        self.selected_id = -1
        self.base_color = (255, 0, 255)
        self.selected_color = (0, 255, 0)
        self.current_shape = "circle" 

    def add_object(self, x, y):
        self.objects.append({
            'x': x, 
            'y': y, 
            'color': self.base_color, 
            'shape': self.current_shape
        })

    def remove_last_object(self):
        if self.objects:
            self.objects.pop()
            self.selected_id = -1

    def set_shape(self, shape_type):
        self.current_shape = shape_type

    def update_drag(self, cx, cy, is_pinching):
        if is_pinching:
            if self.selected_id == -1:
                for i, obj in enumerate(self.objects):
                    dist = math.hypot(cx - obj['x'], cy - obj['y'])
                    if dist < 50:
                        self.selected_id = i
                        break
            
            if self.selected_id != -1 and self.selected_id < len(self.objects):
                self.objects[self.selected_id]['x'] = cx
                self.objects[self.selected_id]['y'] = cy
        else:
            self.selected_id = -1

    def draw(self, img):
        for i, obj in enumerate(self.objects):
            color = obj['color']
            if i == self.selected_id:
                color = self.selected_color
            
            if obj['shape'] == "circle":
                cv2.circle(img, (obj['x'], obj['y']), 40, color, cv2.FILLED)
                cv2.circle(img, (obj['x'], obj['y']), 40, (255, 255, 255), 2)
            
            elif obj['shape'] == "rectangle":
                x, y = obj['x'], obj['y']
                cv2.rectangle(img, (x - 35, y - 35), (x + 35, y + 35), color, cv2.FILLED)
                cv2.rectangle(img, (x - 35, y - 35), (x + 35, y + 35), (255, 255, 255), 2)