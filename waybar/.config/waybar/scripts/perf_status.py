#!/usr/bin/env python3
import json
import subprocess
import os
import time

def get_cpu_usage():
    try:
        with open('/proc/stat', 'r') as f:
            line1 = f.readline()
        time.sleep(0.1)
        with open('/proc/stat', 'r') as f:
            line2 = f.readline()
        
        parts1 = [float(x) for x in line1.split()[1:]]
        parts2 = [float(x) for x in line2.split()[1:]]
        
        idle1, total1 = parts1[3], sum(parts1)
        idle2, total2 = parts2[3], sum(parts2)
        
        idle_delta = idle2 - idle1
        total_delta = total2 - total1
        
        if total_delta == 0:
            return 0.0
        return (1.0 - idle_delta / total_delta) * 100.0
    except Exception:
        try:
            with open('/proc/loadavg', 'r') as f:
                return float(f.read().split()[0]) * 10.0
        except Exception:
            return 0.0

def get_mem_usage():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
        mem_total = 0
        mem_free = 0
        mem_buffers = 0
        mem_cached = 0
        for line in lines:
            if line.startswith("MemTotal:"):
                mem_total = int(line.split()[1])
            elif line.startswith("MemFree:"):
                mem_free = int(line.split()[1])
            elif line.startswith("Buffers:"):
                mem_buffers = int(line.split()[1])
            elif line.startswith("Cached:"):
                mem_cached = int(line.split()[1])
        
        used = mem_total - (mem_free + mem_buffers + mem_cached)
        pct = (used / mem_total) * 100.0 if mem_total > 0 else 0.0
        return used / 1024 / 1024, mem_total / 1024 / 1024, pct
    except Exception:
        return 0.0, 0.0, 0.0

def get_disk_usage():
    try:
        res = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
        lines = res.stdout.strip().split('\n')
        if len(lines) > 1:
            parts = lines[1].split()
            used = parts[2]
            total = parts[1]
            pct_str = parts[4].replace('%', '')
            return used, total, float(pct_str)
    except Exception:
        pass
    return "0G", "0G", 0.0

def get_top_processes():
    try:
        res = subprocess.run(
            ["ps", "-eo", "pcpu,pmem,comm", "--sort=-pcpu"],
            capture_output=True, text=True
        )
        lines = res.stdout.strip().split('\n')
        processes = []
        for line in lines[1:6]:
            parts = line.split(None, 2)
            if len(parts) >= 3:
                pcpu, pmem, comm = parts
                processes.append((pcpu, pmem, comm))
        return processes
    except Exception:
        return []

def make_bar(pct, color):
    num_blocks = int(round(pct / 10.0))
    bar = ""
    for i in range(10):
        if i < num_blocks:
            bar += "█"
        else:
            bar += "░"
    return f"<span color='{color}'><tt>{bar}</tt></span>"

def main():
    cpu = get_cpu_usage()
    mem_used, mem_total, mem_pct = get_mem_usage()
    disk_used, disk_total, disk_pct = get_disk_usage()
    processes = get_top_processes()
    
    try:
        with open('/proc/loadavg', 'r') as f:
            loadavg = ", ".join(f.read().split()[:3])
    except Exception:
        loadavg = "N/A"

    tooltip = ""
    tooltip += "<span color='#5a9fd4'><b>SYSTEM STATUS</b></span>\n"
    tooltip += "<span color='#8090b0'>──────────────────────────────</span>\n"
    tooltip += f"<span color='#e0e8f0'><b>CPU:</b></span>  {make_bar(cpu, '#f0b429')}  <b>{cpu:.1f}%</b>\n"
    tooltip += f"<span color='#e0e8f0'><b>MEM:</b></span>  {make_bar(mem_pct, '#f0b429')}  <b>{mem_used:.1f}/{mem_total:.1f} GB</b> ({mem_pct:.1f}%)\n"
    tooltip += f"<span color='#e0e8f0'><b>DSK:</b></span>  {make_bar(disk_pct, '#5a9fd4')}  <b>{disk_used}/{disk_total}</b> ({disk_pct:.0f}%)\n"
    tooltip += f"<span color='#8090b0'>Load Avg:</span> <span color='#f0b429'>{loadavg}</span>\n"
    tooltip += "<span color='#8090b0'>──────────────────────────────</span>\n"
    tooltip += "<span color='#5a9fd4'><b>TOP PROCESSES (CPU)</b></span>\n"
    
    if processes:
        for pcpu, pmem, comm in processes:
            comm_trunc = comm[:15]
            tooltip += f"<tt>{comm_trunc:<16} {pcpu:>5}% CPU  {pmem:>5}% MEM</tt>\n"
    else:
        tooltip += "No process data available\n"
        
    output = {
        "text": "  󰣇  ",
        "tooltip": tooltip
    }
    print(json.dumps(output))

if __name__ == "__main__":
    main()
