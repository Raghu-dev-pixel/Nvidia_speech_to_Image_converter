# Speech to Image Converter
This project titled **Speech-to-image Converter** aims to generate images based on audio/speech as input by leveraging the benefits of Nvidia's AI workbench. The project can be used in various educational and storytelling applications.

## Description
The Speech-to-Image Converter is an advanced generative AI system that allows users to create real-time images from spoken or audio descriptions. While existing generative AI applications such as speech-to-text and text-to-image converters are well-established, little attention has been given to the direct conversion of speech into images. This project aims to bridge that gap by developing a seamless solution using NVIDIA's AI Workbench to convert audio inputs into visual content.

For example, if a user says, **Lion in a Jungle in 4K** the application transcribes the audio and instantly generates a high-resolution image of a lion in the jungle. This provides an intuitive way to transform verbal ideas into visuals, offering new creative opportunities.

**Setup and Tools**
The project utilizes NVIDIA AI Workbench, a platform that simplifies GPU workstation setup, enabling developers to seamlessly work across different hardware environments. It ensures that even users without a local GPU can run the application effectively.

**Architecture Overview**
The system architecture is divided into two key modules:

1) **Speech-to-Text Conversion**
This module leverages OpenAI's Whisper model to transcribe spoken audio into text. Whisper's ability to handle various languages and noisy environments makes it ideal for this task, ensuring that the application is not limited to specific languages or pristine audio quality.
* **Device Optimization**: The system detects whether a GPU is available and automatically uses it for faster processing, otherwise defaulting to the CPU.
* **Processing**: The ASR model processes audio files in 30-second chunks to ensure efficient handling, providing the transcribed text as input to the next module.

2) **Text-to-Image Conversion**
This module generates images from the text output using NVIDIA's Stable Diffusion AI model.
* **API Usage**: It connects to NVIDIA’s GenAI Stable Diffusion API, authenticating with an API key, and sends the transcribed text along with various image generation parameters (such as sampling method, quality scaling, seed, and steps) to the model.
* **Image Generation**: The generated image is returned in base64 format, decoded, and converted into an image using the Python Imaging Library (PIL), which can then be displayed or saved.

**Key Benefits**
1) **Cross-Platform Compatibility**: The application can be run with or without a local GPU, thanks to NVIDIA’s cloud-based APIs.
2) **Language Independence**: The system supports multiple languages for audio input, making it versatile and accessible to a global audience.
3) **Efficient Processing**: By leveraging pre-trained models from NVIDIA's API, the application avoids the need for local model training, ensuring faster image generation.
4) **Ease of Use**: The use of NVIDIA AI Workbench ensures that the project can be easily cloned and run across different platforms, making it accessible to users with diverse hardware setups.

This speech-to-image converter redefines the creative process, enabling users to generate visuals directly from spoken descriptions, whether for design, education, or storytelling purposes.


## Getting Started
Optional section to summarize important steps and how to use the project & apps in the project