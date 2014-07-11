#!/bin/bash

 curl  "http://210.14.129.43:9880/sms?send=$1&user=op&pwd=191653&source=guopeng.gong" -d "$2"
