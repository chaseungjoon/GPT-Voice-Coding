# GPT-Voice-Coding
This code uses OpenAI's GPT 3.5 model to convert real-time audio to python code and creates a .py file containing the code.


[ACTIONS NEEDED BEFORE COMPILING THE CODE]

1. Create an OpenAI account and get access to your own API Key, in which you will use in line8 and 13 of the code. (The API request for this code is NOT FREE, but you will get 18$ worth of tokens once you sign up.)

2. Type in your project directory at line70. (i.e. C:/Users/user/PycharmProjects/pythonProject)


[How to Use]

1. Execute the code in the terminal.

2. Once the recording starts, speak the code you wish to write into the microphone.

3. When you're done and wish to stop recording, press Ctrl-C to exit the code.

4. A new.py file contating your spoken code will be created in the project directory


[Features]

Because GPT's chat completion is used, You can also just say "Write a code for Quicksort" into the microphone and the corresponding code will be created.

If you wish to voice code to a different programming language, fix the following parts of the code. (i.e. C++)

1. line18 : 'python syntax' into 'C++ syntax'

2. line72 : 'new.py' into 'new.cpp'

3. line74 : 'Your .py file' to 'Your .cpp file'
