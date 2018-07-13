# Swamp IoT Button

## Overview

This was created to be able to remotely toggle a visual display webpage without the need of a computer at hand. This example is for reserving or notifying others that a conference room is in use and is not to be disturbed.

Clicka the button, changa the status. Its that simple.

The script as written expects you to use these pins (Being opensource, you can change these as needed):
- 18 - Red Positive
- 17 - Green Positive
- 16 - Yellow Positive
- 23 - Button Positive

## Requirements

- Raspberry Pi Zero W w/ Power and Micro USB cable
- 1 Tactile button
- 3 LEDs (Yellow, Red, Green) OR 1 Multicolor LED
- 3 Resistors to match your LED requirements
- Access to 3d Printer, or magic, to create case
- Breadboard for testing, soldering iron for production

## Why?

Why What?

### Why didn't you hack an Amazon Dash button?

Due to network restrictions, the network that the dash button would be on has wireless isolation turned on which means, well no ARP requests can be scanned for as well as it simply couldn't talk to the internal webserver for the status page itself anyway.

### Why didn't you just purchase an IoT button off the internet?

I like tinkering.

### Why do your users need a button when you already have a webpage to do this same task?

Users are well.. Users... Let me put it this way.. This button only has ONE button and all you have to do is push it once to toggle busy and once again to toggle open.. and they still wont use it.

### Why did you use a raspberry pi instead of an arduino?

I don't have an arduino to test.

### Why wont this project ever be finished...

<del>Because I am lazy...</del> ... Maybe it will someday..
