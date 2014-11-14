RemoteControlledPiCar
=====================

This Remote Controlled Pi car is controlled via a website (as long as you and the pi are on the same network)
Im going to try and break this down as simply as possible. I used a raspbery pi to control an rc car. The main components 
are a rasperby pi model B, RC car from spark fun, wifi usb, external powersupply, webcam, dual motor relay switch, and a battery pack for the relay switch. 

1. I enabled motion on my pi for streaming video, I also enabled ssh on my pi
2. We (my team including my self and partner Chad) set up a webpage that opens a websocket to send message to the pi 
3. Given our set up we made our car move in bursts, we have it moving for about 0.4 seconds at a time, now that might 
not sound like a lot but any longer and the relay switch will draw in more power and make the car go faster. We did not 
put in any resistors to regualte the current flow. 
4. Create the code that takes in messages from our webpage, and move the car accordingly. 
5. Have fun spying around campus. 
6. I will include pictures and possible links to where I got all the parts from at a later time. 
