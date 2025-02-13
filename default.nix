{ pkgs, mcap, mcap-protobuf-support, ... }:

pkgs.stdenv.mkDerivation {
  pname = "mcap_parser";
  version = "1.0.0";

  src = ./mcap_parser;

  buildInputs = [
    ([ pkgs.python312 ] ++ (with pkgs.python312Packages; [
      mcap         
      mcap-protobuf-support
      tkinter
      customtkinter
      pyinstaller
      numpy
      pandas
      matplotlib
    ]))
  ];

  # customtkinterPath = builtins.toString pkgs.python311Packages.customtkinter;

  installPhase = ''
    pyinstaller --noconfirm --onedir --windowed --add-data "/nix/store/q5i6v39hjqx359n5w0chqqkkzgrppv8r-python3.12-customtkinter-5.2.2/lib/python3.12/site-packages/customtkinter/:customtkinter/" "./mcap_parser.py"
    mkdir -p $out
    mv ./dist $out
  '';
}
