raspivid -o - -t 0 -n -w 480 -h 360 -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://192.168.2.254:8554/}' :demux=h264
