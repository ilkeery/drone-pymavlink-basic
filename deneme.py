import time

from dronekit import Command, LocationGlobalRelative, VehicleMode, connect
from pymavlink import mavutil, mavwp

iha = connect("127.0.0.1:14550", wait_ready=True)

def takeoff(irtifa):
    while iha.is_armable is not True:
        print("İHA arm edilebilir durumda değil.")
        time.sleep(1)


    print("İHA arm edilebilir.")

    iha.mode = VehicleMode("GUIDED")

    iha.armed = True

    while iha.armed is not True:
        print("İHA arm ediliyor...")
        time.sleep(0.5)

    print("İHA arm edildi.")

    iha.simple_takeoff(irtifa)
    
    while iha.location.global_relative_frame.alt < irtifa * 0.9:
        print("İha hedefe yükseliyor.")
        time.sleep(1)

def gorev_ekle1():
    global komut
    komut = iha.commands

    time.sleep(1)
    #TAKEOFF()
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0, 0, 0, 0, 0, 0, 0, 15))
    
    # WAYPOINT
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36278850,	149.16491480, 15))
    komut.upload()
    print("Komutlar yükleniyor...")

def land():

    time.sleep(1)
    #LANDING
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_DO_CHANGE_ALTITUDE, 0, 0, 0, 3, 0, 0, 0, 0, 0))
    komut.upload()
def gorev_ekle2():

    # TAKEOFF()
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0,0, 0, 0, 0, 0, 0, 0, 15))
    komut.upload()
    #WAYPOINT
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36285520,	149.16527150, 15))
def rtl():
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0)) 
    komut.upload()
takeoff(15)

gorev_ekle1()

iha.mode = VehicleMode("AUTO")
time.sleep(15)
land()
time.sleep(5)
takeoff(10)
gorev_ekle2()
time.sleep(20)
rtl()
#while True:
   # next_waypoint = komut.next
    
    #print(f"Siradaki komut {next_waypoint}")
    #time.sleep(1)

    #if next_waypoint is 4:
     #   print("Görev bitti.")
      #  break



#print("Döngüden çikildi.")