﻿# Auto-ContentMarketing-Generator
```Replace OPENAI_API_KEY and SERPER_API_KEY with your personal API key in file apikey.py```
# Build docker
```docker build -t tagname .```
# Run
```docker run -p 5001:5001 tagname```
```docker run -p 5001:5001 -e OPENAI_API_KEY=YOUR_OPENAI_API_KEY -e SERPER_API_KEY=YOUR_SERPER_API_KEY tagname```