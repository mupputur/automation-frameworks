import logging


class Loggers:

    def config(self, *args, **kwargs):
        logging.basicConfig(*args,**kwargs)
        # logging.warning('This will get logged to a file')

    def info_log(self,msg, *args, **kwargs):
        logging.info(msg,*args, **kwargs)

    def error_log(self,msg, *args, **kwargs):
        logging.error(msg, *args, **kwargs)


if __name__=='__main__':
    fb_log = Loggers()
    fb_log.info_log(f'Hello')
    fb_log.error_log('This is error log')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')