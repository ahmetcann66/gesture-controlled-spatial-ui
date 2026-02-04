import cv2
from HandTrackingModule import HandDetector
from ObjectManager import ObjectManager

WIDTH, HEIGHT = 1280, 720
HOLD_THRESHOLD = 40

cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

detector = HandDetector(detectionCon=0.8, maxHands=1)
manager = ObjectManager()

hold_counter = 0
create_cooldown = 0 

while True:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    
    cv2.rectangle(img, (10, 10), (85, 85), (0, 0, 0), cv2.FILLED) 
    cv2.circle(img, (47, 47), 25, (255, 0, 255), cv2.FILLED) 
    cv2.putText(img, "1", (35, 55), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.rectangle(img, (10, 100), (85, 175), (0, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (25, 115), (70, 160), (255, 0, 255), cv2.FILLED) 
    cv2.putText(img, "2", (35, 145), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        fingers = detector.fingersUp()
        length, img, cursor_info = detector.findDistance(4, 8, img)
        cx, cy = cursor_info

        if fingers[1] == 1 and fingers[2] == 0:
            if 10 < cx < 85 and 10 < cy < 85:
                manager.set_shape("circle")
                cv2.rectangle(img, (10, 10), (85, 85), (0, 255, 0), 3) 
            
            elif 10 < cx < 85 and 100 < cy < 175:
                manager.set_shape("rectangle")
                cv2.rectangle(img, (10, 100), (85, 175), (0, 255, 0), 3)
            
            else:
                cv2.circle(img, (lmList[8][1], lmList[8][2]), 10, (0, 255, 255), cv2.FILLED)

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0: 
            if create_cooldown == 0:
                if cx > 100: 
                    manager.add_object(lmList[8][1], lmList[8][2])
                    create_cooldown = 15 
                    cv2.putText(img, "OLUSTURULDU!", (cx, cy - 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        is_pinching = length < 40
        
        if is_pinching and (cx > 100): 
            manager.update_drag(cx, cy, True)
        elif is_pinching and (cx < 100):
            pass
        else:
            manager.update_drag(cx, cy, False)

        if fingers == [0, 0, 0, 0, 0]:
            hold_counter += 1
            bar_x, bar_y = 400, 50
            bar_w, bar_h = 400, 30
            fill_width = int((hold_counter / HOLD_THRESHOLD) * bar_w)
            cv2.rectangle(img, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (50, 50, 50), 3)
            cv2.rectangle(img, (bar_x, bar_y), (bar_x + fill_width, bar_y + bar_h), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, "SILINIYOR...", (bar_x, bar_y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            if hold_counter >= HOLD_THRESHOLD:
                manager.remove_last_object()
                hold_counter = 0
        else:
            hold_counter = 0

    if create_cooldown > 0:
        create_cooldown -= 1

    manager.draw(img)

    cv2.putText(img, f"Mod: {manager.current_shape}", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Tony Stark UI - Pro", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()