import cv2

# Callback function for mouse, prints the coordinates of the clicked point
def print_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('Coordinates: ', x, y)

# Load the frame
frame = cv2.imread('webpage/static/frame.png')

# Show the frame in a window
cv2.namedWindow('image')

# Attach the callback function to the window
cv2.setMouseCallback('image', print_coordinates)

while(True):
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()