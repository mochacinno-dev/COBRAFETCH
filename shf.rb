def shell_fetch
  shell = ENV['SHELL'] || 'Unknown'
  puts "<=== SHELL: #{File.basename(shell)}"
end

def uptime_fetch
  uptime_output = `cat /proc/uptime 2>/dev/null`.split[0].to_f rescue 0
  hours = (uptime_output / 3600).to_i
  minutes = ((uptime_output % 3600) / 60).to_i
  puts "<=== UPTIME: #{hours}h #{minutes}m"
end

def packages_fetch
  pkg_count = 0
  
  # Check different package managers
  if system('which dpkg > /dev/null 2>&1')
    pkg_count = `dpkg -l | grep ^ii | wc -l`.to_i
  elsif system('which rpm > /dev/null 2>&1')
    pkg_count = `rpm -qa | wc -l`.to_i
  elsif system('which pacman > /dev/null 2>&1')
    pkg_count = `pacman -Q | wc -l`.to_i
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