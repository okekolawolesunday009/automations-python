package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}

 # gem install puppet-lint
 #  puppet-lint /etc/puppet/modules
 # puppet-lint --fix /etc/puppet/modules