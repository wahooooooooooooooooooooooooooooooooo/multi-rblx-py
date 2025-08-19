import ctypes
k = ctypes.windll.kernel32
m = k.CreateMutexW(None, True, "ROBLOX_singletonEvent")
input()
