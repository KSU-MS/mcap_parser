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

        tkinterdnd2 = pkgs.python311Packages.buildPythonPackage rec {
          pname = "tkinterdnd2";
          version = "1.0.0";
          format = "pyproject";

          src_repo = pkgs.fetchFromGitHub {
            owner = "Eliav2";
            repo = "tkinterdnd2";
            rev = "9a55907e430234bf8ab72ea614f84af9cc89598c";
            sha256 = "sha256-ataKvBsFqKcuz7C2JfhnG7vjB9OspkBYyMWXOrGlCog=";
          };

          propagatedBuildInputs = [ pkgs.python311Packages.setuptools ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/";
        };

      in with pkgs; {
        devShells.default = mkShell {
          venvDir = ".venv";
          packages = [ 
            pkgs.xorg.libXcursor

            ([ pkgs.python311 ] ++ (with pkgs.python311Packages; [
              mcap         
              mcap-protobuf-support
              tkinterdnd2
              customtkinter
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
