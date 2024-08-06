# puppet example snippets

```java
class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
  }
}
```

## About this code

View the `ntp.pp` manifest file by entering editing mode with the `vim` command. This file contains resources related to the NTP configuration: the ntp package, the ntp configuration file, and ntp service.

The relationships between these resources are also included in the code. In Puppet, code that defines a resource begins with a lowercase letter, whereas code that defines a relationship begins with a capital letter. The ntp configuration file requires the ntp package, which is indicated with the code `require => Package['ntp']`. The ntp service requires the ntp configuration file, which is indicated with the code `require => File['/etc/ntp.conf']`. Additionally, the ntp configuration file resource notifies the ntp service when it is present, which is indicated by the code `notify  => Service['ntp']`.

```javascript
vim ntp.pp
class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/etc/ntp.conf'],
  }
}
include ntp

```

```console
sudo puppet apply -v ntp.pp

# output
Notice: Compiled catalog for ubuntu in environment production in 0.42 seconds

Info: Applying configuration version '1574775824'

Notice: /Stage[main]/Ntp/Package[ntp]/ensure: created

Info: /Stage[main]/Ntp/File[/etc/ntp.conf]: Filebucketed /etc/ntp.conf to puppet with sum aaad5b52b0cfa143eab6b62b247a1c19

Notice: /Stage[main]/Ntp/File[/etc/ntp.conf]/content: content changed '{md5}aaad5b52b0cfa143eab6b62b247a1c19' to '{md5}cebe9424982d7a311aafcf85c6410389'

Info: /Stage[main]/Ntp/File[/etc/ntp.conf]: Scheduling refresh of Service[ntp]

Notice: /Stage[main]/Ntp/Service[ntp]: Triggered 'refresh' from 1 event

Notice: Applied catalog in 6.55 seconds
```

```markdown
vim ntp.conf

driftfile /var/lib/ntp/ntp.drift
statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable

server 0.pool.ntp.org
server 1.pool.ntp.org
server 2.pool.ntp.org
server 3.pool.ntp.org

restrict -4 default kod notrap nomodify nopeer noquery limited
restrict -6 default kod notrap nomodify nopeer noquery limited

restrict 127.0.0.1
restrict ::1

restrict source notrap nomodify noquery
```

## About this code

The command node default installs the sudo and ntp classes on all default nodes. The sudo class is installed with its default parameters, because no parameters are specified. The ntp class is installed with an additional parameter, indicated by `servers => ['ntp1.example.com', 'ntp2.example.com']`.

```java
node default {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
} /
```
## About this code

The command node `webserver.example.com` installs the sudo, ntp, and apache classes on nodes with the fully-qualified domain name (FQDN) webserver.example.com.

Note: Because nodes with this FQDN have a specific set of classes that apply to them, the `node default` command will not apply any classes to them.

```java
node webserver.example.com {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
  class { 'apache': }
}
```

### About this code
This code runs an rspec test to determine whether the `gksu` package has the intended behavior when the fact `is_virtual` is set to `false`. When this is the case, the `gksu` package should have the ensure parameter set to latest: `ensure('latest').`

```javascript
describe 'gksu', :type => :class do
  let (:facts) { { 'is_virtual' => 'false' } }
  it { should contain_package('gksu').with_ensure('latest') }
end

```