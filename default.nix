{ pkgs }:

pkgs.stdenv.mkDerivartion {
  name = "mcap_parser";

  src = ./mcap_parser;

  buildInputs = [

  ];

  installPhase = ''
    mkdir -p $out
  '';
}
