from datetime import datetime


def logger(f):
    """results: Decorator that generate json file to associated tests
    :param f: Function that uses this decorator
    """
    def logger_wrapper(*args, **kwargs):
        return_element = False
        log_info = []
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("[{}]".format(current_time), end="")
        try:
            args = f(*args, **kwargs)
            log_info = args[0]
            return_element = args[1]
            print(log_info)
        except IndexError as e:
            print(e)
            log_info = ["Calling function does not provide required parameters"]
            print(log_info)
            return_element = False
        except Exception as e:
            print(e)
            return_element = False
        finally:
            save_logs(log_info, current_time)
            return return_element
    return logger_wrapper


def save_logs(logs, time):
    """ Saving logs to .txt file
    :param logs: logs to save
    :param time: current time
    """
    try:
        with open("./logs/logs.txt", "a") as f:
            f.write("\n[{}]: {}".format(time, logs[0]))
    except Exception as e:
        print(e)
