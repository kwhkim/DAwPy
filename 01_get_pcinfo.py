# hard linked to get_pcinfo.py
import os
import platform
import sys
import socket
import psutil
import cpuinfo
# pip install py-cpuinfo
# cpuinfo is a cross-platform package : 
import psutil
## disk usage, memory, cpu usage for cross-platform
from time import sleep

from pprint import pprint

#import pwd

def get_os_info():
    plat=platform.system()
    dict_ostype = {'Linux':'Linux',
                'Darwin':'Mac',
                'Windows':'Windows'}
    ostype = dict_ostype[plat]
    # Linx = Linux, Darwin = Mac, Windows = Windows
    osrelease = platform.release()
    hostname = socket.gethostname() # socket.getfqdn()

    path = os.environ.get('path')
    
    if ostype == 'Windows':
        username = os.getlogin()
    else:
        import pwd
        username = pwd.getpwuid( os.getuid() )[0]
    return {'os':ostype, 'os_release':osrelease,
            'hostname':hostname, 'username':username, 
            'path':path} 

def get_mem_info():
    meminfo = psutil.virtual_memory()
    return {'total':round(meminfo.total/(1024.0**3),2),
            'used':round(meminfo.used/(1024.0**3),2),
            'available':round(meminfo.available/(1024.0**3),2),
            'free':round(meminfo.free/(1024.0**3),2),
            'percent_used':round(meminfo.percent, 2)}


def get_cpu_info(keys = ('arch', 'bits', 'count', 'hz_actual_friendly',
                    'l2_cache_line_size', 'l2_cache_size', 'l3_cache_size',
                    'python_version')):
    d_cpuinfo = cpuinfo.get_cpu_info()
    return {key:d_cpuinfo[key] for key in keys}                    

def get_disk_info(mountpoint=None): # src https://github.com/510908220/heartbeats
    if mountpoint is None:
        disk_info = []
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    # skip cd-rom drives with no disk in it; they may raise
                    # ENOENT, pop-up a Windows GUI error for a non-ready
                    # partition or just hang.
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            disk_info.append({
                'device':  part.device,
                'total':  usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent,
                'fstype': part.fstype,
                'mountpoint': part.mountpoint
            })
        return disk_info    
    else:
        usage = psutil.disk_usage(mountpoint)
        return {
                'device':  part.device,
                'total':  usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent,
                'fstype': part.fstype,
                'mountpoint': part.mountpoint
               }
    


def copyfile():
    #print(__file__)
    to_basename = os.path.basename(__file__)
    to_dirname = os.path.dirname(__file__)
    to_filename = 'get_pcinfo.py'

    from shutil import copyfile
    print(f'* copying {__file__} to {to_filename}')
    res = copyfile(__file__, to_filename)
    print(f' - result of copyfile(from, to) = {str(res)}')

def main():
    print('* CPU')
    pprint(get_cpu_info())
    print('* MEMORY')
    pprint(get_mem_info())
    print('* DISK')
    pprint(get_disk_info())
    print('* OS')    
    pprint(get_os_info())    

if __name__=="__main__":    
    copyfile()
    main()
