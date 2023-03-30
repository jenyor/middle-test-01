{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.flake8
    python3Packages.pytest
    python3Packages.pytest-html
  ];
}
