# Role `generic-system-hardening`

## State of target system after role execution

- the Debian security updates repository is in the `apt` list of sources;
- the OpenSSH server is configured to only accept public keys for
  authentification;
- only a white list of users is allowed to SSH into the system;
- `sudo` is installed and only a white list of users can acquire superuser
  priviledges with `sudo`;
- users who did not have a password have their password initialised with a hash
  specified in the role's input data;
- users who already had a password set keep their password unless the role's
  input data explicitly specifies to reinitialise it in addition to providing a
  hash.

## Input data

### Required


### Recommended

##### `deflect_ssh_users`

List of users allowed to SSH into the target system. Each item of the list
represents a user and supports the following keys:

- `login` (string) (mandatory): the user's login on the system;
- `sudo` (boolean) (default: `False`): whether or not the user has `sudo`
  access;
- `password` (string): encrypted UNIX password for the user, following the
  `/etc/shadow` format (see the `mkpasswd` tool provided in Debian's `whois`
  package);
- `force_password` (boolean) (default: `False`): whether or not the user's
  password should be set to `password`'s value even if the user was not newly
  created;
- `pubkey` (string) (default: none): one or several SSH public keys, separated
  by new lines; SSH key not listed will be removed from user's `authorized_keys`
  file.

Example:

```
deflect_ssh_users:
  - login: bob
    sudo: True
    password: $6$TYZFllHTbDCBn$Lph3t5eaaM3YTcqKeowf38z5BOxYVgK.a9nrkpaozmDXymX934o/NpGY1WI1wjfbgrPK0keFxPRun93FbdSi81
    pubkey: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEYa5C/1gMUTM9x4MnhhPW1UttT8VFL3/eMxDD6UuPy0MoREdjShdd6v+sA3ivOx8OAu5wt9mgBXcnl6LYaLw9ivPQ6vN3wrFD3eHVsJnRyl6YW4nn9ADeNH+jI96OF7nyUg2D2tEdG+v2BW74hhUePEefZsJV7MfhHB49bynJrpegV0lPeamczddhtMgorgbSyLodqs8TO4o+xvjJPFPD3CriCq38tmBZ02XWq/H8ac/13pwNsQdHTjHGt5fO7YJXoz5KBRUXDvHkf435AMBGc1jCx8PGn4jMcY1vfnlhWoU8/E84kxgykcsTAK16fuaCqJVlFJ/rhiinYqphtBfT
  - login: someone_with_several_keys
    pubkey: |
      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCzszUbgx0wq52iPVOJW//qRGCALW1mUcXdGzPCMcM619slLp2YoKLg0OpurGJHeTN7pbQ/RdrUaJct/TzrLL1fK/HdaSscZV877gjGDpm8Q7ereVn2l6UQivdmUd5Lr3DvJegPTKIbRuY9LDlPk7d4Iu7sxN5dbvshyLM+7LWXfCytt7o/3+rdaLcE/IP7Q168sToax1lZex/KZpNXqGhugMIr3Igj2blWBXkM25qDxP7KdaxKpUUsad9hJ1zZx3nD55Lq9XuWD6/JXcbbo1KXHsojHdwBFwvIInQv0H487QkMI8CMILPCSKfuNkXdZa8cqzc6AujusigMGy1/Hnh3
      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCg5FKGJg7oTqG2g7PNoCCLu6u0ifSXHT4WOjmiVToZu0WANbQBVGXQhfzKosVvCYzioAt/K38Z6LMqf+fRQ3rqXJhYNWsXRtogyO5BJNMmggmZYr2jXZJnmkVxlBaf2YRFUZICNkUlct6hq23nUJgZU/l1/+oCwfhSjKGr/yQ0tPmx1UG4RIwCpg0FvoSHwDQ7D0pnLLtfw0QTH+0QFTTKnmL5HSeCwZlR9/qXo/Fb7ro3bdiipTt8Otug6zs4Y2ydtMZlyDu8JkMz/2kA3k3oyD4YrDZ977AdU/9cTwrmtOTNlZqenb4IZlxWsMwsWRPSil76QB+qldXLPAGk7vcn
```

Default:

```
deflect_ssh_users:
  - login: "{{ ansible_user }}"
    sudo: true
```

### Optional

#### `ssh_listen_ports` (list of integers)

List of TCP ports the OpenSSH daemon will listen on.

Default: only port 22.
