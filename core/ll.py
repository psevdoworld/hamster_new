from datetime import datetime
start = datetime.now()
end = datetime.now()
counter = 0
while (end-start).total_seconds() < 1:
    counter += 1
    print('',end='')
    end = datetime.now()

print(counter)
        
