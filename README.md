

Based on:
- lilafisch POV (https://badge.team/projects/lilafisch_pov).
- cyberband (https://badge.team/projects/cyberband)

Paint a picture/text defined as png  into the air. 

Included is a converter converting a png (resolution x:11) to a json object, which can be light painted. 

In favor of choosing the animation the flipping options from "cyberband" where removed.   
The top LED is furthermore chosen via the bhi160 sensor. So pixel (0,0) is top. 
Instead you can cycle through animations located in "anims", with LEFT and RIGHT buttons.  

The name of an animation is shown on display, "SELECT" activates shown animation which starts after 3 seconds and loops till a Button is pressed.  

Hold card10 in a way that the LEDS point in moving direction and move it from your right to your left. 
The opposit viewer/cam should see it moving from left to right. 

Update: The direction is now determined via the bhi160 sensor at the start of an animation.
Meaning you don't have to care on which side the LEDs are. 
The moving direction still has to be as described. 
Note that the value to switch direction is not near 0 to be significant. 
The sensor is read after the countdown. You should be safe if you start and bring card10 at the right position.








