from usefuladbplus import activate_pandas_extensions, AdbControlPlus,adbconfig
from usefuladbwithrestart import AdbWRestart
import time 
class Left(AdbControlPlus):
    def __init__(self,*args,**kwargs):
        super(Left, self).__init__(
            adb_path=kwargs.get("adb_path", None),
            device_serial=kwargs.get("device_serial", None),
            use_busybox=kwargs.get("use_busybox", False),
            connect_to_device=kwargs.get("connect_to_device", True),
            invisible=kwargs.get("invisible", True),
            print_stdout=kwargs.get("print_stdout", True),
            print_stderr=kwargs.get("print_stderr", True),
            limit_stdout=kwargs.get("limit_stdout", 3),
            limit_stderr=kwargs.get("limit_stderr", 3),
            limit_stdin=kwargs.get("limit_stdin", None),
            convert_to_83=kwargs.get("convert_to_83", True),
            wait_to_complete=kwargs.get("wait_to_complete", 0.1),
            flush_stdout_before=kwargs.get("flush_stdout_before", False),
            flush_stdin_before=kwargs.get("flush_stdin_before", False),
            flush_stderr_before=kwargs.get("flush_stderr_before", False),
            exitcommand=kwargs.get("exitcommand", "xxxCOMMANDxxxDONExxx"),
            capture_stdout_stderr_first=kwargs.get("capture_stdout_stderr_first", True),
            global_cmd=kwargs.get("global_cmd", True),
            global_cmd_timeout=kwargs.get("global_cmd_timeout", 10),
            use_eval=kwargs.get("use_eval", True),
            eval_timeout=kwargs.get("eval_timeout", 10),
            device_height=kwargs.get("device_height", 0),
            device_width=kwargs.get("device_width", 0),
        )


class Right(AdbWRestart):
    def __init__(self, *args, **kwargs):
        super(Right, self).__init__(*args,**kwargs)

class AdbControlPlusWRestart(Left, Right):
    def __init__(
        self,
        adb_path,
        device_serial,
        use_busybox=False,
        connect_to_device=True,
        print_stdout=False,
        print_stderr=False,
        convert_to_83=True,
        su=False,
        commandtimeout=30,
        escape_filepath=True,
        restart_when_error=True,
        restart_tries=10,
        sleep_after_reconnection_attempt=5,
        device_height=0,
        device_width=0,
        *args,
        **kwargs,
    ):
        super(AdbControlPlusWRestart, self).__init__(
            adb_path=adb_path,
            device_serial=device_serial,
            use_busybox=use_busybox,
            connect_to_device=connect_to_device,
            print_stdout=print_stdout,
            print_stderr=print_stderr,
            convert_to_83=convert_to_83,
            wait_to_complete=0.1,
            su=su,
            commandtimeout=commandtimeout,
            escape_filepath=escape_filepath,
            restart_when_error=restart_when_error,
            restart_tries=restart_tries,
            sleep_after_reconnection_attempt=sleep_after_reconnection_attempt,
            *args,
            **kwargs,
        )
        self.device_height = device_height
        self.device_width = device_width
        self._sendevent_devices = []
        self.hashvalue = hash((time.time(), device_serial))
        adbconfig.all_devices[self.hashvalue] = self

