#!/usr/bin/python2
import os
import sys, getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hsr:e:d:",["help","status","reassign=", "enable=", "disable="])
   except getopt.GetoptError:
      print("python cpu_setting.py -h/--help")
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help") :
         print("usage: python cpu_setting.py [option] [arg]")
         print("Options and arguments")
         print("-h           : print this help message and exit (also --help)")
         print("-s           : print status of CPU assignment (also --status)")
         print("-r CPU# VM#  : reassign CPU core to VM (also --reassign)")
         print("-e CPU# ...  : enable CPU cores (also --enable)")
         print("-d CPU# ...  : disable CPU cores (also --disable)")
         sys.exit()
      elif opt in ("-s", "--status"):
         os.system("/usr/bin/vlm-cpuhg/cpuhg")
      elif opt in ("-r", "--reassign"):
         command = "/usr/bin/vlm-cpuhg/cpuhg CPU" + argv[1] + ":" + argv[2]
         os.system(command)
      elif opt in ("-e", "--enable"):
         for i in range(len(argv)-1):
            command = "echo 1 > /sys/devices/system/cpu/cpu" + argv[i+1] + "/online"
            os.system(command)
      elif opt in ("-d", "--diable"):
         for i in range(len(argv)-1):
            command = "echo 1 > /sys/devices/system/cpu/cpu" + argv[i+1] + "/online"
            os.system(command)
            command = "echo 0 > /sys/devices/system/cpu/cpu" + argv[i+1] + "/online"
            os.system(command)
   if len(argv) == 0:
      print("python cpu_setting.py -h/--help")

if __name__ == "__main__":
   main(sys.argv[1:])
