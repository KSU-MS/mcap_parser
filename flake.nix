{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system: 
      let 
        pkgs = import nixpkgs {
          inherit system;
          overlays = custom_overlays;
        };

        mcap = pkgs.python312Packages.buildPythonPackage rec {
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
            pkgs.python312Packages.setuptools 
            pkgs.python312Packages.lz4 
            pkgs.python312Packages.zstandard
          ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/python/mcap";
        };

        mcap-protobuf-support = pkgs.python312Packages.buildPythonPackage rec {
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
            pkgs.python312Packages.setuptools 
            pkgs.python312Packages.lz4 
            pkgs.python312Packages.zstandard 
            pkgs.python312Packages.protobuf 
            mcap 
          ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/python/mcap-protobuf-support";
        };

        tkinterdnd2 = pkgs.python312Packages.buildPythonPackage rec {
          pname = "tkinterdnd2";
          version = "1.0.0";
          format = "pyproject";

          src_repo = pkgs.fetchFromGitHub {
            owner = "Eliav2";
            repo = "tkinterdnd2";
            rev = "9a55907e430234bf8ab72ea614f84af9cc89598c";
            sha256 = "sha256-ataKvBsFqKcuz7C2JfhnG7vjB9OspkBYyMWXOrGlCog=";
          };

          propagatedBuildInputs = [ pkgs.python312Packages.setuptools ];

          # Extract the specific subdirectory within the repository
          src = src_repo + "/";
        };

        pkg_overlay = final: prev: {
          mcap_parser = final.callPackage ./default.nix { 
            mcap = mcap; 
            mcap-protobuf-support = mcap-protobuf-support;
          };
        };
        custom_overlays = [ pkg_overlay ];

      in with pkgs; {
        overlays.default = nixpkgs.lib.composeManyExtensions custom_overlays;

        packages = rec {
          mcap_parser = pkgs.mcap_parser;
          default = mcap_parser;
        };

        devShells.default = mkShell {
          venvDir = ".venv";
          packages = [ 
            ([ pkgs.python312 ] ++ (with pkgs.python312Packages; [
              mcap         
              mcap-protobuf-support
              tkinterdnd2
              tkinter
              customtkinter
              argparse
              pyinstaller
              numpy
              pandas
              matplotlib
              pip
            ]))
          ];
        };
      }
    );
}
