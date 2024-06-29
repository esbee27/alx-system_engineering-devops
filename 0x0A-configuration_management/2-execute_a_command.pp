# Kills a command
exec { 'killmenow':
  command => 'usr/bin/kpill killmenow'
  provider => 'shell',
  returns => [1, 0],
}
