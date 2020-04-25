# Alexa Door/Window Announce : AppDaemon App (HASS) :chicken:

<a href="https://www.buymeacoffee.com/ubhits" target="_blank">
<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"
     alt="Buy Me A Beer" 
     style="height:41px !important; width:174px !important;" />
</a>

Alexa announces your doors/windows opening and closing. Comes in handy for garage doors or side/main exits for houses and shops where you need to stay informed of the doors/windows state when it changes.

Please ⭐ this repo if you like my work and also check out my other repos like
- [Home Assistant 'STEROIDS' Configuration](https://github.com/UbhiTS/ha-config-ataraxis)
- [Alexa Talking Clock](https://github.com/UbhiTS/ad-alexatalkingclock)
- [Alexa Doorbell](https://github.com/UbhiTS/ad-alexadoorbell)

Also, if you want to see a walkthrough of my Home Assistant configuration, I have my video walkthrough on youtube below
- [Home Automation on 'STEROIDS' : Video Walkthrough](https://youtu.be/qqktLE9_45A)

## Installation
**NEEDS THE [Alexa Media Player](https://github.com/custom-components/alexa_media_player) HACS Integration from Keaton Taylor and Alan Tse**

Use [HACS](https://github.com/custom-components/hacs) or [download](https://github.com/UbhiTS/ad-alexatalkingclock) the `alexa_doorbell` directory from inside the `apps` directory to your local `apps` directory, then add the configuration to enable the `alexa_doorbell` module.

## App Configuration (config/appdaemon/apps/apps.yaml)
```yaml
alexa_door_window_announce:
  module: alexa_door_window_announce
  class: AlexaDoorWindowAnnounce
  alexas:
    - media_player.kitchen_alexa
    - media_player.living_room_alexa
  doors_windows:
    - cover.garage_door_big
    - cover.garage_door_small
    - binary_sensor.main_door
  announcements:
    start_time: "00:00:00"
    end_time: "23:59:59"
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | **False** | string | alexa_door_window_announce | The module name of the app.
`class` | **False** | string | AlexaDoorWindowAnnounce | The name of the Class.
`alexas` | **False** | list |  | The Alexa device(s) to target for the door/window announcements.
`door_windows` | **False** | cover\|binary_sensor |  | The doors/windows to monitor.
`announcements\|start_time` | True | time | 00:00:00 | The time to enable the service. (24h format)
`announcements\|end_time` | True | time | 23:59:59 | The time to disable the service. (24h format)

## Thank you!
This app wouldn't be possible without the amazing work done by the developers and community at **[Home Assistant](https://www.home-assistant.io/)**, and of Keaton Taylor and Alan Tse on their **Alexa Media Player integration** for Home Assistant. *https://github.com/custom-components/alexa_media_player*

It's a secured feeling to know the status of your garage or main/side exits. Ever since we've set this up in our home, now we don't think we can do without it. Your home suddenly gets a voice, something like Jarvis ... awesome ! 

If you like my work and feel gracious, you can buy me a beer below ;)

<a href="https://www.buymeacoffee.com/ubhits" target="_blank">
<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"
     alt="Buy Me A Beer" 
     style="height:41px !important; width:174px !important;" />
</a>

# License
[Apache-2.0](LICENSE). By providing a contribution, you agree the contribution is licensed under Apache-2.0. This is required for Home Assistant contributions.
