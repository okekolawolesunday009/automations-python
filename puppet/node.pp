  GNU nano 6.2                                        manifests/init.pp *
class packages {
    package { 'python3-requests':
        ensure => installed,
    }
    if $facts[os][family] == "Debian" {
        package { 'goalng':
           ensure => installed
     }
    }
    if $facts[os][family] == "RedHat" {
        package { 'nodejs' :
          ensure => installed,
        }
    }
}

