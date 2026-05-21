# Brain Computer Interface for Autonomous Navigation 

This GitHub repository constitutes the codebase for my thesis, and final year bachelor's project, at the University of Edinburgh. This was completed in partial fulfilment of my degree from September 2025 to April 2026. My supervisor as a part of this project was *Prof. Dr. Tughrul Arslan*. 

## Project Description 

This section is basically brief introduction to what this project is trying to accomplish and the basic prerequisites for this project. 

### Brain Computer Interfaces

These are a subset of *Human Computer Interaction* interfaces, that enable interaction with computing devices and actuators with brain signals. The brain signals are usually *electroencephalography* (EEG) signals collected using dry electrodes, in this study we use the [*PiEEG-16*](https://www.pieeg.com/hardware/pieeg-16) - this link is working as of May 2026. 

### This project 

This project uses *Motor Imagery* (MI), to control the interface where the user is expected to imagine some sort of motion pertaining to a specific intent. The interface classifies this intent and sends said classification to the actuator to take action accordingly.

--- 

## How to run the interface :

Prerequisite: Install [`node.js`](https://nodejs.org/en).  

Run these commands : 

```sh
git clone <repository-url>
cd brain-computer-interface-project/client 
npm run dev 
```

### Windows

You need to have `git` installed. Follow the instructions [from the official `git` website](https://git-scm.com/install/windows).  