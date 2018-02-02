# Role `ats-banjax-swabber`

## State of target system after role execution

- Apache Traffic Server (ATS) is installed on the target system solely in binary
  form (the role provides the option to either compile the binaries from source
  on the target — in which case neither the source code or the build-time
  dependencies are kept on the target after compilation — or to fetch them in
  binary form from a location given by input data);
- [Banjax](https://github.com/equalitie/banjax) is installed as an ATS module
  and kept on the target only in binary form (as above, the role supports
  on-target compilation as well as fetching the binary);
- ATS is configured to load and use the banjax module;
- [swabber](https://github.com/equalitie/swabber) is installed on the target
  system solely in binary form (as above, the role supports on-target
  compilation as well fetching as the binary).

## Input data

- the versions to install of:
    - ATS (default: 7.1.1);
    - Banjax (default: 2.0.0);
    - swabber (default: 1.3.5);
- for each of ATS, Banjax and swabber, one optional URL to fetch packaged
  binaries from (default: none);
- for each of ATS, Banjax and swabber, one optional checksum for each file to
  download (default: none).
