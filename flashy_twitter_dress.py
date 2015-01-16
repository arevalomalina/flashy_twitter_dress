from twython import TwythonStreamer
import urllib2

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        urllib2.urlopen('https://agent.electricimp.com/ldq9C8yJxKUP?led=1')

    def on_error(self, status_code, data):
        print status_code

# Want to stop trying to get data because of the error?
# Uncomment the next line!
# self.disconnect()


streamer = MyStreamer(
    'SyOShbVqxyr67ULZxLLNk9K3i',
    'Gs5MHum4LFxJ4uxSH5VOJKgFG9kqPWVupMv8dE9leeosMSjIqT',
    '2572929330-YPMaWiqdSZNO5sBDVeqYnJ7tuhn1hfDwK5UzWuE', 
    'Y2kCBuTrUAeeLMFnKxrTKqwAbp1h80ZrKpYjF4qYbr8ki')

def check_twitter():
    streamer.statuses.filter(track='mariemalina')

if __name__ == '__main__':
    check_twitter()