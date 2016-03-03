docker run -d -p 4444:4444 -p 5900:5900 selenium/standalone-firefox-debug:2.52.0

#open 'docker-machine ip default' url in Safari vnc://192.168.99.101:5900
open -a "Safari" vnc://192.168.99.101:5900
#password is secret

