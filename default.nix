{ pkgs, mcap, mcap-protobuf-support, ... }:

pkgs.stdenv.mkDerivation {
  pname = "mcap_parser";
  version = "1.0.0";

  src = ./mcap_parser;

  buildInputs = [
    ([ pkgs.python311 ] ++ (with pkgs.python311Packages; [
      mcap         
      mcap-protobuf-support
      customtkinter
      pyinstaller
      numpy
      pandas
      matplotlib
    ]))
  ];

  customtkinterPath = builtins.toString pkgs.python311Packages.customtkinter;

  installPhase = ''
    pyinstaller --noconfirm --onedir --windowed --add-data "/nix/store/qqm523a9cd5ifg42d6v2dkh5363y1qsf-python3.11-customtkinter-5.2.2/lib/python3.11/site-packages/customtkinter:customtkinter/" "./mcap_parser.py"
    mkdir -p $out
    mv ./dist $out
  '';
}
