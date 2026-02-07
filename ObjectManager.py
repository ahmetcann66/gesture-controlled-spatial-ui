import cv2
import math

class ObjectManager:
    def __init__(self):
        self.objects = []
        self.selected_id = -1
        self.base_color = (255, 0, 255)
        self.selected_color = (0, 255, 255)
        self.current_shape = "circle"
        
        self.GRAVITY = 0.6
        self.BOUNCE = 0.7
        self.FLOOR_Y = 650
        self.OBJ_RADIUS = 40

    def add_object(self, x, y):
        self.objects.append({
            'x': x, 
            'y': y,
            'dy': 0,
            'dx': 0,
            'grabbed': False,
            'color': self.base_color, 
            'shape': self.current_shape
        })

    def remove_last_object(self):
        if self.objects:
            self.objects.pop()
            self.selected_id = -1

    def set_shape(self, shape_type):
        self.current_shape = shape_type

    def set_color(self, color):
        self.base_color = color

    def check_collisions(self):
        count = len(self.objects)
        for i in range(count):
            for j in range(i + 1, count):
                obj1 = self.objects[i]
                obj2 = self.objects[j]
                
                dist_x = obj1['x'] - obj2['x']
                dist_y = obj1['y'] - obj2['y']
                distance = math.sqrt(dist_x**2 + dist_y**2)
                
                min_dist = self.OBJ_RADIUS * 2
                
                if distance < min_dist:
                    overlap = min_dist - distance
                    if distance == 0: distance = 1
                    
                    move_x = (dist_x / distance) * (overlap / 2)
                    move_y = (dist_y / distance) * (overlap / 2)
                    
                    if not obj1['grabbed']:
                        obj1['x'] += move_x
                        obj1['y'] += move_y
                    if not obj2['grabbed']:
                        obj2['x'] -= move_x
                        obj2['y'] -= move_y

                    if not obj1['grabbed'] and not obj2['grabbed']:
                        obj1['dy'], obj2['dy'] = obj2['dy'], obj1['dy']
                        jitter = 2 if dist_x > 0 else -2
                        obj1['x'] += jitter

    def update_physics(self):
        self.check_collisions()

        for obj in self.objects:
            if not obj['grabbed']:
                obj['dy'] += self.GRAVITY
                obj['y'] += obj['dy']
                
                obj['x'] += obj['dx']
                obj['dx'] *= 0.95

                if obj['y'] > self.FLOOR_Y:
                    obj['y'] = self.FLOOR_Y
                    obj['dy'] = -obj['dy'] * self.BOUNCE
                    
                    if abs(obj['dy']) < 1:
                        obj['dy'] = 0
                
                if obj['x'] < 40: 
                    obj['x'] = 40
                if obj['x'] > 1240: 
                    obj['x'] = 1240

    def update_drag(self, cx, cy, is_pinching):
        if not is_pinching:
            self.selected_id = -1
            for obj in self.objects:
                obj['grabbed'] = False
            return

        if is_pinching and self.selected_id == -1:
            for i, obj in enumerate(self.objects):
                dist = math.hypot(cx - obj['x'], cy - obj['y'])
                if dist < 50:
                    self.selected_id = i
                    obj['grabbed'] = True
                    obj['dy'] = 0
                    obj['dx'] = 0
                    break
        
        if self.selected_id != -1 and self.selected_id < len(self.objects):
            self.objects[self.selected_id]['x'] = cx
            self.objects[self.selected_id]['y'] = cy
            self.objects[self.selected_id]['dy'] = 0
            self.objects[self.selected_id]['dx'] = 0

    def draw(self, img):
        cv2.line(img, (0, int(self.FLOOR_Y + 35)), (1280, int(self.FLOOR_Y + 35)), (100, 100, 100), 5)

        for i, obj in enumerate(self.objects):
            color = obj['color']
            if i == self.selected_id:
                color = self.selected_color
            
            x, y = int(obj['x']), int(obj['y'])
            
            if obj['shape'] == "circle":
                cv2.circle(img, (x, y), 40, color, cv2.FILLED)
                cv2.circle(img, (x, y), 40, (255, 255, 255), 2)
            
            elif obj['shape'] == "rectangle":
                cv2.rectangle(img, (x - 35, y - 35), (x + 35, y + 35), color, cv2.FILLED)
                cv2.rectangle(img, (x - 35, y - 35), (x + 35, y + 35), (255, 255, 255), 2)