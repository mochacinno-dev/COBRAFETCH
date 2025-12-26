##########################
# Cobrafetch 0.9.1
# Ruby System Information Fetching Module
# Written by: Camila "Mocha" Rose
##########################

require 'rbconfig'

def shell_fetch
  if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
    # Windows: Get shell from COMSPEC or default to cmd.exe
    shell = ENV['COMSPEC'] || ENV['SHELL'] || 'cmd.exe'
  else
    shell = ENV['SHELL'] || 'Unknown'
  end
  puts "<=== SHELL: #{File.basename(shell)}"
end

def uptime_fetch
  if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
    # Windows: Use systeminfo to get uptime
    begin
      output = `wmic os get lastbootuptime 2>nul`.split("\n")[1].strip
      if output && !output.empty?
        # Parse WMIC timestamp (format: YYYYMMDDHHmmss.mmmmmm+zzz)
        boot_time = Time.new(output[0..3], output[4..5], output[6..7], 
                             output[8..9], output[10..11], output[12..13])
        uptime_seconds = (Time.now - boot_time).to_i
        hours = uptime_seconds / 3600
        minutes = (uptime_seconds % 3600) / 60
        puts "<=== UPTIME: #{hours}h #{minutes}m"
      else
        puts "<=== UPTIME: Unknown"
      end
    rescue
      puts "<=== UPTIME: Unknown"
    end
  else
    # Linux/Unix
    uptime_output = `cat /proc/uptime 2>/dev/null`.split[0].to_f rescue 0
    hours = (uptime_output / 3600).to_i
    minutes = ((uptime_output % 3600) / 60).to_i
    puts "<=== UPTIME: #{hours}h #{minutes}m"
  end
end

def packages_fetch
  pkg_count = 0
  
  if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
    # Windows: Check for common package managers
    if system('where choco >nul 2>&1')
      pkg_count = `choco list --local-only 2>nul | find /c /v ""`.to_i - 1
    elsif system('where scoop >nul 2>&1')
      pkg_count = `scoop list 2>nul | find /c /v ""`.to_i - 2
    elsif system('where winget >nul 2>&1')
      pkg_count = `winget list 2>nul | find /c /v ""`.to_i - 4
    end
  else
    # Linux: Check different package managers
    if system('which dpkg > /dev/null 2>&1')
      pkg_count = `dpkg -l | grep ^ii | wc -l`.to_i
    elsif system('which rpm > /dev/null 2>&1')
      pkg_count = `rpm -qa | wc -l`.to_i
    elsif system('which pacman > /dev/null 2>&1')
      pkg_count = `pacman -Q | wc -l`.to_i
    end
  end
  
  puts "<=== PACKAGES: #{pkg_count}"
end

def rubyfetch
  shell_fetch
  uptime_fetch
  packages_fetch
end

# Run if called directly
rubyfetch if __FILE__ == $PROGRAM_NAME