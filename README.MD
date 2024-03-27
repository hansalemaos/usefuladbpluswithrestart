# usefuladbplus with restart


### A version of https://github.com/hansalemaos/usefuladbplus that automatically reconnects if it gets disconnected

### pip install usefuladbpluswithrestart


```py
from usefuladbpluswithrestart import (
    AdbControlPlusWRestart,
    activate_pandas_extensions,
)
from PrettyColorPrinter import add_printer

add_printer(1)
activate_pandas_extensions(
    modules=(
        "plus_find_shapes",
        "plus_template_matching",
        "plus_color_search_c",
        "plus_color_cluster",
        "plus_count_all_colors",
        "plus_count_all_colors_coords",
        "plus_fuzzy_merge",
        "plus_tesser_act",
    )
)
adb = AdbControlPlusWRestart(
    adb_path=r"C:\ProgramData\chocolatey\lib\adb\tools\platform-tools\adb.exe",
    device_serial="127.0.0.1:5845",
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
)

df = adb.plus_activity_elements_dump(
    with_screenshot=True,
    screenshot=None,
    with_sendevent=False,
)
print(df)

df1 = adb.plus_uidump(
    timeout=60,
    with_screenshot=True,
    screenshot=None,
    nice=False,
    su=False,
    with_sendevent=False,
)
print(df1)

```