# Role `generic-system-hardening`

## Actions performed on the target system

- adds Debian security updates repository if necessary;
- configures the OpenSSH server to only accept public key authentication (no
  password);
- exclusively allows a specific set of users to SSH into the server;
- installs `sudo` if not present and sets a specific list of users to be able to
  use `sudo`;
- sets users' encrypted passwords if specified (to be used for `sudo`).

## Input data

- the TCP port(s) the SSH server listens on (default: only port 22);
- a list of allowed SSH logins (default: only the user used as Ansible login);
- a list of logins allowed to use `sudo` (default: only the user used as Ansible
  login);
- an encrypted login password for each user (default: no password is set if not
  specified).
