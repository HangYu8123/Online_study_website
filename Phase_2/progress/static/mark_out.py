import cv2

# Open the video
cap = cv2.VideoCapture('webpage/static/spining.avi')

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('webpage/static/marked_spining.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # Define the region to be blurred
        roi = frame[150:187, 285:345]

        # Blur the region of interest
        blur = cv2.GaussianBlur(roi, (51, 51), 0)

        # Substitute the original region with the blurred region
        frame[150:187, 285:345] = blur
        
        # Write the frame into the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
