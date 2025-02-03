#!/bin/bash
cd /media/docker/litellm
git add . && git commit -m "Auto-update $(date)" && git push -f origin main