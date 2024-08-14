# Creates a manidest that fixes typos of a filename
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path => '/bin/'
  }
