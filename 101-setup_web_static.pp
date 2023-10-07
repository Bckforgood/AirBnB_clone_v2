# 101-setup_web_static.pp

# Create the directory structure for web_static
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
}

# Create a symbolic link to the test folder
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Set ownership to ubuntu user and group
exec { 'change_ownership':
  command => 'chown -R ubuntu:ubuntu /data',
}

