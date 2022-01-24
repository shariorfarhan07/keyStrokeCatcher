import keyboard
from datetime import datetime
import json
date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")+".txt"
date_string=date_string.replace('_','cc').replace(' ','_').replace(':','_')
s=""
print(date_string)
f = open(date_string, "a")
recorded = keyboard.record(until='esc')
for i in recorded:
    js=json.loads(i.to_json())
    if js["event_type"]=="down":
        if js['name']=="space":
            s+=" "
        elif js['name']=="enter" or js['name']=='esc':
            s+='\n'
        elif js['name']=="backspace":
            s=s[:len(s)-1]
        else:
            s+= js['name']
f.write(s)
f.close()



