# Role `ats-banjax-swabber`

## State of target system after role execution

- Apache Traffic Server (ATS) is compiled from source and installed on the
  system, and the source code is not kept on the system;
- [Banjax](https://github.com/equalitie/banjax) is compiled from source and
  installed as an ATS module, and its source code is not kept;
- ATS is configured to load and use the banjax module;
- [swabber](https://github.com/equalitie/swabber) is compiled from source and
  installed, and the source code is not kept;
- software packages required for compilation but not for run time are not kept
  on the system.

## Input data

- the version of ATS (default: 7.1.1);
- the version of Banjax (default: 2.0.0);
- the version of swabber (default: 1.3.5).
