import cv2
import SeguimientoManos as sm

# Declaramos nuestro detector
detector = sm.detectormanos(Confdeteccion=0.75)

# Realizamos la videoCaptura
cap = cv2.VideoCapture(0)

# Entramos a nuestro While True
while True:
    #Realizamos lectura de la VideoCaptura
    ret, frame = cap.read()

    #Detectamos los dedos arriba
    frame = detector.encontrarmanos(frame)

    # Hacemos un rectangulo
    cv2.rectangle(frame, (430, 255), (700, 480), (0, 0, 0), cv2.FILLED)

    #Ponemos la palabra dedos
    cv2.putText(frame, "Numero", (440, 290), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 5)

    #Extraemos la informacion de las manos
    manosInfo, cuadro = detector.encontrarposicion(frame, dibujar=False)
    #print (manos Info)

    # Creamos el filtro de seguridad para evitar errores
    if len(manosInfo) != 0:
        dedos = detector.dedosarriba()
        print(dedos)
        contar = dedos.count(1)
        if contar == 0:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
        elif contar == 1:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
        elif contar == 2:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
        elif contar == 3:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
        elif contar == 4:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
        elif contar == 5:
            cv2.putText(frame, str(contar), (485, 430), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)


    # Mostramos los fotogramas
    cv2.imshow("Contando dedos", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()