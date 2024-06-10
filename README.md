# Gesture Control Using Computer Vision

## Overview

This project is part of the Software Development for Smart Glasses, developed as a final year engineering project. The Gesture Control software uses computer vision to recognize and interpret hand gestures, enabling users to control various functionalities of smart glasses without the need for physical buttons or touchscreens. The primary goal is to enhance the hands-free user experience for smart glasses.

## Features

- **Hand Gesture Recognition**: Utilizes advanced computer vision techniques to detect and recognize various hand gestures.
- **Volume Control**: Adjusts the system volume based on recognized hand gestures.
- **Real-time Processing**: Processes video feed in real-time for immediate response.
- **Customizable Gestures**: Allows users to define custom gestures for specific actions.
- **Cross-Platform Compatibility**: Compatible with multiple operating systems, including Windows, Linux, and macOS.

## Technologies Used

- **OpenCV**: For real-time computer vision processing.
- **Python**: The primary programming language for development.
- **Mediapipe**: For hand tracking and gesture recognition.
- **PyCaw**: For audio control.

## Installation

### Prerequisites

- Python 3.x
- OpenCV
- Mediapipe
- PyCaw

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/gesture-control-cv.git
   cd gesture-control-cv
2. **Install the required dependencies:
   ```sh
   pip install opencv-python mediapipe pycaw comtypes
3. **Run the application:
   ```sh
   python gestureControl.py

## Usage
1. Ensure your webcam is connected and functional.
2. Run the application using the command above.
3. The application window will display the video feed.
4. Use hand gestures in front of the webcam to control the system volume.
5. The recognized gestures will trigger corresponding actions, such as increasing or decreasing the volume.

## Configuration
- **Gesture Mapping:** The gesture-to-action mappings can be customized by editing the gestureControl.py file.
- **Sensitivity:** Adjust the gesture recognition sensitivity by modifying parameters in the HandTackingModule.py file.

## Acknowledgements
- Special thanks to the OpenCV and Mediapipe communities for their excellent libraries.
- Thanks to our project advisors and mentors for their guidance and support.
