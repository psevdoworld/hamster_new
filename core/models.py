from django.db import models
from datetime import datetime
from time import sleep
class Code(models.Model):
    input_text = models.TextField(default="", blank=True) # <---
    text = models.TextField(default="", blank=True)
    result = models.TextField(default="", blank=True)
    is_done = models.BooleanField(default=False)
    execution_time = models.FloatField(null=True, blank=True)
    def run_code(self):
        self.result = ""
        def print(*args,sep=" ", end="\n"):
            args = list(map(str,args))
            sleep(1/350)
            self.result+= sep.join(args)+end
        inp_text = self.input_text.split("\n")
        def input(podskazka=""):
            res =  inp_text.pop(0)
            print(podskazka+res)
            return res
        #DANGER ZONE
        start = datetime.now()
        try:
            exec(self.text)
        except Exception as e:
            print(e)
        end = datetime.now()
        self.execution_time = (end-start).total_seconds()
        self.is_done = True
        #/DANGER ZONE
        
    def save(self,*args,**kwargs):
        self.run_code()
        res = super().save(*args,**kwargs)
        return res
    #python manage.py shell
