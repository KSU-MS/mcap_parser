{
  description = "Basic python dev-shell bc fuck python";

  # Anything our flake needs from the internet
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    mach-nix.url = "github:davhau/mach-nix";
  };

  # Anything our flake outputs
  outputs = { self, nixpkgs, mach-nix }: let 
    # Abstract what platform we are building for
    forAllSystems = function: nixpkgs.lib.genAttrs [
      "x86_64-linux"
      "aarch64-linux"
    ] (system: function (import nixpkgs { inherit system; }));

    machNix = import mach-nix { inherit nixpkgs; };

  in {
    devShells = {
      default = machNix.mkPythonShell {
        requirements = ./requirements.txt;
      };
    };
  };
}
