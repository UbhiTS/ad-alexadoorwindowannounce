import appdaemon.plugins.hass.hassapi as hass
import datetime

#
# Alexa Door Window Announce App
#
# Args:
#alexa_door_window_announce:
#  module: alexa_door_window_announce
#  class: AlexaDoorWindowAnnounce
#  alexas:
#    - media_player.kitchen_alexa
#    - media_player.living_room_alexa
#  doors_windows:
#    - cover.garage_door_big
#    - cover.garage_door_small
#    - binary_sensor.main_door
#  announcements:
#    start_time: "00:00:00"
#    end_time: "23:59:59"

class AlexaDoorWindowAnnounce(hass.Hass):

  def initialize(self):

    if "doors_windows" in self.args:
      for door_window_sensor in self.args["doors_windows"]:
        self.listen_state(self.door_window_state_changed, door_window_sensor, attribute = "state")

    self.time_start = datetime.datetime.strptime("00:00:00", '%H:%M:%S').time()
    self.time_end = datetime.datetime.strptime("23:59:59", '%H:%M:%S').time()

    if "announcements" in self.args:
      self.time_start = datetime.datetime.strptime(self.args["announcements"]["start_time"], '%H:%M:%S').time() if "start_time" in self.args["announcements"] else self.time_start
      self.time_end = datetime.datetime.strptime(self.args["announcements"]["end_time"], '%H:%M:%S').time() if "end_time" in self.args["announcements"] else self.time_end

    self.log(f"INITIALIZED : From {self.time_start}, To {self.time_end}")

  def door_window_state_changed(self, entity, attribute, old, new, kwargs):
    
    # if the HA has just rebooted, old state would be unavailable. In that case, do not announce!
    if old == "unavailable":
      return
    
    sensor_name = entity
    friendly_name = self.get_state(entity, attribute = "friendly_name")
    state = "changed"
    if new in ["open", "on"]: state = "opened"
    if new in ["closed", "off"]: state = "closed"
    
    if datetime.datetime.now().time() < self.time_start or self.time_end < datetime.datetime.now().time():
      self.log(f"DOOR/WINDOW TIME LOG ONLY: {sensor_name.split('.')[1]}|{state}")
      return
    
    seconds = 0
    if "alexas" in self.args:
      for alexa in self.args["alexas"]:
        self.run_in(self.announce_state, seconds, sensor_name = sensor_name, friendly_name = friendly_name, state = state, alexa = alexa)
        seconds = seconds + 5


  def announce_state(self, kwargs):
    
    sensor_name = kwargs["sensor_name"]
    friendly_name = kwargs["friendly_name"]
    state = kwargs["state"]
    alexa = kwargs["alexa"]
    
    self.call_service("notify/alexa_media", data = {"type":"tts", "method":"all"}, target = alexa, message = f"Your attention please. The {friendly_name} has been {state}.")
    self.log(f"DOOR/WINDOW ANNOUNCE: {sensor_name.split('.')[1]}|{state}|{alexa.split('.')[1]}")
