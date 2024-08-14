# Creates a manidest that fixes typos of a filename
exec { 'fix_typo':
  command => 'mv /var/www/html/wp_includes/class_wp_locale.php /var/www/html/wp_includes/class_wp_locale.phpp',
  path => '/bin/'
  }
