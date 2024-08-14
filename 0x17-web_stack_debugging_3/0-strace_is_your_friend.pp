# Creates a manidest that fixes typos of a filename
exec { 'fix_wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path => 'usr/local/bin/:/bin/'
  }
