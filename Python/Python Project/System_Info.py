from datetime import datetime
import platform

print("-"*10, "> System Information <", "-"*10)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Version: {uname.version}")
print(f"Processor: {uname.processor}")

