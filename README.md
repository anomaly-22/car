# car

# CAD design
The RC car consists of a simple chassis that uses two servos for power. One turns the car via a rack and pinion in the front, and the other connects to the back via neutral spur gears
All cad files are in the Car folder
<img width="998" height="813" alt="Image" src="https://github.com/user-attachments/assets/1bbc824f-9355-42aa-b2e9-63a3c0db87bc" />
## Why does this exist
We made this project because our origional project, the robotic centipede, was not able to be completed due to stepper driver fuckery and the lack of print time. But we were able to take some things we learned writing the code for that project into the creation of this one!
## Wiring Diagram
<img width="1300" height="1075" alt="image" src="https://github.com/user-attachments/assets/f0056428-3f4a-4b12-ad12-389e3846a245" />
## Basic how to make
1. modify one servo to be continuous
2. wire the servos as they are in the diagram
3. GRAB CARDBOARD AND PRAY to make the servos fit
4. melt the servo horn to the gear on both areas
5. Flash the code provided and use the circuitpython motors library
# BOM

| Part | Quantity | Use |
|---|---|---|
|micro servo 9g | (x2)| drive and turn the car|
|orpheus pico | (x1) | control everything|
| breadboard | (x1) | connect things |
|jumper wires | (x7) | wire up everything|
|power bank | x1 | power the board and servos |
