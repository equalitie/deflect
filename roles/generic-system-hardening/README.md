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

- the TCP port(s) the SSH server listens on (default: only port 22);
- a list of allowed SSH logins (default: only the user used as Ansible login);
- a list of logins allowed to use `sudo` (default: only the user used as Ansible
  login);
- an encrypted login password for each user (default: no password is set if not
  specified).
