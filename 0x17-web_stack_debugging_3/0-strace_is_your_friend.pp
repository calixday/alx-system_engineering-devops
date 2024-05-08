# A puppet manuscript to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# Ensure the directory exists
file { '/var/www/html':
  ensure => directory,
}

# Ensure the file exists
file { $file_to_edit:
  ensure => file,
  mode   => '0644',
}

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command     => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path        => ['/bin','/usr/bin'],
  onlyif      => "test -f ${file_to_edit}",
  refreshonly => true,
}

