import cv2
from pyzbar import pyzbar

def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            draw_rectangle_and_text(frame, barcode)

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def draw_rectangle_and_text(frame, barcode):
    x, y, w, h = barcode.rect
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    barcode_value = barcode.data.decode("utf-8")
    cv2.putText(frame, barcode_value, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

if __name__ == "__main__":
    main()
