from datetime import datetime, timedelta
import time



class SysDate:
    
    def __init__(self):
        pass
    
    def set_sys_clock(self, **kwargs):
        pass
    
    def set_sys_date_time(self, new_date_time):
        pass

    def get_sys_date(self, dformat="DD-MM-YYYY"):
        pass

    def get_date_time(self, dformat="DD-MM-YYYY HH:MM:SS"):
        pass

    def set_sys_date_ahead(self, n_days):
        pass

    def set_sys_date_behind(self, n_days):
        pass
