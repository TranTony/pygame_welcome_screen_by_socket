
import sys
import time
import pygame as pg
import socket
from random import choice, randrange

def main():
       # get the hostname
        host = '192.168.161.173'#socket.gethostname()
        print(host)
        port = 2222  # initiate port no above 1024
        server_socket = socket.socket()  # get instance
        
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together
        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        while True:
            try:
                rcvdData = conn.recv(1024).decode()
        
                name = "welcome " + rcvdData + " !"
                # close system if receiving q
                if rcvdData == 'q':
                    pg.quit()
                    sys.exit()
                    conn.close()
                    break
                pg.init()
                pg.mixer.init()

                if len(rcvdData) > 0:
                    info = pg.display.Info()
                    screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
                    screen_rect = screen.get_rect()
                    font = pg.font.Font(None, 200)
                    clock = pg.time.Clock()
                    color = (randrange(256), randrange(256), randrange(256))
                    done = False
                    start = time.time()
                    
                    pg.mixer.music.load("sample.mp3")
                    pg.mixer.music.play()
                    try:
                        while not done:
                            # Getting audio from dataset play the dataset
                            if time.time() - start > 2:
                                pg.display.quit()
                                pg.mixer.music.stop()
                                done = True                                
                            

                            txt = font.render(name, True, color)
                                           
                            color = (randrange(256), randrange(256), randrange(256))
                            txt = font.render(name, True, color)
                            
                            screen.fill((255, 255, 255))
                            
                            screen.blit(txt, txt.get_rect(center=screen_rect.center))
                        
                            pg.display.flip()
                            pg.display.update()
                            
    
                                         
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
        conn.close()
        
if __name__ == '__main__':
    main()
