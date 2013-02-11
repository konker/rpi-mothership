Raspberry Pi Mothership
==============================================================================
A simple community site where raspberry pi devices can regsiter their details
on boot.

This allows a person to inspect the IP address and some other selected data
about the raspberry pi after it has booted, without need for a monitor and
keyboard.

Could be used by other devices.
JSON/REST API


How It Works
------------------------------------------------------------------------------
Clients POST a JSON structure to the API.
The JSON structure should follow the following example:
  {
      "timestamp": *F<seconds since epch UTC>,
      "uptime_secs": F<uptime seconds>,
      "ip_addresses": [*S<ipv4 address>],
      "ip6_address": [<ipv6 address>],
      "ifconfig": S<ifconfig text>,
      "hostname": S<hostname>,
      "cur_ssid": S<cur wifi AP associated with, if any>,
      "load_average": S<load average>,
      "sys_temperature": F<sys temperature deg. C>,
      "gpu_temperatrure": F<gpu temeratrure deg. C>,
      "available_memory_kb": F<available memory kb>,
      "free_memory_kb": F<free memory kb>,
      "total_space_kb": F<total disk space kb>,
      "free_disk_space_kb": F<free_disk_space_kb>,
      "notes": S<free text>
  }


The ID field can be an arbitrary JSON string.
The user then goes to the web site and enters their ID to search for the record.
Record is displayed if ID is found.
    - If there are more than 1, all are shown
Records expire after a certain time.
    - 1 hour?
Designed to be transient, should not expect data to be long-lived/permanent.


Tech
------------------------------------------------------------------------------
Python, bottle for app
EmberJs for front end
lighttpd, or nginx as web front-end server
Redis as data store
    - can redis expire records automatically?

