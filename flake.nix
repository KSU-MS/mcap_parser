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
          format="pyproject";

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
          format="pyproject";

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

      in with pkgs; {
        devShells.default = mkShell {
          venvDir = ".venv";
          packages = [
            ([ pkgs.python311 ] ++ (with pkgs.python311Packages; [
              mcap         
              mcap-protobuf-support
              argparse
              customtkinter
              # tkinterdnd2
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
