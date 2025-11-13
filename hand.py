<<<<<<< HEAD
import cv2
import mediapipe as mp

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    finger_count = 0
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            if all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20]) and landmarks[4].y > landmarks[3].y:
                finger_count = 10
            elif landmarks[4].y > landmarks[3].y and sum(landmarks[tip].y < landmarks[tip - 2].y for tip in [8, 12, 16, 20]) == 1:
                finger_count = 9
            elif landmarks[4].y < landmarks[3].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20]):
                finger_count = 6
            elif landmarks[4].x < landmarks[3].x and landmarks[8].y < landmarks[6].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [12, 16, 20]):
                finger_count = 7
            elif landmarks[4].x < landmarks[3].x and landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [16, 20]):
                finger_count = 8
            else:
                tip_ids = [8, 12, 16, 20]
                finger_count = sum(landmarks[tip].y < landmarks[tip - 2].y for tip in tip_ids)
                if landmarks[4].x < landmarks[3].x:
                    finger_count += 1

    parity = "Even" if finger_count % 2 == 0 else "Odd"
    cv2.putText(frame, f"Count: {finger_count} ({parity})", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Hand Gesture Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
=======
import cv2
import mediapipe as mp

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    finger_count = 0
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            if all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20]) and landmarks[4].y > landmarks[3].y:
                finger_count = 10
            elif landmarks[4].y > landmarks[3].y and sum(landmarks[tip].y < landmarks[tip - 2].y for tip in [8, 12, 16, 20]) == 1:
                finger_count = 9
            elif landmarks[4].y < landmarks[3].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20]):
                finger_count = 6
            elif landmarks[4].x < landmarks[3].x and landmarks[8].y < landmarks[6].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [12, 16, 20]):
                finger_count = 7
            elif landmarks[4].x < landmarks[3].x and landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y and all(landmarks[tip].y > landmarks[tip - 2].y for tip in [16, 20]):
                finger_count = 8
            else:
                tip_ids = [8, 12, 16, 20]
                finger_count = sum(landmarks[tip].y < landmarks[tip - 2].y for tip in tip_ids)
                if landmarks[4].x < landmarks[3].x:
                    finger_count += 1

    parity = "Even" if finger_count % 2 == 0 else "Odd"
    cv2.putText(frame, f"Count: {finger_count} ({parity})", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Hand Gesture Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
>>>>>>> 75b040d0bfbe178827fb3a826fe27a573aa841c5
