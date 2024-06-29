# Creates a file in the /tmp directory
file { '/tmp/school':
  ensure => 'file',
  group => 'www-data',
  content => 'I love Puppet',
  owner => 'www-data',
  mode => '0744',
}
