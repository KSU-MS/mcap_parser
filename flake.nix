{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system: 
      let 
        pkgs = import nixpkgs {
          inherit system;
        };

        mcap = pkgs.python311Packages.buildPythonPackage rec {
          pname = "mcap";
          version = "1.2.2";
          format = "pyproject";

          src_repo = pkgs.fetchFromGitHub {
            owner = "foxglove";
            repo = "mcap";
            rev = "releases/python/mcap/v${version}";
            sha256 = "VC2CfNEY7CrIwIonSvx0zsCuwcBJKvzh8+l/Ff6MJp0=";
          };

          propagatedBuildInputs = [ pkgs.python311Packages.setuptools pkgs.python311Packages.lz4 pkgs.python311Packages.zstandard ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/python/mcap";
        };

        mcap-protobuf-support = pkgs.python311Packages.buildPythonPackage rec {
          pname = "mcap";
          version = "1.2.2";
          format = "pyproject";

          src_repo = pkgs.fetchFromGitHub {
            owner = "foxglove";
            repo = "mcap";
            rev = "releases/python/mcap/v${version}";
            sha256 = "VC2CfNEY7CrIwIonSvx0zsCuwcBJKvzh8+l/Ff6MJp0=";
          };

          propagatedBuildInputs = [ 
            pkgs.python311Packages.setuptools 
            pkgs.python311Packages.lz4 
            pkgs.python311Packages.zstandard 
            pkgs.python311Packages.protobuf 
            mcap 
          ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/python/mcap-protobuf-support";
        };

        nicegui = pkgs.python311Packages.buildPythonPackage rec {
          pname = "nice-gui";
          version = "2.10.1";
          format = "pyproject";

          src_repo = pkgs.fetchFromGitHub {
            owner = "zauberzeug";
            repo = "nicegui";
            rev = "v${version}";
            sha256 = "sha256-XMPW0fWi13cffVF/PY9+lTv6eQo7f2JpjV3wkqmMqQU=";
          };

          propagatedBuildInputs = [ 
            pkgs.python311Packages.setuptools
            pkgs.python311Packages.poetry-core
            pkgs.python311Packages.pygments
            pkgs.python311Packages.aiofiles
            pkgs.python311Packages.aiohttp
            pkgs.python311Packages.certifi
            pkgs.python311Packages.docutils
            pkgs.python311Packages.fastapi
            pkgs.python311Packages.httpx
            pkgs.python311Packages.ifaddr
            pkgs.python311Packages.itsdangerous
            pkgs.python311Packages.jinja2
            pkgs.python311Packages.markdown2
            pkgs.python311Packages.orjson
            pkgs.python311Packages.python-multipart
            pkgs.python311Packages.python-socketio
            pkgs.python311Packages.requests
            pkgs.python311Packages.typing-extensions
            pkgs.python311Packages.urllib3
            pkgs.python311Packages.uvicorn
            pkgs.python311Packages.vbuild
            pkgs.python311Packages.watchfiles
          ];

          src = src_repo;
        };

      in with pkgs; {
        devShells.default = mkShell {
          venvDir = ".venv";
          packages = [
            ([ pkgs.python311 ] ++ (with pkgs.python311Packages; [
              mcap         
              mcap-protobuf-support
              nicegui
              argparse
              pyinstaller
              numpy
              pandas
              matplotlib
            ]))
          ];
        };
      }
    );
}
