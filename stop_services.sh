#!/bin/bash

ps -ef | grep 'swamp_' | grep -v grep | awk '{print $2}' | xargs -r kill -9
