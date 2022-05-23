# camera and video capture
import cv2 as cv
import numpy as np 
import pprint as pp


##capture = cv2.VideoCapture("..\..\..\Videos\marciano.mkv")
myCameraPort = 2 # Esta es la camara que esta en el computador

capture = cv.VideoCapture(myCameraPort)
TakePicture = True
takeFlip = False

txt = {'x':100, 'y':100 , 'font':cv.FONT_HERSHEY_SIMPLEX, 'font_scale':1, 'color':(255,255,255), 'thickness':2 , "hasUpdate" : False}
# se selecciona un font de texto
font = cv.FONT_HERSHEY_SIMPLEX
def GetextPos():
    return (txt['x'], txt['y'])

while True:
    # si se presiona la tecla t se inicializa captura
    if( cv.waitKey(1) == ord('t') and TakePicture == False):
        TakePicture = True
        print("Iniciando captura")
    # si se presiona la tecla f se inicializa efecto de flip
    if( cv.waitKey(1) == ord('f') and takeFlip == False):
        print("La siguiente Toma se realizara el efecto flip")
        takeFlip = True
    key = cv.waitKey(1)
    flechas = [ord('a'), ord('d'), ord('w'), ord('s')]
    if( key in flechas):
        txt['x'] = txt['x'] + 10 if key == ord('d') else (txt['x'] - 10 if key == ord('a') else txt['x'])
        txt['y'] = txt['y'] - 10 if key == ord('w') else (txt['y'] + 10 if key == ord('s') else txt['y'])
        txt['hasUpdate'] = True
        
    # tomar foto 
    if capture != None:
        if(capture.isOpened() and (TakePicture or txt['hasUpdate']) ):
            
            print("Capturando")
            # se obtiene la captura de la camara
            ret, image = capture.read() if(TakePicture) else (False, image)
            # se añade la captura a una nueva matriz 
            frame = np.zeros(image.shape, np.uint8)
            # se añade la captura a la matriz frame
            frame[0:,0:] = image
            
            # se imprime el texto en la imagen
            cv.putText(frame,'SaidC',GetextPos(),txt['font'],2,txt['color'],txt['thickness'],cv.LINE_AA)
            # en caso de que se presione la tecla f se realiza el efecto flip
            if(takeFlip == True):
                frame = cv.flip(frame, -1)
            # se muestra la imagen
            cv.imshow('frame', frame)
            # se inicializa la variable TakePicture y takeFlip
            TakePicture = False
            takeFlip = False
            txt['hasUpdate'] = False
            print("Captura finalizada")
            #pp.pprint(frame)
    # verifica si se presiono la tecla q o la ventana se ha cerrado
    if ( cv.waitKey(1) == ord('q') or cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1 ):
        print("Se ha cerrado la ventana")
        break
        
capture.release()
cv.destroyAllWindows()
