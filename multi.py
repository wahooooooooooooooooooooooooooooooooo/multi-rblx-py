import ctypes
from ctypes import wintypes

k = ctypes.windll.kernel32
mutex = k.CreateMutexW(None, True, "ROBLOX_singletonEvent")

if mutex == 0:
    error = k.GetLastError()
    print(f"CreateMutex failed with error: {error}")
else:
    error = k.GetLastError()
    if error == 183:
        print("Another instance is already running")
    else:
        print("Mutex created successfully")

input("Press Enter to exit...")

# clean
if mutex:
    k.CloseHandle(mutex)
