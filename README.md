﻿# Auto-ContentMarketing-Generator
```Replace OPENAI_API_KEY and SERPER_API_KEY with your personal API key in file apikey.py```
# Build docker
```docker build -t tagname .```
# Run
```docker run -p 5001:5001 tagname```
```docker run -p 5001:5001 -e OPENAI_API_KEY=YOUR_OPENAI_API_KEY -e SERPER_API_KEY=YOUR_SERPER_API_KEY tagname```
# Run with other container eg. Backend
```docker run -p 5001:5001 --network [network-name] -e OPENAI_API_KEY=YOUR_OPENAI_API_KEY -e SERPER_API_KEY=YOUR_SERPER_API_KEY tagname```
